from collections import deque

k = 0
def topo_sort(edges):
    g = [[] for _ in range(k)]
    left = [0] * k  # 每个 i 对应的前置数量
    for x, y in edges:
        x -= 1
        y -= 1
        g[x].append(y)
        left[y] += 1

    order = []  # 拓扑序
    # BFS
    q = deque(i for i, v in enumerate(left) if v == 0)

    while q:
        x = q.popleft()
        order.append(x)
        for y in g[x]:
            left[y] -= 1  # 依赖于x的值-1
            if left[y] == 0:  # 完成前置
                q.append(y)  # 入列
    return order if len(order) == k else None