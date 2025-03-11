from src import network_analyzer

def test_union_find():
    # Setup initial disjoint sets
    parent = {1: 1, 2: 2, 3: 3}
    rank = {1: 0, 2: 0, 3: 0}
    
    # After union of 1 and 2, they should have the same root.
    network_analyzer.union(parent, rank, 1, 2)
    assert network_analyzer.find(parent, 1) == network_analyzer.find(parent, 2), "1 and 2 should be in the same set"
    
    # Union 2 and 3 and then check that 1 and 3 are connected
    network_analyzer.union(parent, rank, 2, 3)
    assert network_analyzer.find(parent, 1) == network_analyzer.find(parent, 3), "1 and 3 should be in the same set"

def assertEdgeLength(mst, expected_edges):
    assert len(mst) == len(expected_edges), "MST should have" + str(len(expected_edges)) + " edges"
    for edge in expected_edges:
        assert edge in mst, f"Expected edge {edge} not found in MST"

def assertCost(edges, expected_cost):
    total_cost, mst = network_analyzer.kruskal_mst(edges, num_nodes=5)
    
    assert total_cost == expected_cost, "Total cost should be " + str(expected_cost) + " for the MST"
    return mst

def test_kruskal_mst1():
    edges = [
        (1, 2, 1),
        (1, 3, 3),
        (2, 3, 2),
        (3, 4, 4),
        (2, 4, 5)
    ]
    
    # Running Kruskal's algorithm should yield an MST with total cost 7:
    # Expected MST edges: (1,2,1), (2,3,2), (3,4,4)
    mst = assertCost(edges, expected_cost=7)
        
    # Expected edges in the MST (order doesn't matter)
    expected_edges = [
        {"from": 1, "to": 2, "cost": 1},
        {"from": 2, "to": 3, "cost": 2},
        {"from": 3, "to": 4, "cost": 4}
    ]
    
    assertEdgeLength(mst, expected_edges)

def test_kruskal_mst2():
    edges = [
        (1, 2, 3),
        (2, 3, 1),
        (3, 4, 4),
        (1, 4, 2)
    ]
    
    mst = assertCost(edges, expected_cost=6)
        
    expected_edges = [
        {"from": 1, "to": 2, "cost": 3},
        {"from": 2, "to": 3, "cost": 1},
        {"from": 1, "to": 4, "cost": 2}
    ]
    
    assertEdgeLength(mst, expected_edges)
