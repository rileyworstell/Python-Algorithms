"""
function takes in a non-empty string and returns its run-length encoding.
"""


def runLengthEncoding(string):
    answer = ''
    pointer = 1
    current = string[0]
    count = 1
    iterator = []
    while pointer <= len(string):
        if pointer == len(string):
            while count > 9:
                iterator.append(9)
                count -= 9
            iterator.append(count)
            for i in iterator:
                answer += (str(i) + current)
            iterator = []
            return answer
        if current != string[pointer]:
            while count > 9:
                iterator.append(9)
                count -= 9
            iterator.append(count)
            for i in iterator:
                answer += (str(i) + current)
            iterator = []
            current = string[pointer]
            count = 1
        elif string[pointer] == current:
            count += 1
        pointer += 1


string = "AAAAAAAAAABBCCCCD"
print(runLengthEncoding(string))
