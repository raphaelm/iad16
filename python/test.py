from tsplib import TspFile

with open('data/gr96.tsp') as f:
    prob = TspFile.create_from_file(f)
with open('data/gr96.opt.tour') as f:
    tour = TspFile.create_from_file(f)

print(prob.length(tour.tours[0]))

