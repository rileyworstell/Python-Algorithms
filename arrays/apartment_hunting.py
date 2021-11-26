
# Time O(nm) | Space (O(nm))
def apartmentHunting(blocks, reqs):
    building_distances = [[0 for _ in blocks] for _ in reqs]
    for i in range(len(reqs)):
        cur = None
        for j in range(len(blocks)):
            if blocks[j].get(reqs[i]) == True:
                cur = 0
            elif cur != None:
                cur += 1
            building_distances[i][j] = cur
    for i in reversed(range(len(reqs))):
        cur = None
        for j in reversed(range(len(blocks))):
            if blocks[j].get(reqs[i]) == True:
                cur = 0
            elif cur != None:
                cur += 1
            if building_distances[i][j] is not None and cur is not None:
                if building_distances[i][j] > cur:
                    building_distances[i][j] = cur
            elif building_distances[i][j] is None and cur is not None:
                building_distances[i][j] = cur
    lowest_req = float('inf')
    idx = -1
    for j in range(len(blocks)):
        cur_min = float('-inf')
        for i in range(len(reqs)):
            cur_min = max(cur_min,building_distances[i][j])
        if cur_min < lowest_req:
            lowest_req = cur_min
            idx = j


    return idx                




blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },    
    {
        "gym": False,
        "school": True,
        "store": True
    },
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs)) # 3