# FSI Practica 1

This is a repository for the first practice of the subject "Fundamentos de los Sistemas Inteligentes" in the University of Las Palmas de Gran Canaria.
The practice consists in the implementation of algorithms for solving search problems (DFS, BFS, Branch and Bound, Branch and Bound with underestimation)

## Getting Started

### How to install

First of all, you need to clone the repository.

```
git clone https://github.com/PedroRS9/FSIPractica1.git
```

Then, you need to install the requirements. You need to install Pytest for being able to run the unit tests.

```
pip install pytest
```

### How to run

If you want to run the main file which prints the search algorithm results with the execution time:

```commandline
python run.py
```

If you want to run the unit tests:

```commandline
python -m pytest tests.py
```

### Explanation of each file

#### run.py

This file is the main file of the project. It contains some functions for running the four algorithms (BFS, DFS, Branch and Bound, Branch and Bound with underestimation) and the function for running the tests. The graph used for the tests (Romania) is contained in search.py. We run each algorithm in that graph and, for each algorithm, we print the output path, the number of generated nodes, the number of visited nodes, the path cost and the execution time.

Our code has been written using several methods for improving the readibility and the modularity. We will explain each added method:

* **make_tests()**: Creates a set of test problems using the Romania graph and performs searches on each using multiple search methods (breadth_first_graph_search, depth_first_graph_search, branch_and_bound, branch_and_bound_underestimation), which are in the **search.py** file. For each test, the **do_search()** method is called passing the desired search algorithm as a parameter.
* **do_search()**: Executes a search method on a given problem, measures the execution time, and calls **show_result** to display the results.
* **show_result():** Displays the results of a search, including the path, number of generated and visited nodes, path cost, and execution time.

*How do we  measure the execution time?* For measuring the execution time, we're using the **default_timer** class of the **timeit** library (renamed as "timer" in our code). For each algorithm, we start the timer before executing the search algorithm, and we stop it just as it ends.

#### search.py

This file contains the implementation of the graph used for the tests (Romania) and the implementation of the four algorithms (BFS, DFS, Branch and Bound, Branch and Bound with underestimation). The file also includes definitions for graph-related classes, such as **Graph** and **Node**, essential for representing and traversing problem spaces. We've modified the original code for implementing the algorithms. Let's discuss our modifications:

* **graph_search()**: Search through the successors of a problem to find a goal. It takes two parameters (**problem**, which consists of the root node, the destination node and the graph), and **fringe** (the structure used for the search, which can be a queue [**FIFOQueue**], a stack [**Stack**], a priority queue for the branch and bound algorithm [**BABPriorityQueue**] and a priority queue for the branch and bound with underestimation algorithm [**HeuristicPriorityQueue**] ). We'll discuss the implementation of each structure when we explain the **utils.py** file later. We've modified the original code for keeping track of the number of generated nodes and visited nodes. This function returns an object of type **Result**, which contains the last visitated node, the number of generated nodes, the number of visited nodes, the path cost and the execution time.
* **breadth_first_graph_search()**: The function for calculating the path using the BFS algorithm. It calls the **graph_search** function with the **FIFOQueue** structure.
* **depth_first_graph_search()**: The function for calculating the path using the DFS algorithm. It calls the **graph_search** function with the **Stack** structure.
* **branch_and_bound()**: The function for calculating the path using the Branch and Bound algorithm. It calls the **graph_search** function with the **BABPriorityQueue** structure.
* **branch_and_bound_underestimation()**: The function for calculating the path using the Branch and Bound with underestimation algorithm. It calls the **graph_search** function with the **HeuristicPriorityQueue** structure.
* **to_string_nodes()**: The function for converting a list of nodes into a list of strings representing the nodes.


#### utils.py

This file contains the implementation of the structures used for the search algorithms. It also contains the implementation of the **Resultado** class, which is used for returning the results of the search algorithms. It also contains another data structures like **Dict**, functions for sequences or statistical and mathematical functions. Now, we'll discuss the structures we've added here:

* **BABPriorityQueue**: This class is used for implementing the priority queue for the Branch and Bound algorithm. It's a subclass of the **Queue** class. The difference is that this class automatically sorts the elements of the queue when you append or extend the queue.
* **HeuristicPriorityQueue**: This class is used for implementing the priority queue for the Branch and Bound with underestimation algorithm. It's a subclass of the **Queue** class. The difference is that this class automatically sorts the elements of the queue when you append or extend the queue. The sorting is done using the node's accumulated path cost and the heuristic function (euclidean distance to the node).

#### tests.py

This file contains the unit tests for the search algorithms. To achieve that goal, we're using the **Pytest** module for keeping our code clean and easily understandable. For each algorithm, we check that the number of generated nodes, the number of visited nodes, the path cost and the path are the expected output values for the problem.

### Authors
* **Pedro Romero Suárez** - [PedroRS9](https://github.com/PedroRS9)
* **Nahuel Cosme Díaz Vera** - [NahuelCosmeDiazVera](https://github.com/NahuelCosme-DiazVera)