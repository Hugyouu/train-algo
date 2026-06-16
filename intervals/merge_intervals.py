def merge(intervals: list[list[int]]) -> list[list[int]]:
    limit = len(intervals)-1
    arr = []
    intervals.sort()
    for i, interval in enumerate(intervals):
        arr.append(intervals[i])
        if i >= limit: break
        if interval[1] >= intervals[i+1][0]:
            tmp = intervals
            tmp[i][1] = intervals[i+1][1]
            arr[i] = tmp[i]
            intervals.pop(i+1)
            limit -= 1
    return arr


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(merge(intervals))

intervals = [[4,7],[1,4]]
intervals.sort()
print(intervals)


# def merge(intervals: list[list[int]]) -> list[list[int]]:
#     intervals.sort(key=lambda x: x[0])
#     res = [intervals[0]]
#     for start, end in intervals:
#         if start <= res[-1][-1]:
#             res[-1][-1] = max(res[-1][-1], end)
#         else:
#             res.append([start, end])
#     return res