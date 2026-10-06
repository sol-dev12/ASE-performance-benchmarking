import time
import statistics
import networkx as nx

print("NetworkX version:", nx.__version__)

G = nx.grid_2d_graph(70, 70)
source = (0, 0)
target = (69, 69)

# warm-up
for _ in range(3):
    nx.shortest_path_length(G, source=source, target=target)

times = []

for _ in range(20):
    start = time.perf_counter()

    nx.shortest_path_length(
        G,
        source=source,
        target=target
    )

    end = time.perf_counter()
    times.append(end - start)

print("Runs:", len(times))
print(f"Mean: {statistics.mean(times) * 1000:.4f} ms")
print(f"Median: {statistics.median(times) * 1000:.4f} ms")
print(f"Min: {min(times) * 1000:.4f} ms")
print(f"Max: {max(times) * 1000:.4f} ms")