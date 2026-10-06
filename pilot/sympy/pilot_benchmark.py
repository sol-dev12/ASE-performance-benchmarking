import time
import statistics
import sympy as sp

print("SymPy version:", sp.__version__)

x = sp.symbols("x")

expr = sum((x + i)**5 for i in range(100))

# warm-up
for _ in range(3):
    sp.expand(expr)

times = []

for _ in range(20):
    start = time.perf_counter()

    sp.expand(expr)

    end = time.perf_counter()
    times.append(end - start)

print("Runs:", len(times))
print(f"Mean: {statistics.mean(times) * 1000:.4f} ms")
print(f"Median: {statistics.median(times) * 1000:.4f} ms")
print(f"Min: {min(times) * 1000:.4f} ms")
print(f"Max: {max(times) * 1000:.4f} ms")