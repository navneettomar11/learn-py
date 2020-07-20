from typing import List

"""
    Reverse words
"""
def reverse_words(s: str) -> str:
    sarr = s.split(" ")
    sarr = list(filter(lambda s: s!='', sarr[:: -1]))
    res = ' '.join(sarr)
    return res

"""
    Reverse String - Leetcode 344
"""
def reverse_string(s: List[str]) -> None :

    def helper(s: List[str], start: int, end: int):
        if start >= end:
            return
        s[start] = s[start] + s[end]
        s[end] = s[start][0]
        s[start] = s[start][-1]
        helper(s, start+1, end-1)

    helper(s, 0,len(s)-1)

"""
    Backspace Compare - Leetcode 844
"""
def backspace_compare(s:str, t: str) -> bool :
    sstk = []
    tstk = []

    for ch in s:
        if ch == '#':
            if len(sstk) > 0: sstk.pop()
        else:
            sstk.append(ch)

    for ch in t:
        if ch == '#':
            if len(tstk) > 0: tstk.pop()
        else:
            tstk.append(ch)

    return "".join(sstk) == "".join(tstk)


"""
    Reverse Vowels -> Leetcode - 345
"""
def reverse_vowels(s: str) -> str:
    start, end = 0, len(s)-1
    vowels = ['a', 'e', 'i', 'o', 'u']
    is_vowel = lambda x: x.lower() in vowels
    while start < end:

        if is_vowel(s[start]) and is_vowel(s[end]):
            #s = s[:start]+s[end]+s[start:]
            s = s[:start]+s[end]+s[start+1:end]+s[start]+s[end+1:]
            #print(s,'----Before start' ,s[:start],'End: ', s[end],'Start +1 to end: ', s[start+1:end] ,'Start: ',s[start], 'End to str end: ',s[end+1:], '-----', start, end)
            start+=1
            end-=1

        if not is_vowel(s[start]):
            start+=1
        if not is_vowel(s[end]):
            end-=1

    return s

"""
Long pressed name - Leetcode - 925
"""
def long_pressed_name(name: str, typed: str) -> bool :
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i+=1
        elif j == 0 or typed[j] != typed[j-1]:
            return False
    return i == len(name)


"""
 Valid Palindrome - Leetcode - 125
"""
def is_plaindrome_2(s: str) -> bool :
    s = ''.join([c.lower() for c in s if c.isalnum()])
    reverse = ''.join(reversed(s))
    if s == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    #print(reverse_words('a good   example'))
    #s = ['h','e', 'l', 'l', 'o']
    #reverse_string(s)
    #print(s)

    #print(backspace_compare('ab#c', 'ad#c')) # True
    #print(backspace_compare('ab##', 'c#d#')) # True
    #print(backspace_compare('a##c', '#a#c')) # True
    #print(backspace_compare('a#c', 'b')) # False
    #print(backspace_compare("y#fo##f","y#f#o##f")) # True

    #print(reverse_vowels("hello")) #holle
    #print(reverse_vowels("leetcode")) #leotcede
    #print(reverse_vowels("navneet")) #nevneat
    #print(reverse_vowels("aA")) # Aa

    #print(long_pressed_name("alex", "aaleex")) # True
    #print(long_pressed_name("saeed", "ssaaed")) # False
    #print(long_pressed_name("leelee", "lleeelee")) # True
    #print(long_pressed_name("laiden", "laiden")) # True
    #print(long_pressed_name("alex","alexxr")) #False

    print(is_plaindrome_2("A man, a plan, a canal: Panama"))
    print(is_plaindrome_2("race a car"))
