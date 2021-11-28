
def minimumAreaRectangle(points):
    if points == []:
        return 0
    minArea = float('inf')
    maximum = float('-inf')
    for i in points:
        if i[0] > maximum:
            maximum = i[0]
    getHorizontals = [[] for _ in range(maximum+1)]
    for i in points:
        getHorizontals[i[0]].append(i)
    i = 0
    while i < len(getHorizontals):
        if getHorizontals[i] == []:
            getHorizontals.pop(i)
        else:
            getHorizontals[i].sort(key=lambda x: x[1])
            i += 1
    for i in range(len(getHorizontals)):
        for x in getHorizontals[i]:
            for y in getHorizontals[i]:
                if x != y and x[0] == y[0]:
                    pair = [x[1], y[1]]
                
                    for j in range(len(getHorizontals)):
                        if i != j:
                            for a in getHorizontals[j]:
                                for b in getHorizontals[j]:
                                    if a != b:
                                        if a[1] == pair[0] and b[1] == pair[1]:
                                            minArea = min(minArea, abs((pair[1] - pair[0]) * (b[0]-x[0])))
    if minArea == float('inf'):
        return 0
    return minArea


points = [
    [0, 0],
    [1, 1],
    [2, 2],
    [-1, -1],
    [-2, -2],
    [-1, 1],
    [-2, 2],
    [1, -1],
    [2, -2],
]

print(minimumAreaRectangle(points)) 
