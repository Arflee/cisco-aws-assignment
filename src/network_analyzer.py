def find(parent, node):
    # If the node is not its own parent, it's not the root.
    if parent[node] != node:
        # Recursively find the root of node's parent and update parent[node] to point directly to the root.
        parent[node] = find(parent, parent[node])
    # Return the representative (root) of this node.
    return parent[node]

def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

def kruskal_mst(edges, num_nodes):
    edges.sort(key=lambda x: x[2])  # Sort edges by cost
    parent = {i: i for i in range(1, num_nodes + 1)}
    rank = {i: 0 for i in range(1, num_nodes + 1)}
    
    mst = []
    total_cost = 0
    
    for node1, node2, cost in edges:
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            mst.append({"from": node1, "to": node2, "cost": cost})
            total_cost += cost
    
    return total_cost, mst