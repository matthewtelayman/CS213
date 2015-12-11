#Matt Layman CS213 dijkstra.py
import heap_id

def node_by_name(nodes, city, state):
        """Returns the first node that matches specified location.
        
        Args:
            city: the description of the node should include city.
            state: the state of the node should match state.
        
        Returns:
            The node if it exists, or None otherwise.
        """
    
        for node in nodes:
            if node.state == state:
                if city in node.description:
                    return node
        return None
        
def distance(node1, node2):
    """Returns the distance between node1 and node2, ignoring the Earth's 
    curvature.
    """
    latitude_diff = node1.latitude - node2.latitude
    longitude_diff = node1.longitude - node2.longitude
    return (latitude_diff**2 + longitude_diff**2)**.5

def create_adjacency_lists(nodes, links):
    # Use an adjacency list representation, by putting all vertices
    # adjacent to node in node.adj.
    for node in nodes:
        node.adj = []
    for link in links:
        link.begin.adj.append(link.end)
        link.end.adj.append(link.begin)

def create_edge_set(links):
    # Put edges in a set for faster lookup.
    edge_set = set()
    for link in links:
        edge_set.add( (link.begin, link.end) )
    return edge_set

def reconstruct_path(source, destination):
    """Returns list of nodes in path from source to destination. Uses
    node.parent pointers."""
    node = destination
    p = [destination]
    while node != source:
        node = node.parent
        p.append(node)
    p.reverse()
    return p

def _heap_insert(node):
    """Assumes key is already in node.distance."""
    node.ID = heap.insert(node.distance)
    ID_to_node[node.ID] = node

def _heap_decrease_key(node):
    """Assumes new key is already in node.distance."""
    heap.decrease_key_using_id(node.ID, node.distance)

def _heap_extract_min():
    """Returns the node associated with the minimum key."""
    ID = heap.extract_min_with_id()[1]
    node = ID_to_node[ID]
    return node

def shortest_path(nodes, edges, weight, source, destination):
    """Returns list of nodes in path from source to destination. Uses
    node.parent pointers."""
    dijkstra(nodes, edges, weight, source)
    return reconstruct_path(source, destination)

def dijkstra(nodes, edges, weight, source):
    """Finds the shortest path from source to all nodes in the
    graph (nodes and edges), where the weight on edge (u, v) is
    given by weight(u, v). Assumes that all weights are
    non-negative.

    At the end of the algorithm:
    - node.visited is True if the node is visited, False otherwise.
    (Note: node is visited if shortest path to it is computed.)
    - node.distance is set to the shortest path length from source
        to node if node is visited, or not present otherwise.
    - node.parent is set to the previous node on the shortest path
        from source to node if node is visited, or not present otherwise.        

    Returns the number of visited nodes.
    """

    global heap, ID_to_node
    
    # Initialize.
    for node in nodes:
        node.marked = False # node is marked if it has been added to the heap.
        node.visited = False # node is visited if the shortest path from source
                             # to node is found (i.e., if removed from heap).
    num_visited = 0

    # create adjacency lists/edge sets
    create_adjacency_lists(nodes, edges)
    edge_set = create_edge_set(edges)

    # run dijkstra's algorithm.

    ID_to_node = {}
    heap = heap_id.heap_id()
    source.distance = 0
    _heap_insert(source)
    source.marked = True

    while(heap.heapsize > 0):
        current = _heap_extract_min()
        current.visited = True
        num_visited = num_visited + 1
        for node in current.adj: # Relax nodes adjacent to current.
            if not node.visited:
                new_distance = weight(current, node) + current.distance
                if node.marked:
                    if new_distance < node.distance:
                        node.distance = new_distance
                        _heap_decrease_key(node)
                        node.parent = current
                else:
                    node.distance = new_distance
                    _heap_insert(node)
                    node.marked = True
                    node.parent = current

    
    return num_visited
