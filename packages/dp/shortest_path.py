import numpy as np 

def shortest_path(cost_matrix : list, start : int, stop : int) -> dict: 
    """
    Returns the shortest path between a starting vertex, `start`, and a stopping 
    vertex, `stop`, in a weighted, directed graph, given a cost matrix, `cost_matrix`. 

    It is assumed that the vertices of the graph are indexed naturally, (1,2,...,N),. 
    The cost matrix is hence an N x N matrix wherein the entry in row i, column j is 
    the cost to travel from vertex i to vertex j, if there is a directed edge from i 
    to j, and 0 otherwise. 
    """
