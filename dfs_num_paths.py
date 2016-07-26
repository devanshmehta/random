# Input first line contains number of flights
# Second line onwards contains aiport - airport
# eg: 3
#     JFK SFO
#     JFK ATL
#     ATL SFO
# Number of flights between JFK and SFO is 2 
# JFK-SFO and JFK->ATL->SFO

airports = {}
num_flights = int(raw_input())
for i in xrange(num_flights):
    src , des = raw_input().split(' ')
    if src in airports:
        airports[src].append(des)
    else:
        airports[src] = [des]

def get_num_paths(src, dest, airports, visited):
    '''gets the number of paths between source and destination'''
    if src == dest:
        # we have reached
        return 1
    num_paths = 0
    next_nodes = airports[src]
    for next_node in next_nodes:
        if next_node in visited:
            continue
        visited.add(next_node)
        num_paths += get_num_paths(next_node, dest, airports, visited)
        visited.remove(next_node)
    return num_paths

def get_routes(src, dest, airports, visited):
    '''gets all the routes between source and destination. Returns 
       an empty list if none exist'''
    if src == dest:
        # we have reached destination
        return [[dest]]
    routes_from_src = []
    next_nodes = airports[src]
    for next_node in next_nodes:
        if next_node in visited:
            continue
        visited.add(next_node)
        routes = get_routes(next_node, dest, airports, visited)
        if routes:
           for route in routes:
               route.append(src)
               routes_from_src.append(route)
        visited.remove(next_node)
    return routes_from_src

print get_num_paths('JFK', 'SFO', airports, set(["JFK"]))
routes = get_routes('JFK', 'SFO', airports, set(["JFK"]))
for route in routes:
    for i in reversed(route):
        print i, 
    print 
