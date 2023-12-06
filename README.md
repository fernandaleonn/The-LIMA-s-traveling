# The-LIMA-s-traveling

**Abstract** 

The traveling agent problem (TSP) stands out as a crucial challenge in the field of combinatorial optimization and persists as an open question in mathematical programming. This problem, with practical applications in areas such as logistics, route planning and resource distribution, has aroused deep interest in the scientific community since the 1950s. The inherent complexity of TSP manifests itself in the vast and exponential number of possible paths, making exhaustive exploration impractical. This project aims to address this complexity and explore a way of resolution, using the pruning method, which will be explained during the course of the project.

A brief historical introduction is presented, the aforementioned concepts and also a brief explanation of the Hamiltonian circuit, among other concepts that will be addressed in detail.

Furthermore, we will see why this method is very useful for solving this problem and finally, a section is presented where recommendations and conclusions are presented, which guide possible future developments of this theory.

**Keywords:** Traveling Agent Problem, bounding functions

**Introduction**

What is the optimal route to choose to visit all the cities and return to the city of departure? We know that there may be multiple ways to get to the same place, but choosing the most efficient one is directly related to reducing travel costs, so it should also be the shortest. The Traveling Salesman Problem refers to the problem of finding the shortest and, at the same time, the most efficient route to reach a destination.

The first reported solution to solve the Traveling Agent problem was in 1954, when George Dantzig, Ray Fulkerson, and Selmer Johnson published a description of a PAV solution method titled "Solutions of a large scale traveling salesman problem", to solve a instance of 49 cities where a travel agent wants to visit a set of cities, assigning them a cost for visiting adjacent cities (travel distance between two cities).

The inherent complexity of exploring all possible path combinations makes finding the optimal solution a fascinating computational challenge.

Over the course of this document, we will explore various techniques and approaches implemented in the Python language, also using Google Colab, to address the traveling agent challenge. This work aims to provide solutions and best practices to face this classic optimization problem in the context of Python programming.

**Solution methods**

The traveling salesman problem consists of a salesman and a set of cities. The salesman has to visit each one of the cities starting from a certain one (e.g. the hometown) and returning to the same city. The challenge of the problem is that the traveling salesman wants to minimize the total length of the trip, as previously mentioned.

The complexity of calculating the traveling agent problem has sparked multiple initiatives to improve efficiency in route calculations. The most basic method is known as brute force, which consists of calculating all possible routes, which is extremely inefficient and almost impossible in large networks. There are also heuristics that have been developed due to the complexity in calculating optimal solutions in robust networks, which is why there are methods such as nearest neighbor, cheapest insertion and two-way. 
Finally, there are algorithms that provide optimal solutions, such as the branch and bound method, which works on the problem as an assignment algorithm.

A more sophisticated pruning method is to use a bounding function. We require some preliminary definitions, which will apply to any backtracking algorithm for a maximization problem.











References:

Definition:
A Hamiltonian cycle is a cycle on a graph that goes through all the
