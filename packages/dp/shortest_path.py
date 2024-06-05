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

    if(start == stop):
        raise Exception("Starting vertex can not be the same as the stopping vertex.")
    
    num_vertices    = len(cost_matrix[0])
    stop_adj_in     = [(i + 1) for i in range(num_vertices) if ((cost_matrix[i][stop-1] != 0) and ((i+1) != start))] 
    non_stop_adj_in = [(i + 1) for i in range(num_vertices) if (((i+1) not in stop_adj_in)    and ((i+1) != start))] 

    # Remove the stopping vertex
    non_stop_adj_in.remove(stop) 

    # Sort vertex list in order of stopping vertex in-adjacencies, non stopping vertex in-adjacencies, starting vertex
    vertices = stop_adj_in + non_stop_adj_in + [start] 

    optimal_cost_to_stop = {} 
    optimal_vertex_out   = {} 

    while_iters = 0 
    done        = False 

    while not done: 

        while_iters += 1 
        vertex_count = 0 

        # Iterate through the vertices
        for vertex in vertices: 

            # Obtain out-adjacencies to that vertex 
            vertex_adj_out = [(i+1) for i in range(num_vertices) if (cost_matrix[vertex-1][i] != 0 )]

            costs = []
            outs  = []
            exceptions = 0

            # Calculate costs, outs, and exceptions 
            for out in vertex_adj_out:
                if(out == stop):
                    costs.append(cost_matrix[vertex-1][out-1]) 
                    outs.append(out) 
                else:
                    try:
                        costs.append(cost_matrix[vertex-1][out-1] + optimal_cost_to_stop[out]) 
                        outs.append(out) 
                    except:
                        exceptions += 1
            
            # If there are no excpetions, compute optimal cost
            if(exceptions == 0):
                # Check costs is non-empty 
                if(costs): 
                    optimal_cost_to_stop[vertex] = min(costs)
                    optimal_vertex_out[vertex]   = outs[costs.index(min(costs))] 
                else: 
                    optimal_cost_to_stop[vertex] = np.inf
                    optimal_vertex_out[vertex]   = np.inf 
                vertex_count += 1

        # Stop once we have computed the optimal cost for each vertex
        if(vertex_count == (num_vertices - 1)):
            done = True 

    # Extract the optimal path from optimal vertices out
    path = []
    path.append(start) 
    next_vertex = optimal_vertex_out[start] 

    while(next_vertex != stop):
        path.append(next_vertex) 
        next_vertex = optimal_vertex_out[next_vertex] 

    path.append(stop)
    
    return { 
        "path" : path, 
        "cost" : optimal_cost_to_stop[start], 
        "iter" : while_iters 
    }