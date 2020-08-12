
"""##Longest Substring with K Distinct Characters (medium)

### Problem statement
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
"""

''' Time 0 (n) , Space: 0(k)
e.g. 
     a r a a c i    ss, max_ss , dist_char (<=2)
     i j            2   2         [a,r]
     i   j          3   3         [a,r]
     i     j        4   4         [a,r]
     i       j      5   4         [a,r,c]
       i     j      4   4         [a,r,c]   start to shrink
         i   j      3   4         [a,c]     still k > 2
         i      j   4   4         [a,c,i]   start to shrink
           i    j



'''
def longest_substring_with_k_distinct(str, k):
    if k>len(str):
        return -1
    else:
        i =0     # starting 
        # j = 1    
        # dist_char = {str[i]:1,str[j]:1}      # have to assign str[j]:1 or else never visit the first j 
        max_ss = 0
        dist_char = {}
        print ("k=",k)
        for j in range(len(str)):           # ending
            if str[j] not in dist_char:
                dist_char[ str[j] ]  = 0     # add new string
            dist_char[ str[j] ] += 1         # update frequency          
            # start to shrink        :       # find largest substring ending at j
            while len ( dist_char) >k:                           
                dist_char[ str[i] ] -= 1      # update frequency  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if dist_char[ str[i] ]  == 0: # delete 0 frequent onese
                    del  dist_char[ str[i] ] 
                i += 1
            max_ss = max(max_ss , j - i + 1) 

        return max_ss

def main():
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()
