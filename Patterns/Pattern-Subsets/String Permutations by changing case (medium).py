'''
MEthod2
'''
def letterCasePermutation(self, S):
    """
    :type S: str
    :rtype: List[str]
    """
    if len(S) ==0:
        return [S]
    
    result = [S]
    for i,s  in enumerate(S):
        if s.isalpha():
            width = len (result)
            s_p = s.upper() if s.islower() else s.lower()  # permutated case
            for ni in range (width):
                new = result[ni]                           # new node
                new = new[:i] + s_p + new[i+1:]
                result.append (new)
    return result
    
'''
MEthod1
'''

def find_letter_case_string_permutations(str):
    S= str
    if len(S) <=1:
        return [S]
    
    result = []
    letter_ids = []
    for i, s in enumerate(S):
        if s.isnumeric() == False:
            letter_ids.append(i)
            
    print ("letter_ids=",letter_ids)
    subsets = []
    subsets.append([])
    for letter_id in letter_ids:
        width = len (subsets)
        for ni in range(width):
            new_node = list(subsets[ni])
            new_node.append(letter_id)
            subsets.append(new_node)

            # Generate Uppper/lower case:
            upper_s = S
            for i in new_node:
                s = upper_s[i]
                s_p = s.upper() if s.islower() else s.lower()
                upper_s = upper_s[:i] + s_p + upper_s[i+1:]
            
            result.append(upper_s)
    
    return result
  
  # find all subset of 



def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
