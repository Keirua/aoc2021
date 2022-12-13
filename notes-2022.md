# day 9

Parsing
```python
# Love this pattern
moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RDLU]) (\d+)", input)]
```
# day 11:

regex + lambda + eval for the parsing

```python
import re
operation_code = re.search(r"new = (.*)", lines[2]).group(1)
return cls(
    items=Counter([int(s) for s in re.findall("(\d+)", lines[1])]),
    operation_code=operation_code,
    op=lambda old: eval(operation_code),
    test=int(lines[3].split()[-1]),
    on_true=int(lines[4].split()[-1]),
    on_false=int(lines[5].split()[-1])
)
```


# day 12: dijkstra

```python
import heapq
def dijkstra(grid, start=(0, 0), end=None):
    """Dijkstra's algorithm implementation using a priority queue"""
    # Initial state:
    #  - all the distances to the starting node are maximal
    #    (except the starting node: it has a distance of 0 to itself).
    #  - all the ancestors are non-existing
    dist = { v: 1000000000000000 for v in grid.all_coords()}
    dist[start] = 0
    prev = {v: None for v in grid.all_coords()}

    # The queue of nodes we will consider, with
    Q = [(0, start)]
    while len(Q) > 0:
        # We consider the "cheapest" node, that is the node with the lowest cost.
        # We store the tuples (cost, position). In this context, heapq.heappop compares on the cost
        # https://docs.python.org/3.11/library/heapq.html#basic-examples
        min_dist, min_coord = heapq.heappop(Q)

        # we may provide an end node, if so we can break early
        if end is not None and min_coord == end:
            break

        if min_dist > dist[min_coord]:
            continue

        for neighbour in grid.valid_neighbours(min_coord):
            new_distance = min_dist + 1
            # If we found a better path, we update both the cost and the predecessor
            # and add this node to the queue
            if new_distance < dist[neighbour]:
                dist[neighbour] = new_distance
                prev[neighbour] = min_coord
                heapq.heappush(Q, (new_distance, neighbour))

    return dist, prev
```

# day 13: sorting according to a custom function

```python
def cmp(a, b):
# do something, return -1, 0 or 1

sorted_packets = sorted(packets, key=functools.cmp_to_key(cmp))
p2 = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
print(p2)
```
