from collections import deque

class Solution:
    def find_even_length_palindrome_string(s: str):
        result = ''
        short_palindromes = []
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                short_palindromes.append((i, i + 1))

        for palin in short_palindromes:
            palindrome = ''
            i, j = palin
            q = deque([i, j])
            while i > 0 and j < len(s) - 1 and s[i - 1] == s[j + 1]:
                i, j = i - 1, j + 1
                q.appendleft(i)
                q.append(j)

            if len(result) < len(q):
                while q:
                    palindrome += s[q.popleft()]
                result = palindrome

        return result


    def find_odd_length_palindrome_string(s: str):
        result = ''
        short_palindromes = []

        for i in range(0, len(s) - 2):
            if s[i] == s[i + 2]:
                short_palindromes.append((i, i + 1, i + 2))

        for palin in short_palindromes:
            palindrome = ''
            i, j = palin[0], palin[2]
            q = deque([i, palin[1], j])

            while i > 0 and j < len(s) - 1 and s[i - 1] == s[j + 1]:
                i, j = i - 1, j + 1
                q.appendleft(i)
                q.append(j)

            if len(result) < len(q):
                while q:
                    palindrome += s[q.popleft()]
                result = palindrome

        return result

    def longestPalindrome(self, s: str) -> str:
        odd_palindrome = self.find_odd_length_palindrome_string(s)
        even_palindrome = self.find_even_length_palindrome_string(s)
        if len(odd_palindrome) == 0 and len(even_palindrome) == 0:
            return s[0]

        if len(odd_palindrome) > len(even_palindrome):
            return odd_palindrome
        else:
            return even_palindrome