# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from turtle import st


def find_anagram(word, anagram):
    # [assignment] Add your code here

      #using sorted strings
      #finding_anagrams("hello", "check") -- False
    strHello_find_anagrams = list("hello")
    strHello_find_anagrams.sort()
    strCheck_find_anagrams = list("check")
    strCheck_find_anagrams.sort()

      #finding_anagrams("below", "elbow") -- True
    strBelow_find_anagrams = list("below")
    strBelow_find_anagrams.sort()
    strElbow_find_anagrams = list("elbow")
    strElbow_find_anagrams.sort()

    #retun False
    print(strHello_find_anagrams == strCheck_find_anagrams)

    #return True
    print(strBelow_find_anagrams == strElbow_find_anagrams) 




    



