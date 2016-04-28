use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
use std::path::Path;

pub enum EdgeWeightTypes {
	Explicit,
	Euc2D,
	Euc3D,
	Geo
}

pub struct Node {
	num: i32,
	x: i32,
	y: i32
}

pub struct TSPFile {
	pub edge_weight_type: EdgeWeightTypes, 
	pub nodes: Vec<Node>
}

pub type TSPFileResult = Result<TSPFile, io::Error>;

pub fn parse_file (path: &Path) -> TSPFileResult {
	let f = try!(File::open(&path));
	let mut reader = BufReader::new(f);
	let mut buffer = String::new();
	let result = TSPFile{ edge_weight_type: EdgeWeightTypes::Euc2D, nodes: vec![] };

	// read a line into buffer
	try!(reader.read_line(&mut buffer));

	println!("{}", buffer);
	Ok(result)
}
