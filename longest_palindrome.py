
"""Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.
Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

def longest_palindrome (s):
    if len(s) == 0:
        return 0
    length = 1
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            word = s[i:j+1]
            reversed = word[::-1]
            if word == reversed:
                if length < len(word):
                    length = len(word)
            j += 1
        i += 1
    return length

