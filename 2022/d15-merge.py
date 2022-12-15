# Say we have the following intervals, a list of [a,b)
intervals = [[9,10],[9,15],[10,12],[-1,0], [9,10],[2,4],[2,3],[1,3],[6,8]]

def merge_intervals(intervals):
    intervals.sort()
    stack = [intervals[0]]
    for lo, hi in intervals[1:]:
        qlo, qhi = stack[-1]
        # We can play with <= and <= 1+ in order to change how we represent those ranges,
        # depending on if the upper value is included or not
        if lo <= qhi:
            # The new interval overlaps the largest, latest range, so we update the max
            stack[-1][1] = max(hi, qhi)
        else:
            stack.append([lo, hi])
    return stack

# output:
# [[-1, 0], [1, 4], [6, 8], [9, 15]]
stack = merge(intervals)
print(stack)