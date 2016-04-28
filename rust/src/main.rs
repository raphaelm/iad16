mod tsplib;
use std::path::Path;

#[test]
fn test_parse_gr96() {
	let path = Path::new("../data/gr96.tsp");
	let res = tsplib::parse_file(path);
	assert!(res.is_ok());
	let tspf = res.unwrap();
	assert!(tspf.nodes.len() == 96);
}

fn main() {
    println!("Hello, world!");
}
