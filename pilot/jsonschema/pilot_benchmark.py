import time
import statistics
import jsonschema

print("jsonschema version:", jsonschema.__version__)

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string"},
        "tags": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["name", "age", "email"]
}

instance = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "tags": ["python", "benchmark", "json"]
}

# warm-up
for _ in range(3):
    jsonschema.validate(instance=instance, schema=schema)

times = []

for _ in range(20):
    start = time.perf_counter()

    jsonschema.validate(
        instance=instance,
        schema=schema
    )

    end = time.perf_counter()
    times.append(end - start)

print("Runs:", len(times))
print(f"Mean: {statistics.mean(times) * 1000:.4f} ms")
print(f"Median: {statistics.median(times) * 1000:.4f} ms")
print(f"Min: {min(times) * 1000:.4f} ms")
print(f"Max: {max(times) * 1000:.4f} ms")