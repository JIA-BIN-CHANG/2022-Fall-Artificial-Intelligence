from random import vonmisesvariate
import unittest

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
    while len(path) > 1:
        curr_node = path[0]
        next_node = path[1]
        # if next_node not in list(graph[curr_node].keys()):
        #     path.remove(next_node)
        #     continue
        cost = cost + graph[curr_node][next_node]
        del path[0]
    return cost

# path = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti']
# print(computeGCost(graph, path))


def AStar(graph, heuristics, start, end, total_cost= 0, queue=[], visited=[]):
    # print(queue)
    if start not in visited:
        visited.append(start)
    print(f'visited:{visited}')
    
    if start == end:
        path = {}
        path['path'] = visited
        path['total_cost'] = total_cost
        return path
    
    # check if start is in the graph
    # return none if not found
    if start not in graph:
        path = {}
        path['path'] = []
        path['total_cost'] = total_cost
        return path
    
    # add the child nodes into the queue
    print(f'currect start: {start}')
    print(f'total cost: {total_cost}')
    for node in graph[start].items():
        cost_path=[]
        cost_path = visited.copy()
        cost_path.append(node[0])
        print(cost_path)
        # build a node for the queue
        queue_node = {}
        queue_node['name'] = node[0]
        queue_node['f_cost'] = heuristics[node[0]] + computeGCost(graph, cost_path)
        queue_node['heuristic'] = heuristics[node[0]]
        queue_node['cost'] = node[1]
        # queue_node['cost'] = node[1]
        queue.append(queue_node)
    
    # queue is maintained in nondecreasing order of the SLD, f(n) = g(n) + h(n)
    # f(n) is the estimated cost of the cheapest solution through n
    # g(n) is the actual cost to reach n
    # h(n) is the heuristic
    # queue.sort(key = f(n) cost)
    queue.sort(key=lambda element: element['f_cost'])
    print(queue)
    print('\n')
    
    # return None if nothing was added to the queue
    if not queue:
        return []
    else:
        next_node = queue[0]
        print(f'next: {next_node}')
        if next_node['name'] in list(graph[start].keys()):
            total_cost = total_cost + next_node['cost']
            print(total_cost)
        else:
            while next_node['name'] not in list(graph[visited[-1]].keys()):
                print('pop one')
                visited.pop(-1)
        del queue[0]
        return AStar(graph, heuristics, next_node['name'], end, total_cost, queue, visited)


result = AStar(graph, heuristics, 'Arad', 'Bucharest',queue=[],visited=[])
print(result)

# def AStar(graph, heuristics, start, end):
#     path = []
#     total_cost = 0
#     if start not in graph:
#         result = {}
#         result['path'] = path
#         result['total_cost'] = total_cost
#         return result
#     curr_node = start
#     path.append(curr_node)
    
#     while (curr_node is not end):
#         temp_cost = 9999
#         for node in graph[curr_node].items():
#             if heuristics[node[0]] + node[1] < temp_cost:
#                 temp_cost = heuristics[node[0]] + node[1]
#                 curr_node = node[0]
#                 curr_cost = node[1]
#         path.append(curr_node)
#         total_cost = total_cost + curr_cost
    
#     result = {}
#     result['path'] = path
#     result['total_cost'] = total_cost
#     return result

# class SearchingTest(unittest.TestCase):
#     def test_01(self):
#         print("TestCase01")
#         print("Arad -> Bucharest")

#         path = AStar(graph, heuristics, 'Arad', 'Bucharest',queue=[],visited=[])
#         self.assertEqual(['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'], path['path'])
#         self.assertEqual(418, path['total_cost'])
    
#     def test_02(self):
#         print("TestCase02")
#         print("Pitesti -> Bucharest")

#         path = AStar(graph, heuristics, 'Pitesti', 'Bucharest',queue=[],visited=[])
#         self.assertEqual(['Pitesti', 'Bucharest'], path['path'])
#         self.assertEqual(101, path['total_cost'])

#     def test_03(self):
#         print("TestCase03")
#         print("Bucharest -> Bucharest")

#         path = AStar(graph, heuristics, 'Bucharest', 'Bucharest',queue=[],visited=[])
#         self.assertEqual(['Bucharest'], path['path'])
#         self.assertEqual(0, path['total_cost'])

#     def test_04(self):
#         print("TestCase04")
#         print("None -> Bucharest")

#         path = AStar(graph, heuristics, 'None', 'Bucharest',queue=[],visited=[])
#         self.assertEqual([], path['path'])
#         self.assertEqual(0, path['total_cost'])

# if __name__ == '__main__':
#     unittest.main()
