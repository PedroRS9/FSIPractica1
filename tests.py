import search
from search import Node
import pytest

# python -m pytest tests.py

@pytest.mark.parametrize("graph, output",
        [
                (search.GPSProblem('A','B',search.romania), [21,16,450,["B","F","S","A"]]),
                (search.GPSProblem('O','E',search.romania), [45,43,730,["E","H","U","B","F","S","O"]]),
                (search.GPSProblem('G','Z',search.romania), [41,34,615,["Z","A","S","F","B","G"]]),
                (search.GPSProblem('N','D',search.romania), [32,26,765,["D","C","P","B","U","V","I","N"]]),
                (search.GPSProblem('M','F',search.romania), [31,23,520,["F","S","R","C","D","M"]])
         ]        
)
def test_BFS(graph, output):  
        bfs_result = search.breadth_first_graph_search(graph)
        assert bfs_result.generados == output[0]
        assert bfs_result.visitados == output[1]
        assert bfs_result.node.path_cost == output[2]
        assert Node.to_string_nodes(bfs_result.node.path()) == output[3]

@pytest.mark.parametrize("graph, output",
        [
                (search.GPSProblem('A','B',search.romania), [18,10,733,["B","P","C","D","M","L","T","A"]]),
                (search.GPSProblem('O','E',search.romania), [41,31,698,["E","H","U","B","P","R","S","O"]]),
                (search.GPSProblem('G','Z',search.romania), [32,21,1284,["Z","A","T","L","M","D","C","P","R","S","F","B","G"]]),
                (search.GPSProblem('N','D',search.romania), [31,19,1151,["D","C","P","R","S","F","B","U","V","I","N"]]),
                (search.GPSProblem('M','F',search.romania), [29,18,928,["F","B","P","R","S","A","T","L","M"]])
         ]        
)
def test_DFS(graph, output):
        dfs_result = search.depth_first_graph_search(graph)
        assert dfs_result.generados == output[0]
        assert dfs_result.visitados == output[1]
        assert dfs_result.node.path_cost == output[2]
        assert Node.to_string_nodes(dfs_result.node.path()) == output[3]

@pytest.mark.parametrize("graph, output",
        [
                (search.GPSProblem('A','B',search.romania), [31,24,418,["B","P","R","S","A"]]),
                (search.GPSProblem('O','E',search.romania), [43,40,698,["E","H","U","B","P","R","S","O"]]),
                (search.GPSProblem('G','Z',search.romania), [41,35,583,["Z","A","S","R","P","B","G"]]),
                (search.GPSProblem('N','D',search.romania), [32,26,765,["D","C","P","B","U","V","I","N"]]),
                (search.GPSProblem('M','F',search.romania), [36,27,520,["F","S","R","C","D","M"]])
         ]        
)
def test_branch_and_bound(graph, output):
        bab_result = search.branch_and_bound(graph)
        assert bab_result.generados == output[0]
        assert bab_result.visitados == output[1]
        assert bab_result.node.path_cost == output[2]
        assert Node.to_string_nodes(bab_result.node.path()) == output[3]

@pytest.mark.parametrize("graph, output",
        [
                (search.GPSProblem('A','B',search.romania), [16,6,418,["B","P","R","S","A"]]),
                (search.GPSProblem('O','E',search.romania), [32,15,698,["E","H","U","B","P","R","S","O"]]),
                (search.GPSProblem('G','Z',search.romania), [26,12,583,["Z","A","S","R","P","B","G"]]),
                (search.GPSProblem('N','D',search.romania), [23,12,765,["D","C","P","B","U","V","I","N"]]),
                (search.GPSProblem('M','F',search.romania), [25,16,520,["F","S","R","C","D","M"]])
         ]        
)
def test_branch_and_bound_underestimation(graph, output):
        bab_underestimation_result = search.branch_and_bound_underestimation(graph)
        assert bab_underestimation_result.generados == output[0]
        assert bab_underestimation_result.visitados == output[1]
        assert bab_underestimation_result.node.path_cost == output[2]
        assert Node.to_string_nodes(bab_underestimation_result.node.path()) == output[3]