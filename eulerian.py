from copy import copy

'''

	is_connected - Checks if a graph in the form of a dictionary is 
	connected or not, using Breadth-First Search Algorithm (BFS)

'''

def is_connected(G):
	start_node = list(G)[0]
	color = {v: 'white' for v in G}
	color[start_node] = 'gray'
	S = [start_node]
	while len(S) != 0:
		u = S.pop()
		for v in G[u]:
			if color[v] == 'white':
				color[v] = 'gray'
				S.append(v)
			color[u] = 'black'
	return list(color.values()).count('black') == len(G)

'''
	odd_degree_nodes - returns a list of all G odd degrees nodes
'''
def odd_degree_nodes(G):
	odd_degree_nodes = []
	for u in G:
		if len(G[u]) % 2 != 0:
			odd_degree_nodes.append(u)
	return odd_degree_nodes

'''
	from_dict - return a list of links in the form tuples from a graph in a 
	dictionary format
'''	
def from_dict(G):
	links = []
	for u in G:
		for v in G[u]:
			links.append((u,v))
	return links

'''
	fleury(G) - return eulerian trail from graph G or a string 'Not Eulerian Graph' if is not possible
'''
def fleury(G):
	'''
		checks if G has eulerian cycle or trail
	'''
	odn = odd_degree_nodes(G)
	if len(odn) > 2 or len(odn) == 1:
		return 'Not Eulerian Graph'
	else:
		g = copy(G)
		trail = []
		if len(odn) == 2:
			u = odn[0]
		else:
			u = list(g)[0]
		while len(from_dict(g)) > 0:
			current_vertex = u
			for u in g[current_vertex]:
				g[current_vertex].remove(u)
				g[u].remove(current_vertex)
				bridge = not is_connected(g)
				if bridge:
					g[current_vertex].append(u)
					g[u].append(current_vertex)
				else:
					break
			if bridge:
				g[current_vertex].remove(u)
				g[u].remove(current_vertex)
				g.pop(current_vertex)
			trail.append((current_vertex, u))
	return trail

# testing 7 bridges of konigsberg
print('Konigsberg')
G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
print(fleury(G))

# testing a eulerian cycle
print('1st Eulerian Cycle')
G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
print(fleury(G))

# testing another eulerian cycle
print('2nd Eulerian Cycle')
G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
print(fleury(G))

# testing a eulerian trail
print('Eulerian Trail')
G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
print(fleury(G))

