extern crate tsplib;

use tsplib::EdgeWeightTypes;
use tsplib::parse_file;
use std::path::Path;

#[test]
fn test_parse_gr96() {
	let path = Path::new("../../data/gr96.tsp");
	let res = parse_file(path);
	assert!(res.is_ok());
	let tspf = res.unwrap();
	assert!(tspf.edge_weight_type == EdgeWeightTypes::Geo);
	assert!(tspf.nodes.len() == 96);
}

#[test]
fn test_parse_gr96_tour() {
	let path = Path::new("../../data/gr96.opt.tour");
	let res = parse_file(path);
	assert!(res.is_ok());
	let tspf = res.unwrap();
	assert!(tspf.tours.len() == 1);
	assert!(tspf.tours[0].len() == 96);
}

#[test]
fn test_parse_pcb442() {
	let path = Path::new("../../data/pcb442.tsp");
	let res = parse_file(path);
	assert!(res.is_ok());
	let tspf = res.unwrap();
	assert!(tspf.edge_weight_type == EdgeWeightTypes::Euc2D);
	assert!(tspf.nodes.len() == 442);
}

#[test]
fn test_parse_pcb442_tour() {
	let path = Path::new("../../data/pcb442.opt.tour");
	let res = parse_file(path);
	assert!(res.is_ok());
	let tspf = res.unwrap();
	assert!(tspf.tours.len() == 1);
	assert!(tspf.tours[0].len() == 442);
}