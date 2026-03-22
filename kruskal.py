def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(parent, x, y):
    parentX = find_parent(parent, x)
    parentY = find_parent(parent, y)
    parent[parentY] = parentX


def kruskal(n, edges):
    edges.sort()                      
    parent = list(range(n))
    mst = []
    total_cost = 0

    for w, u, v in edges:
        if find_parent(parent, u) != find_parent(parent, v):
            mst.append((u, v, w))
            total_cost += w
            union(parent, u, v)

    return mst, total_cost




edges = [
    (1, 3, 4),  # D-E
    (2, 3, 6),  # D-G
    (3, 4, 6),  # E-G
    (3, 2, 3),  # C-D
    (3, 6, 7),  # G-H
    (3, 2, 5),  # C-F
    (4, 1, 2),  # B-C
    (4, 1, 4),  # B-E
    (4, 1, 5),  # B-F
    (4, 1, 7),  # B-H
    (5, 0, 7),  # A-H
    (6, 3, 5),  # D-F
    (8, 0, 1),  # A-B
    (10, 0, 5)  # A-F
]

mst, cost = kruskal(8, edges)

print("MST:", mst)
print("Total Cost:", cost)