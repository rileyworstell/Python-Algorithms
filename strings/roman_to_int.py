

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    pointer = 0
    answer = 0
    while pointer < len(s):
        answer += roman_dict[s[pointer]]
        if pointer != len(s) - 1:
            if s[pointer] == 'I' and (s[pointer+1] == 'V' or s[pointer+1] == 'X'):
                answer += roman_dict[s[pointer+1]]
                answer -= 2
                pointer += 1
            elif s[pointer] == 'X' and (s[pointer+1] == 'L' or s[pointer+1] == 'C'):
                answer += roman_dict[s[pointer+1]]
                answer -= 20
                pointer += 1
            elif s[pointer] == 'C' and (s[pointer+1] == 'D' or s[pointer+1] == 'M'):
                answer += roman_dict[s[pointer+1]]
                answer -= 200
                pointer += 1
        pointer += 1
    return answer


roman = 'III'
roman = 'LVII'
# roman = 'MCMXCIV'
print(roman_to_int(roman))
