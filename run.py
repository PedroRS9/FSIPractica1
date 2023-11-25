# Search methods

import search
import tests
from timeit import default_timer as timer

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

def show_result(result, execution_time):
    print("Path: " + str(result.node.path()))
    print("Generated nodes: " + str(result.generados))
    print("Visited nodes: " + str(result.visitados))
    print("Total cost: " + str(result.node.path_cost))
    print("Execution time: " + str(execution_time) + " ms")
    print("=" * 40)

def do_search(problem, method):    
    print ("Search method: " + method.__name__)
    start = timer()
    result = method(problem)
    end = timer()
    execution_time = round((end - start) * 1000, 3)
    show_result(result, execution_time)

def make_tests():
    tests = [
        search.GPSProblem('A', 'B', search.romania),
        search.GPSProblem('O', 'E', search.romania),
        search.GPSProblem('G', 'Z', search.romania),
        search.GPSProblem('N', 'D', search.romania),
        search.GPSProblem('M', 'F', search.romania)
    ]
    for test in tests:
        print("*" * 40)
        print("TEST: " + test.initial + " -> " + test.goal)
        print("*" * 40)
        do_search(test, search.breadth_first_graph_search)        
        do_search(test, search.depth_first_graph_search)        
        do_search(test, search.branch_and_bound)
        do_search(test, search.branch_and_bound_underestimation)

make_tests()