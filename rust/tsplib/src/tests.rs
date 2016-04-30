use super::*;

#[test]
fn test_latlong_conv() {
	let pi: f64 = 3.141592;
	let node = make_geo_node(1, 360.0, 90.0);
    match node {
        Node::NodeGeo { lat, lon, .. } => assert!(lat == 2.0 * pi && lon == pi / 2.0),
		_ => panic!("Invalid node returned")
    };
}
