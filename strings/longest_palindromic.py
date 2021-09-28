import unittest

def longestPalindrome(s):
    if len(s) == 1:
        return s
    longest_palindrome = s[0]
    for i in range(len(s)-1):
        pointer_one = i - 1
        pointer_two = i + 1
        # check if middle value
        if pointer_one < 0 or pointer_two >= len(s):
            pass
        elif s[pointer_one] == s[pointer_two]:
            while pointer_one >= 0 and pointer_two < len(s) and s[pointer_one] == s[pointer_two] :
                if len(s[pointer_one:pointer_two+1]) > len(longest_palindrome):
                    longest_palindrome = s[pointer_one:pointer_two+1]
                pointer_one -= 1
                pointer_two += 1

        # check if first of even 
        pointer_one = i
        pointer_two = i + 1
        # check if middle value
        if pointer_one < 0 or pointer_two >= len(s):
            pass
        elif s[pointer_one] == s[pointer_two]:
            while pointer_one >= 0 and pointer_two < len(s) and s[pointer_one] == s[pointer_two]:
                if len(s[pointer_one:pointer_two+1]) > len(longest_palindrome):
                    longest_palindrome = s[pointer_one:pointer_two+1]
                pointer_one -= 1
                pointer_two += 1

    return longest_palindrome


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longestPalindrome('babad'), 'bab')
        self.assertEqual(longestPalindrome('cbbd'), 'bb')
        self.assertEqual(longestPalindrome('a'), 'a')
        self.assertEqual(longestPalindrome('ac'), 'a')


if __name__ == '__main__':
    unittest.main()
