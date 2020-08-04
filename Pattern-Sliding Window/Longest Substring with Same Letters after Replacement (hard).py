
"""## Longest Substring with Same Letters after Replacement (hard)

Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

'''
Time (0(n)) Space (1)
  "a a b c c b b"  len max_len dist (dist nonmax smaller than k=2)
  []                1  1       {a:1}
  [  ]              2  2       {a:2}
  [    ]            3  3       {a:2,b:1}
  [      ]          4  4       {a:2,b:1,c:1}
  [        ]        5  4       {a:2,b:1,c:2} shrink
    [      ]        4  4       {a:1,b:1,c:2} 
    [        ]      5  4       {a:1,b:2,c:2} shrink
      [      ]      4  4       {b:2,c:2}
'''
def check_replacement(dict):
  major_frequency = 0
  sum = 0
  for key in dict:
    major_frequency = max( major_frequency, dict[ key ] )
    sum += dict[ key ]
  return (sum-major_frequency)

def length_of_longest_substring(str, k):
  # TODO: Write your code here
  
  dict={}
  i=0
  major_frequency =  0
  max_len = 0
  for j in range(len(str)):
    if str[j] not in dict:
      dict[ str[j] ] = 0
    dict[ str[j] ] +=1
    major_frequency = max (major_frequency,dict[str[j]])
    if j-i+1 -major_frequency  > k:                       # it need to calcuate before and after the loop so put here its the best
      dict[ str[i] ] -= 1       
      if dict[ str[j] ] ==0:
        del dict[ str[j] ]        
      i+=1
    #   print (i,j ,dict, major_frequency)
    max_len = max(max_len, j-i+1 )
  return max_len


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()
