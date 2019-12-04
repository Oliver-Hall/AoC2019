# Advent of Code Day 3

with open('day3.txt') as f:
    routes = f.read()
path1, path2 = routes.strip().split('\n')

#create dictionary with co-ord changes for each direction
deltas = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def plot_points(directions):
	# initialise
    steps, x, y = 0, 0, 0
    points = set()
	# dictionary to keep track of steps for part 2
    step_counts = {}
	# loop through each direction
    for dir in directions.split(','):
		# get the direction and magnitude of each direction
        direction, magnitude = dir[:1], int(dir[1:])
		# get the change in x and y from from dictionary
        dx, dy = deltas[direction]
		# loop for enought times to hit every point along the line
        for point in range(magnitude):
			# move use along the line (one of these will be zero)
            x += dx
            y += dy
            steps += 1
			# add the co-ords to the points set
            points.add((x, y))
			# create a dictionary key of co-ord and steps to that point 
			# (if it doesn't already exist in steps dictionary.
            step_counts.setdefault((x, y), steps)

    return points, step_counts

# create points for first and second paths
p1_points, p1_steps = plot_points(path1)
p2_points, p2_steps = plot_points(path2)

# use intersection to find common points
intersections = p1_points & p2_points

# work out manhatten distance for part 1
print(min(abs(x) + abs(y) for x, y in intersections))

# work out minimum steps for each intersection for part 2
print(min(p1_steps[point] + p2_steps[point] for point in intersections))
