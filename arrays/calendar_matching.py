
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    a, b = parseNumber(dailyBounds1[0])
    c, d = parseNumber(dailyBounds1[1])
    dailyBounds1[0] = (a*60) + b
    dailyBounds1[1] = (c*60) + d
    a, b = parseNumber(dailyBounds2[0])
    c, d = parseNumber(dailyBounds2[1])
    dailyBounds2[0] = (a*60) + b
    dailyBounds2[1] = (c*60) + d
    totalBounds = [max(dailyBounds1[0], dailyBounds2[0]), min(dailyBounds1[1], dailyBounds2[1])]
    if calendar1 == [] and calendar2 == []:
        returnValue = convertToStringTime(totalBounds)
        return [returnValue]
    for i in range(len(calendar1)):
        a, b = parseNumber(calendar1[i][0])
        c, d = parseNumber(calendar1[i][1])
        calendar1[i][0] = (a*60) + b
        calendar1[i][1] = (c*60) + d
    for i in range(len(calendar2)):
        a, b = parseNumber(calendar2[i][0])
        c, d = parseNumber(calendar2[i][1])
        calendar2[i][0] = (a*60) + b
        calendar2[i][1] = (c*60) + d
    calendar = calendar1 + calendar2
    calendar = mergeOverlap(calendar)
    arr = []
    if totalBounds[0] < calendar[0][0]:
        if calendar[0][0] - totalBounds[0] >= meetingDuration:
            arr.append([totalBounds[0], calendar[0][0]])
    for i in range(len(calendar)-1):
        if calendar[i+1][0] - calendar[i][1] >= meetingDuration:
            arr.append([calendar[i][1], calendar[i+1][0]])
    if totalBounds[1] > calendar[-1][1]:
        if totalBounds[1] - calendar[-1][1] >= meetingDuration:
            arr.append([calendar[-1][1], totalBounds[1]])
    if len(arr) > 0 and totalBounds[0] > arr[0][0]:
        arr.pop(0)
    for i in range(len(arr)):
        arr[i] = convertToStringTime(arr[i])
    return arr



def convertToStringTime(items):
    left = ''
    right = ''
    left = str(items[0]//60) + ':' + str(items[0]%60)
    right = str(items[1]//60) + ':' + str(items[1]%60)
    if left[-2] == ":":
        left += "0"
    if right[-2] == ":":
        right += "0"
    return [left, right]


def mergeOverlap(calendar):
    calendar.sort(key= lambda x: x[0])
    i = 0
    while i < len(calendar)-1:
        if calendar[i][1] > calendar[i+1][0]:
            calendar[i] = [min(calendar[i][0], calendar[i+1][0]), max(calendar[i][1], calendar[i+1][1])]
            calendar.pop(i+1)
        else:
            i += 1
    return calendar

    
            

def parseNumber(date):
    if date[2] == ":":
        return int(date[0:2]), int(date[3:])
    else:
        return int(date[0:1]), int(date[2:])
    


calendar1 = [
    ["7:00", "7:45"],
    ["8:15", "8:30"],
    ["9:00", "10:30"],
    ["12:00", "14:00"],
    ["14:00", "15:00"],
    ["15:15", "15:30"],
    ["16:30", "18:30"],
    ["20:00", "21:00"]
  ]
calendar2 = [
["9:00", "10:00"],
["11:15", "11:30"],
["11:45", "17:00"],
["17:30", "19:00"],
["20:00", "22:15"]
]
dailyBounds1 = ["6:30", "22:00"]
dailyBounds2 = ["8:00", "22:30"]
meetingDuration= 30

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))

