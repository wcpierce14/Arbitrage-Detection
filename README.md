# Arbitrage-Detection

This project implements the Bellman-Ford algorithm to detect arbitrage opportunities within a set of exchange rates between currencies. Within this repository, there are four Python files: currencies.py, arbitrageTests.py, vertex.py, and arbitrage.py.

####################################################################################

currencies.py is a Currencies Class that has 5 instance variables:

rates = a 2D array representing the exchange rates

currs: a list of the currency names as strings

adjList: the adjacency list of Vertex objects

adjMat: the adjacency matrix (stored as a 2D list)

negCyc: what will ultimately contain the negative cost cycle, stored as a list of ranks (not a list of vertices)

####################################################################################

arbitrageTests.py contains the testRates function that tests all of the provided exchange rate examples to look for arbitrage opportunities.

####################################################################################

vertex.py contains the Vertex class that has 4 instance variables:

rank: the rank (label) of the given vertex

neigh: the list of the neighboring vertices

dist: the distance from the start vertex

prev: the previous vertex in the path

This file also contains init, repr and isEqual

####################################################################################

arbitrage.py contains the code that executes the Bellman Ford Algorithm. Within it, you can find the two functions rates2mat and detectArbitrage.
