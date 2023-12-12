# THE TRAVELING SALESMAN PROBLEM
**A CLASSIC CHALLENGE USING THE PRUNING METHOD**

**Abstract** 

  
The Traveling Salesman Problem (TSP) stands as a significant challenge in the domain of combinatorial optimization, remaining an unsolved question in mathematical programming. This intricate problem, with real-world applications ranging from logistics to route planning and resource distribution, has intrigued the scientific community since the 1950s. The inherent complexity of TSP becomes evident in the extensive and exponentially increasing number of possible paths, making exhaustive exploration unfeasible. This project aims to address this complexity and present a resolution method leveraging the pruning technique, as detailed in the subsequent sections.
  

  
The narrative commences with a succinct historical introduction, elaborating on the foundational concepts related to TSP and offering a brief overview of the Hamiltonian circuit, among other pertinent topics slated for in-depth exploration.



Furthermore, we will delve into the rationales underpinning the effectiveness of the pruning method in addressing this problem. The concluding section provides recommendations and conclusions, offering guidance for potential future developments within this theoretical framework.

**Keywords:** Traveling Agent Problem, pruning method

**Introduction**

What constitutes the optimal route for visiting all cities and returning to the city of departure? While acknowledging the existence of multiple routes to reach the same destination, selecting the most efficient one is crucial for directly minimizing travel costs, and consequently, it must also be the shortest. The Traveling Salesman's Problem (TSP) encapsulates the challenge of determining the shortest and most efficient route to reach a destination.

The inaugural solution to the Traveling Salesman Problem was presented in 1954 by George Dantzig, Ray Fulkerson, and Selmer Johnson. Their publication, titled 'Solutions to the Large-Scale Traveling Salesman Problem,' outlined a PAV solution method. This method was employed to address an instance involving 49 cities, where a travel agent aimed to visit a set of cities while assigning costs for visiting adjacent cities, representing the travel distance between two cities.

The inherent complexity arises from the exhaustive exploration of all possible path combinations, turning the quest for the optimal solution into a captivating computational challenge.

Throughout this document, we will delve into various techniques and approaches implemented in the Python language, utilizing tools such as Google Colab, to tackle this formidable challenge. This endeavor aspires to provide a robust and optimal solution for this classic optimization problem within the realm of Python programming.

**Traveling salesman problem**

It is one of the most renowned and intricate challenges in computer science, and various engineering disciplines have sought to address it. As outlined by De los Cobos et al. (2010), the Traveling Salesman Problem (TSP) is formally defined: given a positive integer  $n>0$ and the distances between each pair of n cities, expressed through the $n x n$ matrix $(d_{ij})$, where $d_{ij}$ is a non-negative integer. 

A tour in this context refers to a trajectory that visits all cities exactly once. The primary objective is to identify a path that minimizes the total length of the tour.

In the context of the TSP, a cyclic permutation $\pi$ serves as a representation of a tour. 

If $\pi(j)$ is interpreted as the city following city j for j = 1, 2, ··· , n, the cost of the tour can be defined as follows:
$\sum_{j=1}d_{j\pi (j)}$, for $j \leq n$ .

**Solution methods**

The traveling salesman problem entails a salesman and a set of cities. The task at hand is for the salesman to visit each city, commencing from a specific city (perhaps his hometown), and eventually returning to the same starting point. The primary challenge revolves around minimizing the overall duration of the journey.

Given the inherent complexity associated with solving the traveling salesman problem, various initiatives have been launched to enhance the efficiency of route determination. The most fundamental approach, known as brute force, involves computing all possible routes—an approach that proves exceedingly inefficient and practically unfeasible, particularly in expansive networks. Furthermore, heuristics, including the nearest neighbor, cheapest insertion, and bidirectional methods, have been developed to address the intricacies of computing optimal solutions in robust networks.

Within this context, algorithms designed to yield optimal solutions have emerged, such as the branch and join method and the pruning method. This work will primarily focus on the latter, a technique aimed at reducing the search space by systematically eliminating branches and nodes. In the realm of the Traveling Salesman Problem (TSP), pruning proves indispensable for enhancing the algorithm's efficiency by discarding solutions known in advance not to lead to the optimal solution.

**Proposed algorithm**

To address this problem with the pruning method, pruning stands out as a crucial data compression technique employed in machine learning and search algorithms. Its primary objective is to diminish the size of decision trees by eliminating non-critical and redundant sections. This process significantly enhances the efficiency of the final classifier, leading to improved predictive accuracy. Here, we present an overview of how this method can be effectively applied to the problem:

The TSP can be conceptualized as a search tree, wherein each node represents a city, and edges signify connections between cities. The primary objective is to discover a tour that visits each city exactly once, returning to the starting point, while minimizing the total distance covered.

In the course of the search, various branches of the tree are traversed to assess potential solutions. Pruning plays a crucial role by eliminating branches incapable of leading to an optimal solution or those previously explored and deemed suboptimal.

To facilitate this process, a bounding function is employed to estimate the minimum distance achievable from a given node. This function guides decisions on whether to delve deeper into a branch or prune the current one, redirecting the search elsewhere in the tree.

Key pruning strategies include:

*Pruning by Feasibility:* Discarding branches failing to meet specific feasibility criteria. For instance, a branch is pruned if a city is visited twice in a tour, rendering it invalid.

*Pruning for Optimality:* Eliminating branches incapable of yielding a superior solution to the best-known solution encountered thus far. If the bounding function indicates that the minimum achievable distance on a branch exceeds the current best solution, pruning is warranted.

Continuous updates to the best-known solution occur as the tree is explored. Employing pruning techniques in the TSP can significantly enhance the algorithm's efficiency, particularly in minimizing execution time.

__Matrix of cost__

To address this issue irrespective of the method employed, we needed to take into account an entity known as the "matrix of cost." The primary goal is to minimize this matrix, utilizing various methods. For instance, let's consider the following approach:
M =
| $\infty$ | 3 | 5 | 8 |
|----------|----------|---|---|
| 3 | $\infty$ | 2 | 7 |
| 5 | 2 | $\infty$ | 6 |
| 8 | 7 | 6 | $\infty$ |

In this scenario, our objective is to minimize the matrix M. It is straightforward to understand how distances are defined in this context. We can approach it row by row, considering the permutation $C = (0 \quad 1 \quad 2 \quad 3)$, where each number corresponds to a city, with 0 representing the origin city. For the given matrix, the cost of the route $C$ is 19. This calculation is derived from the fact that the journey from city 0 to city 1 incurs a cost of 3, and the journey from city 2 to city 3 incurs a cost of 6. Essentially, the row number represents the current city, and the column number represents the destination city. On the other hand, it is worth noting that in the trace of the matrix, we encounter 
$\infty$. This is due to the fact that in Hamiltonian diagrams, the distance from a point to itself is defined as $\infty$.

**Algotithm**

https://colab.research.google.com/drive/12HSIfmL30q84P9Qqx1UihzjlF8KqapvR



**References**

1. Rosen, K. H. (1999). Discrete Mathematics Its Applications. Editorial.
2. Dantzig, G. B., Fulkerson, D. R., & Johnson, S. M. (1954). Solution of a large-scale traveling-salesman problem. Operations Research, 2(4), 393-410.
3. 


**Authors**

| [<img src="https://avatars.githubusercontent.com/u/141681072?v=4" width=115><br><sub>Eduardo Pérez Ponce</sub>](https://github.com/Edd-P-P) |  [<img src="https://avatars.githubusercontent.com/u/141791463?v=4" width=115><br><sub>Alejandro Sánchez Cisneros</sub>](https://github.com/alesac12) |  [<img src="https://avatars.githubusercontent.com/u/141685549?v=4" width=115><br><sub>Maria Fernanda Garcia León</sub>](https://github.com/fernandaleonn) |  [<img src="https://avatars.githubusercontent.com/u/141802122?v=4" width=115><br><sub>Eduardo Alanís Garcia</sub>](https://github.com/Eduardo-Alanis-Garcia)
| :---: | :---: | :---: | :---: |
