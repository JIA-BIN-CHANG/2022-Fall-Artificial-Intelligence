# Dieudonne Muhirwa M14185704
# Allen Detmer M15216736
# JiaBin Chang M13782945
# Joseph Matawaran M15228497

# Libraries Included:
import unittest
import time
from collections import deque

# graph - Dictionary of Dictionary
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
    
    
} # end graph

# heuristics - Dictionary
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

# Depth First Search algorithm expand deepest the unexpanded node
# return path from start to destination node i.e., end if the path exist
# return empty path found if the path does not exist
# DFS takes 3 parameter(graph, start, end)
# return the result of each search has a dictionary object that contains the result and stats about the run for Efficiency comparison 
# Key 'path' is a list of shortest path; empty path if no path is found
# Key 'visited' which is a list of all visited cities including the destination to find the end
# Key 'numVisited' is the total number of the visited cities including the destination
def DepthFirst(graph,start,end):
    
    # handle condition where start element is not in the graph
    if start not in graph:
        return {'path': [], 'visited': [], 'numVisited': 0}
    
    # init the visited and numVisted
    visited=[]
    numVisited = 0
        
    stack=deque()
    visited.append(start)
    stack.append(visited)
    
    while stack:
        #LIFO imprementation
        path=stack[-1]
        visited=stack.pop()
        last_visited=visited[-1]
        
        # count the number of elements visited
        numVisited = numVisited + 1
        
        # is this the end element
        if last_visited==end:
            return {'path': path, 'visited': visited, 'numVisited': numVisited}
        
        for current_neighbor in graph[last_visited]:
            if current_neighbor not in visited:
                new_path = []
                new_path = visited + [current_neighbor]
                stack.append(new_path)

    return {'path': [], 'visited': [], 'numVisited': 0}

# Breadth-first search finds shortest paths from a given starting city to the end city
# In terms of the number of edges in the paths
# Param graph - The graph that shows the connections
# start - the starting city
# end - the end city
# return the result of each search has a dictionary object that contains the result and stats about the run for Efficiency comparison 
# Key 'path' which is a list of shortest path; empty path if no path is found
# Key 'visited' which is a list of all visited cities including the destination to find the end
# Key 'numVisited' which is the total number of the visited cities including the destination
def BreadthFirst(graph, start, end):
    visited = []
    queue = [[start]]

    while queue:

        # gets first path in the queue and the last node in the path
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            visited.append(end)
            return {'path': path, 'visited': visited, 'numVisited': len(visited)}

        # check if the current node has already visited
        elif node not in visited:

            # list all the neighbor nodes
            # construct new path and put it into the queue
            for current_neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(current_neighbor)
                queue.append(new_path)

            # identify the visited city
            visited.append(node)
    # return None if nothing was added to the queue
    return {'path': [], 'visited': [], 'numVisited': 0}

# Best-first search implements the Best-first map/graph search algorithm
# Using a priority queue and heuristic search
# Param graph - The graph that shows the connections and their costs
# heuristics - list of heuristic values to the target
# start - the starting city
# end - the end city
# total_cost - optional param for the starting cost
# queue - optinoal param for the started queue in order
# visited - optional param for the list of visited cities
# return the result of each search has a dictionary object that contains the result and stats about the run for Efficiency comparison 
# Key 'path' is a list of shortest path; empty path if no path is found
# Key 'total_cost' is the total cost of the shortest path
# Key 'numVisited'  is the total number of the visited cities including the destination
def BestFirst(graph, heuristics, start, end, total_cost= 0, queue=[], visited=[]):
    if start not in visited:
        visited.append(start)
    
    if start == end:
        path = {}
        path['path'] = visited
        path['total_cost'] = total_cost
        path['numVisited'] = len(visited)
        return path
    
    # check if start is in the graph
    # return empty path if the element is not found in the graph
    if start not in graph:
        path = {}
        path['path'] = []
        path['total_cost'] = total_cost
        path['numVisited'] = 0
        return path
    
    # add the child nodes into the queue
    for node in graph[start].items():
        if node[0] not in visited:
            # build a node for the queue
            queue_node = {}
            queue_node['name'] = node[0]
            queue_node['heuristic'] = heuristics[node[0]]
            queue_node['cost'] = node[1]
            queue.append(queue_node)
    
    # queue is maintained in nondecreasing order of the SLD, h(n)
    # h(n) is the heuristic
    # queue.sort(key=getHeuristic)
    queue.sort(key=lambda element: element['heuristic'])
    
    # return empty path if nothing was added to the queue
    # test for element that has no nodes
    if not queue:
        path = {}
        path['path'] = []
        path['total_cost'] = total_cost
        path['numVisited'] = len(visited)
        return path
    else:
        curr_node = queue[0]
        total_cost = total_cost + curr_node['cost']
        del queue[0]
        return BestFirst(graph, heuristics, curr_node['name'], end, total_cost, queue, visited)

# A* search implements the A* map/graph search algorithm
# Param graph - The graph that shows the connections and their costs
# path - The start and end subpath; empty path if no path is found
# Returns the actual g cost from start node to end node
def computeGCost(graph, path):
    cost=0
    for i in range(len(path)-1):
        curr_node = path[i]
        next_node = path[i+1]
        cost = cost + graph[curr_node][next_node]
    return cost

# Param graph - The graph that shows the connections and their costs
# heuristics - list of heuristic values to the target
# start - the starting city
# end - the end city
# return the result of each search has a dictionary object that contains the result and stats about the run for Efficiency comparison 
# Key 'path' is a list of shortest path 
# Key 'total_cost' is the total cost of the shortest path
# Key 'numVisited' is the total number of the visited cities including the destination
def AStar(graph, heuristics, start, end):
    # check if start is in the graph
    # return empty path if the element is not found in the graph
    if start not in graph:
        return {'path' : [], 'total_cost' : 0, 'numVisited' : 0}
    all_paths = []
    path = []
    visited = []
    curr_node = start
    path.append(curr_node)
    visited.append(curr_node)
    while curr_node != end:
        for node in graph[curr_node].items():
            #new path is the expanding path from node A to all the connecting nodes
            new_path = list(path)
            new_path.append(node[0])
            
            # f(n) is the estimated cost of the cheapest solution through n
            # g(n) is the actual cost to reach n
            # h(n) is the heuristic
            path_and_cost = {}
            path_and_cost['path'] = new_path
            path_and_cost['f_cost'] = computeGCost(graph, new_path) + heuristics[node[0]]
            all_paths.append(path_and_cost)
        # all_paths contains all the current path and it's f(n) cost
        # all_paths.sort(key = f(n) cost)
        all_paths.sort(key=lambda element: element['f_cost'])
        curr_node = all_paths[0]['path'][-1]
        path = all_paths[0]['path']
        for city in path:
            if city not in visited:
                visited.append(city)
        del all_paths[0]
    return {'path': path, 'total_cost': computeGCost(graph, path), 'numVisited' : len(visited)}

# This function computes the searching time of different algorithms
# Param searchAlgorithm - the algorithm used in searching
# Param graph - The graph that shows the connections and their costs
# heuristics - list of heuristic values to the target
# start - the starting city
# end - the end city
# Returns the result dictionary of each algorithm
def computeTime(searchAlgorithm, graph, heuristics, start, end):
    if searchAlgorithm == "DepthFirst":
        t1 = time.process_time_ns()
        result = DepthFirst(graph,start,end)
        t2 = time.process_time_ns()
        print(f'{searchAlgorithm} execution time: {t2-t1} ns')
    elif searchAlgorithm == "BreadthFirst":
        t1 = time.process_time_ns()
        result = BreadthFirst(graph, start, end)
        t2 = time.process_time_ns()
        print(f'{searchAlgorithm} execution time: {t2-t1} ns')
    elif searchAlgorithm == "BestFirst":
        t1 = time.process_time_ns()
        result = BestFirst(graph, heuristics, start, end, total_cost= 0, queue=[], visited=[])
        t2 = time.process_time_ns()
        print(f'{searchAlgorithm} execution time: {t2-t1} ns')
    elif searchAlgorithm == "AStar":
        t1 = time.process_time_ns()
        result = AStar(graph, heuristics, start, end)
        t2 = time.process_time_ns()
        print(f'{searchAlgorithm} execution time: {t2-t1} ns')
    else:
        print("Input value for search algorithm is not valid returninng None")
        return None
    return result

'''
Test case design
Based on ISP(Input Space Partitioning) and ECC(Each Choice Coverage)

1.  BreadthFirst test path from Arad to Bucharest
2.  BreadthFirst test path from Bucharest to Bucharest
3.  BreadthFirst test path from Pitesti to Bucharest
4.  BreadthFirst test path from None to Bucharest
5.  DepthFirst test path from Arad to Bucharest
6.  DepthFirst test path from Bucharest to Bucharest
7.  DepthFirst test path from Pitesti to Bucharest
8.  DepthFirst test path from None to Bucharest
9.  BestFirst test path from Arad to Bucharest
10. BestFirst test path from Bucharest to Bucharest
11. BestFirst test path from Pitesti to Bucharest
12. BestFirst test path from None to Bucharest
13. AStar test path from Arad to Bucharest
14. AStar test path from Bucharest to Bucharest
15. AStar test path from Pitesti to Bucharest
16. AStar test path from None to Bucharest
17. Comparsion of all algorithms from Arad to Bucharest
18. Comparsion of all algorithms from Sibiu to Bucharest
19. Comparsion of all algorithms from Oradea to Bucharest
'''

class SearchingTest(unittest.TestCase):
    def test_01(self):
        print("TestCase01 - BreadthFirst test path from Arad to Bucharest")
        print("Arad -> Bucharest")
        path = computeTime("BreadthFirst", graph, heuristics, 'Arad', 'Bucharest')
        self.assertEqual(['Arad', 'Sibiu', 'Fagaras', 'Bucharest'], path['path'])
        self.assertEqual(['Arad', 'Sibiu', 'Timisoara', 'Zerind', 'Oradea', 'Fagaras', 'Rimnicu Vilcea', 'Lugoj', 'Bucharest'], path['visited'])
        self.assertEqual(9, path['numVisited'])
    def test_02(self):
        print("\nTestCase02 - BreadthFirst test path from Bucharest to Bucharest")
        print("Bucharest -> Bucharest")
        path = computeTime("BreadthFirst", graph, heuristics, 'Bucharest', 'Bucharest')
        self.assertEqual(['Bucharest'], path['path'])
        self.assertEqual(['Bucharest'], path['visited'])
        self.assertEqual(1, path['numVisited'])
    def test_03(self):
        print("\nTestCase03 - BreadthFirst test path from Pitesti to Bucharest")
        print("Pitesti -> Bucharest")
        path = computeTime("BreadthFirst", graph, heuristics, 'Pitesti', 'Bucharest')
        self.assertEqual(['Pitesti', 'Bucharest'], path['path'])
        self.assertEqual(['Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Bucharest'], path['visited'])
        self.assertEqual(4, path['numVisited'])
    def test_04(self):
        print("\nTestCase04 - BreadthFirst test path from None to Bucharest")
        print("None -> Bucharest")
        path = computeTime("BreadthFirst", graph, heuristics, 'None', 'Bucharest')
        self.assertEqual([], path['path'])
        self.assertEqual([], path['visited'])
        self.assertEqual(0, path['numVisited'])
        
    def test_05(self):
        print("\nTestCase05 - DepthFirst test path from Arad to Bucharest")
        print("Arad -> Bucharest")
        path = computeTime("DepthFirst",graph,heuristics,'Arad','Bucharest')
        self.assertEqual(['Arad','Zerind','Oradea','Sibiu','Rimnicu Vilcea','Pitesti','Bucharest'], path['path'])
    
    def test_06(self):
        print("\nTestCase06 - DepthFirst test path from Bucharest to Bucharest.")
        print("Bucharest -> Bucharest")
        path = computeTime("DepthFirst",graph,heuristics,'Bucharest','Bucharest')
        self.assertEqual(['Bucharest'], path['path'])
        
    def test_07(self):   
        print("\nTestCase07 - DepthFirst test path from Pitesti to Bucharest.")
        print("Pitesti -> Bucharest")
        path = computeTime("DepthFirst",graph,heuristics,'Pitesti','Bucharest')
        self.assertEqual(['Pitesti','Bucharest'], path['path'])  
        
    def test_08(self):
        print("\nTestCase08 - DepthFirst test path from None to Bucharest")
        print("None -> Bucharest")
        path = computeTime("DepthFirst",graph,heuristics,'None','Bucharest')
        self.assertEqual([], path['path'])
              
    def test_09(self):
        print("\nTestCase09 - BestFirst test path from Arad to Bucharest")
        print("Arad -> Bucharest")
        path = computeTime("BestFirst", graph, heuristics, 'Arad', 'Bucharest')
        self.assertEqual(['Arad', 'Sibiu', 'Fagaras', 'Bucharest'], path['path'])
        self.assertEqual(450, path['total_cost'])
        self.assertEqual(4, path['numVisited'])
    
    def test_10(self):
        print("\nTestCase10 - BestFirst test path from Pitesti to Bucharest")
        print("Pitesti -> Bucharest")
        path = computeTime("BestFirst", graph, heuristics, 'Pitesti', 'Bucharest')
        self.assertEqual(['Pitesti', 'Bucharest'], path['path'])
        self.assertEqual(101, path['total_cost'])
        self.assertEqual(2, path['numVisited'])

    def test_11(self):
        print("\nTestCase11 - BestFirst test path from Bucharest to Bucharest")
        print("Bucharest -> Bucharest")
        path = computeTime("BestFirst", graph, heuristics, 'Bucharest', 'Bucharest')
        self.assertEqual(['Bucharest'], path['path'])
        self.assertEqual(0, path['total_cost'])
        self.assertEqual(1, path['numVisited'])
    
    def test_12(self):
        print("\nTestCase12 - BestFirst test path for a city None that is not found in the graph")
        print("None -> Bucharest")
        path = computeTime("BestFirst", graph, heuristics, 'None', 'Bucharest')
        self.assertEqual([], path['path'])
        self.assertEqual(0, path['total_cost'])
        self.assertEqual(0, path['numVisited'])
    
    def test_13(self):
        print("\nTestCase13 - AStar test path from Arad to Bucharest")
        print("Arad -> Bucharest")
        path = computeTime("AStar", graph, heuristics, 'Arad', 'Bucharest')
        self.assertEqual(['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'], path['path'])
        self.assertEqual(418, path['total_cost'])
        self.assertEqual(6, path['numVisited'])
    
    def test_14(self):
        print("\nTestCase14 - AStar test path from Pitesti to Bucharest")
        print("Pitesti -> Bucharest")
        path = computeTime("AStar", graph, heuristics, 'Pitesti', 'Bucharest')
        self.assertEqual(['Pitesti', 'Bucharest'], path['path'])
        self.assertEqual(101, path['total_cost'])
        self.assertEqual(2, path['numVisited'])

    def test_15(self):
        print("\nTestCase15 - AStar test path from Bucharest to Bucharest")
        print("Bucharest -> Bucharest")
        path = computeTime("AStar", graph, heuristics, 'Bucharest', 'Bucharest')
        self.assertEqual(['Bucharest'], path['path'])
        self.assertEqual(0, path['total_cost'])
        self.assertEqual(1, path['numVisited'])

    def test_16(self):
        print("\nTestCase16 - AStar test path for a city None that is not found in the graph")
        print("None -> Bucharest")
        path = computeTime("AStar", graph, heuristics, 'None', 'Bucharest')
        self.assertEqual([], path['path'])
        self.assertEqual(0, path['total_cost'])
        self.assertEqual(0, path['numVisited'])
    
    def test_17(self):
        print("\nTestCase17 - Comparision of all algorithms from Arad to Bucharest")
        print("Arad -> Bucharest")
        result_bfs = computeTime("BreadthFirst", graph, heuristics, 'Arad', 'Bucharest')
        path_bfs = result_bfs['path']
        num_bfs = result_bfs['numVisited']
        print(f'Path of BreadthFirst: {path_bfs}')
        print(f'Number of city visited for BreadthFirst: {num_bfs}')
        print('\n')
        result_dfs = computeTime("DepthFirst", graph, heuristics, 'Arad', 'Bucharest')
        path_dfs = result_dfs['path']
        num_dfs = result_dfs['numVisited']
        print(f'Path of DepthFirst: {path_dfs}')
        print(f'Number of city visited for DepthFirst: {num_dfs}')
        print('\n')
        result_bf = computeTime("BestFirst", graph, heuristics, 'Arad', 'Bucharest')
        path_bf = result_bf['path']
        cost_bf = result_bf['total_cost']
        num_bf = result_bf['numVisited']
        print(f'Path of BestFirst: {path_bf}, cost: {cost_bf}')
        print(f'Number of city visited for BestFirst: {num_bf}')
        print('\n')
        result_as = computeTime("AStar", graph, heuristics, 'Arad', 'Bucharest')
        path_as = result_as['path']
        cost_as = result_as['total_cost']
        num_as = result_as['numVisited']
        print(f'Path of AStar: {path_as}, cost: {cost_as}')
        print(f'Number of city visited for AStar: {num_as}')
        
    def test_18(self):
        print("\nTestCase18 - Comparision of all algorithms from Sibiu to Bucharest")
        print("Sibiu -> Bucharest")
        result_bfs = computeTime("BreadthFirst", graph, heuristics, 'Sibiu', 'Bucharest')
        path_bfs = result_bfs['path']
        num_bfs = result_bfs['numVisited']
        print(f'Path of BreadthFirst: {path_bfs}')
        print(f'Number of city visited for BreadthFirst: {num_bfs}')
        print('\n')
        result_dfs = computeTime("DepthFirst", graph, heuristics, 'Sibiu', 'Bucharest')
        path_dfs = result_dfs['path']
        num_dfs = result_dfs['numVisited']
        print(f'Path of DepthFirst: {path_dfs}')
        print(f'Number of city visited for DepthFirst: {num_dfs}')
        print('\n')
        result_bf = computeTime("BestFirst", graph, heuristics, 'Sibiu', 'Bucharest')
        path_bf = result_bf['path']
        cost_bf = result_bf['total_cost']
        num_bf = result_bf['numVisited']
        print(f'Path of BestFirst: {path_bf}, cost: {cost_bf}')
        print(f'Number of city visited for BestFirst: {num_bf}')
        print('\n')
        result_as = computeTime("AStar", graph, heuristics, 'Sibiu', 'Bucharest')
        path_as = result_as['path']
        cost_as = result_as['total_cost']
        num_as = result_as['numVisited']
        print(f'Path of AStar: {path_as}, cost: {cost_as}')
        print(f'Number of city visited for AStar: {num_as}')
        
        
    def test_19(self):
        print("\nTestCase19 - Comparision of all algorithms from Oradea to Bucharest")
        print("Oradea -> Bucharest")
        result_bfs = computeTime("BreadthFirst", graph, heuristics, 'Oradea', 'Bucharest')
        path_bfs = result_bfs['path']
        num_bfs = result_bfs['numVisited']
        print(f'Path of BreadthFirst: {path_bfs}')
        print(f'Number of city visited for BreadthFirst: {num_bfs}')
        print('\n')
        result_dfs = computeTime("DepthFirst", graph, heuristics, 'Oradea', 'Bucharest')
        path_dfs = result_dfs['path']
        num_dfs = result_dfs['numVisited']
        print(f'Path of DepthFirst: {path_dfs}')
        print(f'Number of city visited for DepthFirst: {num_dfs}')
        print('\n')
        result_bf = computeTime("BestFirst", graph, heuristics, 'Oradea', 'Bucharest')
        path_bf = result_bf['path']
        cost_bf = result_bf['total_cost']
        num_bf = result_bf['numVisited']
        print(f'Path of BestFirst: {path_bf}, cost: {cost_bf}')
        print(f'Number of city visited for BestFirst: {num_bf}')
        print('\n')
        result_as = computeTime("AStar", graph, heuristics, 'Oradea', 'Bucharest')
        path_as = result_as['path']
        cost_as = result_as['total_cost']
        num_as = result_as['numVisited']
        print(f'Path of AStar: {path_as}, cost: {cost_as}')
        print(f'Number of city visited for AStar: {num_as}')
     
   
if __name__ == '__main__':
    unittest.main()

'''
Running result of the code

TestCase01 - BreadthFirst test path from Arad to Bucharest
Arad -> Bucharest
BreadthFirst execution time: 39835 ns
.
TestCase02 - BreadthFirst test path from Bucharest to Bucharest
Bucharest -> Bucharest
BreadthFirst execution time: 16036 ns
.
TestCase03 - BreadthFirst test path from Pitesti to Bucharest
Pitesti -> Bucharest
BreadthFirst execution time: 19436 ns
.
TestCase04 - BreadthFirst test path from None to Bucharest
None -> Bucharest
BreadthFirst execution time: 7215 ns
.
TestCase05 - DepthFirst test path from Arad to Bucharest
Arad -> Bucharest
DepthFirst execution time: 28453 ns
.
TestCase06 - DepthFirst test path from Bucharest to Bucharest.
Bucharest -> Bucharest
DepthFirst execution time: 7090 ns
.
TestCase07 - DepthFirst test path from Pitesti to Bucharest.
Pitesti -> Bucharest
DepthFirst execution time: 11539 ns
.
TestCase08 - DepthFirst test path from None to Bucharest
None -> Bucharest
DepthFirst execution time: 3152 ns
.
TestCase09 - BestFirst test path from Arad to Bucharest
Arad -> Bucharest
BestFirst execution time: 43160 ns
.
TestCase10 - BestFirst test path from Pitesti to Bucharest
Pitesti -> Bucharest
BestFirst execution time: 16225 ns
.
TestCase11 - BestFirst test path from Bucharest to Bucharest
Bucharest -> Bucharest
BestFirst execution time: 4947 ns
.
TestCase12 - BestFirst test path for a city None that is not found in the graph
None -> Bucharest
BestFirst execution time: 4844 ns
.
TestCase13 - AStar test path from Arad to Bucharest
Arad -> Bucharest
AStar execution time: 98369 ns
.
TestCase14 - AStar test path from Pitesti to Bucharest
Pitesti -> Bucharest
AStar execution time: 33982 ns
.
TestCase15 - AStar test path from Bucharest to Bucharest
Bucharest -> Bucharest
AStar execution time: 7907 ns
.
TestCase16 - AStar test path for a city None that is not found in the graph
None -> Bucharest
AStar execution time: 2962 ns
.
TestCase17 - Comparision of all algorithms from Arad to Bucharest
Arad -> Bucharest
BreadthFirst execution time: 36194 ns
Path of BreadthFirst: ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
Number of city visited for BreadthFirst: 9


DepthFirst execution time: 20653 ns
Path of DepthFirst: ['Arad', 'Zerind', 'Oradea', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
Number of city visited for DepthFirst: 7


BestFirst execution time: 30946 ns
Path of BestFirst: ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'], cost: 450
Number of city visited for BestFirst: 4


AStar execution time: 99803 ns
Path of AStar: ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'], cost: 418
Number of city visited for AStar: 6
.
TestCase18 - Comparision of all algorithms from Sibiu to Bucharest
Sibiu -> Bucharest
BreadthFirst execution time: 31411 ns
Path of BreadthFirst: ['Sibiu', 'Fagaras', 'Bucharest']
Number of city visited for BreadthFirst: 8


DepthFirst execution time: 15916 ns
Path of DepthFirst: ['Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
Number of city visited for DepthFirst: 4


BestFirst execution time: 36468 ns
Path of BestFirst: ['Sibiu', 'Fagaras', 'Bucharest'], cost: 310
Number of city visited for BestFirst: 3


AStar execution time: 65409 ns
Path of AStar: ['Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'], cost: 278
Number of city visited for AStar: 5
.
TestCase19 - Comparision of all algorithms from Oradea to Bucharest
Oradea -> Bucharest
BreadthFirst execution time: 32394 ns
Path of BreadthFirst: ['Oradea', 'Sibiu', 'Fagaras', 'Bucharest']
Number of city visited for BreadthFirst: 8


DepthFirst execution time: 17354 ns
Path of DepthFirst: ['Oradea', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
Number of city visited for DepthFirst: 5


BestFirst execution time: 40437 ns
Path of BestFirst: ['Oradea', 'Sibiu', 'Fagaras', 'Bucharest'], cost: 461
Number of city visited for BestFirst: 4


AStar execution time: 79220 ns
Path of AStar: ['Oradea', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'], cost: 429
Number of city visited for AStar: 6
.
----------------------------------------------------------------------
Ran 19 tests in 0.011s

OK
'''

'''
Discussion

1. By time

   Let us consider the algorithm execution time in Arad to Bucharest in each algorithm:
  
   BreadthFirst execution time: 33120 ns
   DepthFirst execution time: 24927 ns
   BestFirst execution time: 28189 ns
   AStar execution time: 82006 ns
   
   Let us consider the cost from Sibiu to Bucharest in each algorithm:
   
   BreadthFirst execution time: 31411 ns
   DepthFirst execution time: 15916 ns
   BestFirst execution time: 36468 ns
   AStar execution time: 65409 ns
   
   Let us consider the cost from Oradea to Bucharest in each algorithm:
   
   BreadthFirst execution time: 32394 ns
   DepthFirst execution time: 17354 ns
   BestFirst execution time: 40437 ns
   AStar execution time: 79220 ns
   
   From the result above, in terms of execution time, Depth-first has the shortest execution time compared to other algorithms followed by the Best-first, Breadth-First, and lastly A-star which has the longest execution time. We conclude that A-star has the longest execution time because it visits nodes and checks the best path that will have the lowest cost while Depth-first has the shortest execution time because it disregards the cost.
   
2. By city visited

   Let us consider the cost from Arad to Bucharest in each algorithm:
    
   BreadthFirst cost : 9
   DepthFirst cost : 7
   BestFirst cost : 4
   AStar cost : 6
   
   
   Let us consider the cost from Sibiu to Bucharest in each algorithm:
   
   BreadthFirst cost : 8
   DepthFirst cost : 4
   BestFirst cost : 3
   AStar cost : 5
   
   Let us consider the cost from Oradea to Bucharest in each algorithm:
   
   BreadthFirst cost : 8
   DepthFirst cost : 4
   BestFirst cost : 3
   AStar cost : 5
   
    
   Based on number of cities visited before getting to destination "Bucharest", we can see    that Best-first Algorithm perfomed better than the other 3 algorithms. While Breadth-      first Algorithm has the highest cost compared to the 3 other algorithms.
   
   

3. By cost
   
   Let us consider the cost from Arad to Bucharest in each algorithm:
   
   BreadthFirst cost : 450
   DepthFirst cost : 575
   BestFirst cost : 450
   AStar cost : 418
   
   Let us consider the cost from Sibiu to Bucharest in each algorithm:
   
   BreadthFirst cost : 310
   DepthFirst cost : 278
   BestFirst cost : 310
   AStar cost : 278
   
   Let us consider the cost from Oradea to Bucharest in each algorithm:
   
   BreadthFirst cost : 461
   DepthFirst cost : 429
   BestFirst cost : 461
   AStar cost : 429
   
   According to the cost, A-Star algorithm has the smallest cost. Best-fisrt algorithm only    considers the heuristic cost of each city. However, A-Star algorithm considers both        actual cost and heuristic cost. By considering both actual cost and heuristic cost,        A-Star has the lowest cost in the four algorithms. 
'''
