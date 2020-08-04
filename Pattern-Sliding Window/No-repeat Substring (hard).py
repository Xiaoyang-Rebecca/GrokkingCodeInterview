

"""## No-repeat Substring (hard)

### Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""

''' Time: 0(n), space 0(unique(str))
    aabccbb  len max_len dist
    ij        2   1       [a:1]
     ij       2   2       [a:1,b:1]
     i j      3   3       [a:1,b:1,c:1]
     i  j     4   3       [a:1,b:1,c:2]  move
        ij    2   3       [c:1,b:1]      

'''
def non_repeat_substring(str):
    dist = {}
    j = 0
    max_len = 0
    while j < len(str):
        if str[j] not in dist:
            dist[ str[j]  ] =0
        dist[ str[j]  ] +=1
        max_len = max(max_len,len(dist))
        if dist[ str[j]  ] > 1:  # replicate element found
            dist = {}            # reset dist
            dist[str[j] ] = 1
        j+=1
    return   max_len

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()