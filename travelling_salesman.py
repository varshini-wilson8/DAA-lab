import heapq
from itertools import permutations

INF = float("inf")


class Node:
    """State space tree node for Branch and Bound TSP."""

    def __init__(self, matrix, cost, path, level):
        self.matrix = matrix
        self.cost = cost
        self.path = path
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost


def reduce_matrix(mat):
    """Reduce matrix rows and columns and return reduction cost."""
    n = len(mat)
    m = [row[:] for row in mat]
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min != INF and row_min > 0:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min != INF and col_min > 0:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_branch_and_bound(cost_matrix, n):
    """Solve TSP using LC Branch and Bound with Matrix Reduction."""
    reduced_mat, initial_cost = reduce_matrix(cost_matrix)
    pq = []
    root = Node(reduced_mat, initial_cost, [0], 0)
    heapq.heappush(pq, root)

    while pq:
        curr = heapq.heappop(pq)
        u = curr.path[-1]

        if curr.level == n - 1:
            final_path = curr.path + [0]
            return final_path, curr.cost

        for v in range(n):
            if v not in curr.path and curr.matrix[u][v] != INF:
                child_mat = [row[:] for row in curr.matrix]

                # Set row u and column v to INF
                for k in range(n):
                    child_mat[u][k] = INF
                    child_mat[k][v] = INF

                # Prevent early return to start node
                child_mat[v][0] = INF

                red_mat, red_cost = reduce_matrix(child_mat)
                new_cost = curr.cost + curr.matrix[u][v] + red_cost

                child_node = Node(
                    red_mat, new_cost, curr.path + [v], curr.level + 1
                )
                heapq.heappush(pq, child_node)

    return None, INF


def tsp_brute_force(cost_matrix, n):
    """Brute force approach for verification."""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None
    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        c = sum(cost_matrix[path[i]][path[i + 1]] for i in range(n))
        if c < best_cost:
            best_cost = c
            best_path = path
    return best_path, best_cost


# --- Main Execution ---
if __name__ == "__main__":
    # 5-city cost matrix
    cost = [
        [INF, 10, 8, 9, 7],
        [10, INF, 10, 5, 6],
        [8, 10, INF, 8, 9],
        [9, 5, 8, INF, 6],
        [7, 6, 9, 6, INF],
    ]
    n = 5
    cities = ["A", "B", "C", "D", "E"]

    # Solve using Branch and Bound
    bb_path, bb_cost = tsp_branch_and_bound(cost, n)

    # Solve using Brute Force
    bf_path, bf_cost = tsp_brute_force(cost, n)

    print("5-City TSP - Cost Matrix:")
    print(f'{"":>4}', " ".join(f"{c:>5}" for c in cities))
    for i, row in enumerate(cost):
        r = ["INF" if x == INF else str(x) for x in row]
        print(f"{cities[i]:>4}", " ".join(f"{v:>5}" for v in r))

    print("\n=== Branch and Bound Result ===")
    print(f'Optimal Tour: {" -> ".join(cities[i] for i in bb_path)}')
    print(f"Minimum Cost: {bb_cost}")

    print("\n=== Path Edge Costs ===")
    for i in range(n):
        u, v = bb_path[i], bb_path[i + 1]
        print(f"  {cities[u]} -> {cities[v]}: cost = {cost[u][v]}")