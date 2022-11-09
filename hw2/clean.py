graph = {
    'Oradea' : {
        'Zerind' : 71,
        'Sibiu' : 151
    },
    'Sibiu' : {
        'Oradea' : 151,
        'Arad' : 140,
        'Fagaras': 99,
        'Rimnicu Vilcea': 80
    },
    'Urziceni' : {
        'Bucharest': 85,
        'Hirsova': 98,
        'Vaslui': 142
    },
    'Vaslui': {
        'Urziceni': 142,
        'Iasi': 92
    },
    'Iasi': {
        'Vaslui': 92,
        'Neamt': 87
    },
    'Neamt': {
        'Iasi': 87
    },
    'Hirsova': {
        'Eforie' : 86,
        'Urziceni' : 98
    },
    'Eforie' : {
        'Hirsova': 86
    },
    'Giurgiu': {
        'Bucharest' : 90
    },
    'Zerind' : {
        'Oradea' : 71,
        'Arad': 75
    },
    'Arad' : {
        'Sibiu': 140,
        'Timisoara': 118,
        'Zerind' : 75
    },
    'Timisoara': {
        'Lugoj': 111,
        
        'Arad': 118
    },
    'Lugoj' : {
        'Timisoara': 111,
        'Mehadia': 70
    },
    'Mehadia' : {
        'Lugoj': 70,
        'Drobeta': 75
    },
    'Drobeta' : {
        'Mehadia': 75,
        'Craiova': 120
    },
    'Craiova' : {
        'Drobeta' : 120,
        'Rimnicu Vilcea' : 146,
        'Pitesti' : 138  
    },
    'Pitesti' : {
        'Craiova' : 138,
        'Rimnicu Vilcea' : 97,
        'Bucharest' : 101
    },
    'Rimnicu Vilcea' : {
        'Sibiu' : 80,
        'Craiova' : 146,
        'Pitesti': 97
    },
    'Fagaras' : {
        'Sibiu' : 99,
        'Bucharest' : 211
    },
    'Bucharest' : {
        'Giurgiu' : 90,
        'Fagaras' : 211,
        'Pitesti' : 101,
        'Urziceni' : 85
    }
}

heuristics = {}
heuristics['Arad'] = 366
heuristics['Bucharest'] = 0
heuristics['Craiova'] = 160
heuristics['Drobeta'] = 242
heuristics['Eforie'] = 161
heuristics['Fagaras'] = 176
heuristics['Giurgiu'] = 77
heuristics['Hirsova'] = 151
heuristics['Iasi'] = 226
heuristics['Lugoj'] = 244
heuristics['Mehadia'] = 241
heuristics['Neamt'] = 234
heuristics['Oradea'] = 380
heuristics['Pitesti'] = 100
heuristics['Rimnicu Vilcea'] = 193
heuristics['Sibiu'] = 253
heuristics['Timisoara'] = 329
heuristics['Urziceni'] = 80
heuristics['Vaslui'] = 199
heuristics['Zerind'] = 374

def computeGCost(graph, path):
    cost=0
    # while len(path) > 1:
    for i in range(len(path)-1):
        curr_node = path[i]
        next_node = path[i+1]
        cost = cost + graph[curr_node][next_node]
    return cost

def AStar(graph, heuristics, start, end):
    if start not in graph:
        return {'path' : [], 'total_cost' : 0}
    all_paths = []
    path = []
    curr_node = start
    path.append(curr_node)
    while curr_node != end:
        for node in graph[curr_node].items():
            new_path = list(path)
            new_path.append(node[0])
            path_and_cost = {}
            path_and_cost['path'] = new_path
            path_and_cost['f_cost'] = computeGCost(graph, new_path) + heuristics[node[0]]
            all_paths.append(path_and_cost)
        all_paths.sort(key=lambda element: element['f_cost'])
        print(len(all_paths))
        curr_node = all_paths[0]['path'][-1]
        path = all_paths[0]['path']
        del all_paths[0]
    final_path = path.copy()
    return {'path': path, 'total_cost': computeGCost(graph, path)}
        

ans = AStar(graph, heuristics, 'Arad', 'Bucharest')
print(ans)
ans = AStar(graph, heuristics, 'Bucharest', 'Bucharest')
print(ans)
ans = AStar(graph, heuristics, 'Pitesti', 'Bucharest')
print(ans)
ans = AStar(graph, heuristics, 'None', 'Bucharest')
print(ans)
