# THE TRAVELING SALESMAN PROBLEM
**A CLASSIC CHALLENGE USING THE PRUNING METHOD**

**Abstract** 

The Traveling Salesman Problem (TSP) emerges as a pivotal challenge within the realm of combinatorial optimization, persisting as an open question in mathematical programming. This quandary, with practical implications spanning logistics, route planning, and resource distribution, has captivated the scientific community's attention since the 1950s. The inherent complexity of TSP becomes apparent in the vast and exponentially growing number of potential paths, rendering exhaustive exploration impractical. This project seeks to grapple with this complexity and propose a resolution method utilizing the pruning technique, elucidated in subsequent sections.

The narrative unfolds with a concise historical introduction, expounding upon the fundamental concepts associated with TSP and providing a brief overview of the Hamiltonian circuit, among other relevant topics slated for detailed exploration.

Moreover, we will delve into the reasons behind the efficacy of the pruning method in tackling this problem. The final section offers recommendations and conclusions, guiding potential future developments in this theoretical framework.

**Keywords:** Traveling Agent Problem, pruning method

**Introduction**

What constitutes the optimal route for visiting all cities and returning to the city of departure? We acknowledge the existence of multiple ways to reach the same destination, but selecting the most efficient one is crucial for directly minimizing travel costs; hence, it must also be the shortest. The Traveling Salesman's Problem (TSP) embodies the challenge of determining the shortest and, simultaneously, the most efficient route to reach a destination.

The inaugural solution to the Traveling Salesman Problem was reported in 1954 by George Dantzig, Ray Fulkerson, and Selmer Johnson. Their publication, titled 'Solutions to the Large-Scale Traveling Salesman Problem,' detailed a PAV solution method. This method was applied to address an instance involving 49 cities, where a travel agent aimed to visit a set of cities while assigning costs for visiting adjacent cities (representing the travel distance between two cities).

The inherent complexity emerges from the exhaustive exploration of all possible path combinations, rendering the quest for the optimal solution a captivating computational challenge.

Throughout this document, we will delve into various techniques and approaches implemented in the Python language, leveraging tools such as Google Colab, to confront this formidable challenge. This endeavor aspires to furnish a robust and optimal solution for this classic optimization problem within the realm of Python programming.

**Solution methods**

The traveling salesman problem consists of a salesman and a set of cities. The salesman has to visit each one of the cities starting from a certain one (e.g. the hometown) and returning to the same city. The challenge of the problem is that the traveling salesman wants to minimize the total length of the trip, as previously mentioned.

The complexity of calculating the traveling agent problem has sparked multiple initiatives to improve efficiency in route calculations. The most basic method is known as brute force, which consists of calculating all possible routes, which is extremely inefficient and almost impossible in large networks. There are also heuristics that have been developed due to the complexity in calculating optimal solutions in robust networks, which is why there are methods such as nearest neighbor, cheapest insertion and two-way. 
Finally, there are algorithms that provide optimal solutions, such as the branch and bound method, which works on the problem as an assignment algorithm.

A more sophisticated pruning method is to use a bounding function. We require some preliminary definitions, which will apply to any backtracking algorithm for a maximization problem.











References:

Definition:
A Hamiltonian cycle is a cycle on a graph that goes through all the
