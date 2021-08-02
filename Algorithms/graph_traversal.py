###############
# Dijkstra's
# Finding shortest path
# - Unweighted graph --> BFS
# - Weighted, Directed and all positive edge graph --> Dijkstra's
# Data structure: min-heap
###########

# Dijkstra's algotirhm
# source = index of the source node
# edges  = adjcency list of all vertex/nodes
#        = {0: {1, 2},
#           1: {2},
#           3: {0}}
# n      = number of nodes in graph
#
import heapq
def shortest_path(source, edges, n){
  # make an array of distances, which are the distance from the source node.
  for index from 0 to n-1 {
     dist[index] = inf
  }
  # the source node is 0 distance from itself
  dist[source] = 0

  # make a min-heap of unvisited nodes
  toVisit = []
  for index from 0 to n-1 {
    toVisit.add( (dist[index], index) )
  }
  heapq.heapify(toVisit)

  while toVisit is not empty{
    # find the closest node to source so far. Because
    # no edge lengths are negative, there are no alternate
    # routes involving nodes further from source that give
    # a shorter path to this node

    # distance is stored in dist[] array, so discard.
    # keep index
    _, current = toVisit.extractMin();

    for destination, edge_dist in edges[current]{
      # does a detour through the current lead to a
      # shorter distance?
      dist_to_node = min(dist[destination], dist[current] + edge_dist)
      if dist_to_node is not dist[destination]:
        # need to update the heap / priority queue.
        # Finds index and updates first element to
        # dist_to_node, and reimplements to the heap invariant
        # takes O(log n) time.
        toVisit.updateElements( (dist_to_node, index))
    }
  }

  return dist
}




#############
# Prim's algorithm - Minimum Spanning Tree
# A "spanning tree" of a connected component with n nodes is a subgraph that has no cycles and leaves the n nodes connected.
# Every spanning tree has n-1 edges; for a typical graph there are multiple spanning trees.
# The tree with lowest sum of edge weights is called "minimum spanning tree"
# Data structure: min-heap
#############


#############
# Kruskal's algorithm
# 1. Sort original edges (O(m log m))
# 2. Add edges in order, rejecting those making cycles
#############


#############
# Colorig a graph
# assigning a color to each node such that no two nodes that are connected by an edge have the same color
