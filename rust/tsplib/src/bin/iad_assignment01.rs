extern crate tsplib;
extern crate rand;

use std::path::Path;
use std::env;
use rand::Rng;
use rand::thread_rng;
use tsplib::parse_file;
use tsplib::tour_length;

fn make_random_tour(n_nodes: i32) -> Vec<i32> {
	let mut nodes = (1..(n_nodes + 1)).collect::<Vec<i32>>();
	thread_rng().shuffle(&mut nodes);
	nodes
}

fn main() {
    let args: Vec<String> = env::args().collect();
	let path = Path::new(&args[1]);
	let tspf = parse_file(path).unwrap();
	let mut lens = vec![];
	for i in 0..1000000 {
		let tour = make_random_tour(tspf.nodes.len() as i32);
		lens.push(tour_length(&tspf, &tour));
	}
	println!("Hello world");
}
