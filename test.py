# Bellman-Ford Algorithm 구현

# 그래프 정의
edges = [
    ("b", "a", 1),
    ("b", "c", -12),
    ("a", "d", -2),
    ("a", "e", 5),
    ("d", "e", -3),
    ("e", "c", -5),
    ("e", "b", 3)
]

vertices = ["a", "b", "c", "d", "e"]
dist = {v: float("inf") for v in vertices}
prev = {v: None for v in vertices}

# 시작점
dist["a"] = 0

# V-1 번 반복
for i in range(len(vertices) - 1):
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            prev[v] = u

# 결과 출력
print("최단 거리:")
for v in vertices:
    print(f"{v}: {dist[v]}")

print("\n이전 정점:")
for v in vertices:
    print(f"{v}: {prev[v]}")
