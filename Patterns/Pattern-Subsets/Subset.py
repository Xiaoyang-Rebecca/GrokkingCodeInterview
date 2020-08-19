'''
i   []
0   [] [1]
1   [] [1] [3] [1,3]
'''
def find_subsets(nums):
  subsets = []
  subsets.append([])
  for ele in  nums:
    # ls = 2 * ls        
    level_width = len(subsets)
    for ni in range(level_width):
      new_node = list( subsets[ni] )
      new_node.append(ele)
      subsets.append( new_node )

  print(subsets)
      


  

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  # print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

#%%
s = "a"
s.upper()

# %%
s.isupper()

# %%
a = "1"
a.isupper()

# %%
