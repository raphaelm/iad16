use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
use std::path::Path;

#[cfg(test)]
mod tests;

#[derive(PartialEq)]
pub enum EdgeWeightTypes {
	Euc2D,
	Euc3D,
	Geo
}

pub enum Node {
	Node2D { num: i32, x: f64, y: f64 },
	Node3D { num: i32, x: f64, y: f64, z: f64 },
	NodeGeo { num: i32, lat: f64, lon: f64, x: f64, y: f64 }
}

pub struct TSPFile {
	pub edge_weight_type: EdgeWeightTypes, 
	pub nodes: Vec<Node>,
	pub tours: Vec<Vec<i32>>
}

pub type TSPFileResult = Result<TSPFile, io::Error>;

#[derive(PartialEq)]
enum ParserState {
	Specification,
	Data,
	Nodes,
	Tours
}

pub fn dist_euc2d (n1: &Node, n2: &Node) -> i32 {
	if let &Node::Node2D{x: x1, y: y1, ..} = n1 {
		if let &Node::Node2D{x: x2, y: y2, ..} = n2 {
			return ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)).sqrt().round() as i32;
		}
	}
	panic!("Invalid");
}

pub fn dist_euc3d (n1: &Node, n2: &Node) -> i32 {
	if let &Node::Node3D{x: x1, y: y1, z: z1, ..} = n1 {
		if let &Node::Node3D{x: x2, y: y2, z: z2, ..} = n2 {
			return ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2)).sqrt().round() as i32;
		}
	}
	panic!("Invalid");
}

pub fn dist_geo (n1: &Node, n2: &Node) -> i32 {
	let rrr = 6378.388;
	if let &Node::NodeGeo{lat: lat1, lon: lon1, ..} = n1 {
		if let &Node::NodeGeo{lat: lat2, lon: lon2, ..} = n2 {
			let q1 = (lon1 - lon2).cos();
			let q2 = (lat1 - lat2).cos();
			let q3 = (lat1 + lat2).cos();

			return (rrr * (0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)).acos() + 1.0) as i32;
		}
	}
	panic!("Invalid");
}

pub fn calculate_length (prob: &TSPFile, tour: &Vec<i32>) -> i32 {
	let dist: fn(&Node, &Node) -> i32 = match prob.edge_weight_type {
		EdgeWeightTypes::Euc2D => dist_euc2d,
		EdgeWeightTypes::Euc3D => dist_euc3d,
		EdgeWeightTypes::Geo => dist_geo,
	};
	let len = tour.len();
	let mut d: i32 = 0;
	for i in 0..len {
		let node = &prob.nodes[(tour[i] as usize) - 1];
		let next_node = &prob.nodes[(tour[(i + 1) % len] as usize) - 1];
		d = d + dist(&node, &next_node);
	}
	d
}

pub fn make_geo_node (num: i32, x: f64, y: f64) -> Node {
	let pi = 3.141592;
	let deg = (x as i32) as f64;
	let minutes = x - deg;
	let lat = pi * (deg + 5.0 * minutes / 3.0) / 180.0;
	let deg = (y as i32) as f64;
	let minutes = y - deg;
	let lon = pi * (deg + 5.0 * minutes / 3.0) / 180.0;
	Node::NodeGeo {
		num: num, x: x, y: y, lat: lat, lon: lon
	}
}

pub fn parse_file (path: &Path) -> TSPFileResult {
	let f = try!(File::open(&path));
	let reader = BufReader::new(f);
	let mut result = TSPFile{ 
		edge_weight_type: EdgeWeightTypes::Euc2D, 
		nodes: vec![],
		tours: vec![]
	};

	// read a line into buffer
	let mut parser_state = ParserState::Specification;
	for line in reader.lines().filter_map(|result| result.ok()) {
		if line.len() == 0 {
			continue;
		}
		if line.trim() == "EOF" {
			break;
		}

		if parser_state == ParserState::Specification {
			if line.contains(":") {
				let res: Vec<&str> = line.split(":").collect();
				let key = res[0].trim();
				let val = res[1].trim();
				if key == "EDGE_WEIGHT_TYPE" {
					result.edge_weight_type = match val {
						"GEO" => EdgeWeightTypes::Geo,
						"EUC_2D" => EdgeWeightTypes::Euc2D,
						"EUC_3D" => EdgeWeightTypes::Euc3D,
						_ => panic!("Unsupported edge weight type")
					}
				}
				continue;
			} else {
				parser_state = ParserState::Data;
			}
		}

		if line.chars().next().expect("Invalid line").is_alphabetic() {
			if line == "NODE_COORD_SECTION"	{
				parser_state = ParserState::Nodes;
			} else if line == "TOUR_SECTION" {
				parser_state = ParserState::Tours;
			} else {
				panic!("Data section '{}' is not supported.", line);
			}
		} else if parser_state == ParserState::Nodes {
			let parts: Vec<&str> = line.trim().split(" ").collect();
			if result.edge_weight_type == EdgeWeightTypes::Euc3D {
				result.nodes.push(Node::Node3D{
					num: parts[0].trim().parse::<i32>().unwrap(),
					x: parts[1].trim().parse::<f64>().unwrap(),
					y: parts[2].trim().parse::<f64>().unwrap(),
					z: parts[3].trim().parse::<f64>().unwrap(),
				});
			} else if result.edge_weight_type == EdgeWeightTypes::Euc2D {
				result.nodes.push(Node::Node2D{
					num: parts[0].trim().parse::<i32>().unwrap(),
					x: parts[1].trim().parse::<f64>().unwrap(),
					y: parts[2].trim().parse::<f64>().unwrap(),
				});
			} else if parts.len() == 3 {
				result.nodes.push(make_geo_node(
					parts[0].trim().parse::<i32>().unwrap(),
					parts[1].trim().parse::<f64>().unwrap(),
					parts[2].trim().parse::<f64>().unwrap()
				));
			} else {
				panic!("Unknown type of coordinates");
			}
		} else if parser_state == ParserState::Tours {
			let node = line.trim().parse::<i32>().unwrap();
			if node == -1 || result.tours.is_empty() {
				result.tours.push(vec![]);
			}
			if node != -1 {
				let index = result.tours.len() - 1;
				result.tours[index].push(node);
			}
		} else {
			panic!("Invalid parser state");
		}
	}

	// Cleanup
	if !result.tours.is_empty() && result.tours[result.tours.len() - 1].is_empty() {
		result.tours.pop();
	}

	Ok(result)
}
