import heapq
def main(arr):
    heapq.heapify(arr)
    start, end = arr[0], arr[0]
    res = [[start, end]]
    while arr:
        top = heapq.heappop(arr)
        print(start, end)
        if top == end:
            continue
        elif top == end + 1:
            res[-1][1] += 1
            end += 1
            continue
        else:
            new = [top, top] if arr else [top]
            res.append(new)
            end = top
            start = top
            
    if len(res[-1]) > 1:
        if res[-1][0] == res[-1][1]:
            res[-1] = [res[-1][0]]

    return res


arr = [2,2,3,4,5, 5,5,7,7,8,10,10,10]
print(main(arr))