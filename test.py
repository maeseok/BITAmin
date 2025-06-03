vertices = ['a', 'b', 'c', 'd', 'e']
idx = {v: i for i, v in enumerate(vertices)}
n = len(vertices)

edges = [
    ('b', 'a', 1),
    ('a', 'd', -2),
    ('d', 'e', -3),
    ('e', 'b', 3),
    ('e', 'c', -5),
    ('b', 'c', -12),
    ('a', 'e', 5)
]

dist = [float('inf')] * n
prev = [None] * n
dist[idx['a']] = 0
history = [dist.copy()]

for _ in range(n - 1):
    updated = dist.copy()
    for u, v, w in edges:
        u_i, v_i = idx[u], idx[v]
        if dist[u_i] != float('inf') and dist[u_i] + w < updated[v_i]:
            updated[v_i] = dist[u_i] + w
            prev[v_i] = u
    dist = updated
    history.append(dist.copy())

# Distance Table
print("Distance Table:")
print("Step\t" + "\t".join(vertices))
for i, row in enumerate(history):
    print(f"{i}\t" + "\t".join(["inf" if x == float('inf') else str(x) for x in row]))

# Previous Vertex Table
print("\nPrevious Vertex Table:")
print("Vertex\t" + "\t".join(vertices))
print("Prev\t" + "\t".join([p if p else "-" for p in prev]))
