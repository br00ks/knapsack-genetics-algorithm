# Solving the 0-1 Knapsack problem with Genetics algorithm
Solve 0-1 knapsack problem with genetics algorithm

This project is supposed to show an algorithm to solve the 0-1 knapsack problem with genetics algorithms.
The algorithm implemented was provided by the paper of Hristakeva (see References).

The Knapsack Problem (KP) is a combinatorial optimization problem. This problem also is NP (non deterministic polynomial), which means that there are no known algorithms that would guarantee to run in polynomial time. In order to find approximately solutions for optimizations problems such as the Knapsack Problem we can use Genetics Algorithms. Genetic Algorithms do not necessarily give the optimal solution, but they are currently the most efficient ways for finding an approximately optimal solution.

## 0-1 Knapsack Problem
The Knapsack Problem is a combinatorial optimization problem. Within a given set S with n items that are potentially placed in the knapsack, we are looking for a subset T. Each item has a weight and a value. The idea is to maximize the value of objects in a knapsack without exceeding a capacity W.
The 0-1 Knapsack Problem is a specific problem KP where it is not allowed to take fractional amounts of items. Each item is either included or excluded.

## Flowchart of the algorithm
<p align="center"><img src="https://github.com/br00ks/knapsack-genetics-algorithm/blob/master/diagram.png" /></p>


## References:
- http://www.micsymposium.org/mics_2004/Hristake.pdf
- http://www.obitko.com/tutorials/genetic-algorithms/index.php
