# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


import this
from turtle import st


def find_anagram(word, anagram):
    # [assignment] Add your code here

      #using sorted strings
      #finding_anagrams("hello", "check") -- False
    strHello_find_anagrams = list("hello")
    strHello_find_anagrams.sort()
    strCheck_find_anagrams = list("check")
    strCheck_find_anagrams.sort() 

    if list("Hello") == list("check"):
      return True
    else:
      return False
      print(find_anagram("hello", "check"))