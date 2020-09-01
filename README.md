# GrokkingCodeInterview


The solution for ["Educative.io/Grokking the Coding Interview: Patterns for Coding Questions"](https://www.educative.io/courses/grokking-the-coding-interview) and their related [Leetcode](https://leetcode.com/) solutions
* The number ID correspond to the leetcode id

Study use only
contact: Xiaoyang.rebecca.li@gmail.com


## Pattern: Sliding Window
* [Maximum Sum Subarray of Size K (easy)](./Patterns/Pattern-Sliding%20Window/Maximum%20Sum%20Subarray%20of%20Size%20K%20(easy).py)
* [Smallest Subarray with a given sum (easy)](./Patterns/Pattern-Sliding%20Window/Smallest%20Subarray%20with%20a%20given%20sum%20(easy).py)
* [Longest Substring with K Distinct Characters (medium)](./Patterns/Pattern-Sliding%20Window/Longest%20Substring%20with%20K%20Distinct%20Characters%20(medium).py)
* [Longest Subarray with Ones after Replacement (hard)](./Patterns/Pattern-Sliding%20Window/Longest%20Subarray%20with%20Ones%20after%20Replacement%20(hard).py)
* [Longest Substring with Same Letters after Replacement (hard).py](./Patterns/Pattern-Sliding%20Window/Longest%20Substring%20with%20Same%20Letters%20after%20Replacement%20(hard).py)
* [No-repeat Substring (hard).py](./Patterns/Pattern-Sliding%20Window/No-repeat%20Substring%20(hard).py)
## Pattern: Two Pointers

## Pattern: Merge Intervals
```
   ## Time O(N*logN)  (   O(N*logN) for sorting +O(N) for merging )


```
* [Merge Intervals (medium)](./Patterns/Pattern-Merge%20Intervals/Merge%20Intervals%20(medium).py)
  


## Pattern: Tree Breadth First Search

```
  ## Space O(w), where ‘W’ is the maximum number of nodes on any level.

  ls =[root]                            # queue: storage the node  in breadth first order
  while len(ls) > 0:
    level_width = len(ls)              # the width of the current level
    for i in range(level_width):
      n = ls.pop(0)         # pop
      ls.append( n.left )           # push left
      ls.append( n.right )          # push right
    
    ** Breath level caluclation

```
* [Binary Tree Level Order Traversal (easy)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Binary%20Tree%20Level%20Order%20Traversal%20(easy).py)
* [Reverse Level Order Traversal (easy)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Reverse%20Level%20Order%20Traversal%20(easy).py)
* [Zigzag Traversal (medium)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Zigzag%20Traversal%20(medium).py)
  - [103. Binary Tree Zigzag Level Order Traversal](./Leetcode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal.py)
  - [281. Zigzag Iterator](./Leetcode/281.%20Zigzag%20Iterator.py)
* [Level Averages in a Binary Tree (easy)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Level%20Averages%20in%20a%20Binary%20Tree%20(easy).py)  
  - [637. Average of Levels in Binary Tree](./Leetcode/637.%20Average%20of%20Levels%20in%20Binary%20Tree.py)
  - [1161. Maximum Level Sum of a Binary Tree](./Leetcode/1161.%20Maximum%20Level%20Sum%20of%20a%20Binary%20Tree.py)
* [Minimum Depth of a Binary Tree (easy)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Minimum%20Depth%20of%20a%20Binary%20Tree%20(easy).py)
* [Level Order Successor (easy)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Level%20Order%20Successor%20(easy).py)
* [Connect Level Order Siblings (medium)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Connect%20Level%20Order%20Siblings%20(medium).py)

* [Connect All Level Order Siblings (medium)](./Patterns/Pattern-Tree%20Breadth%20First%20Search/Connect%20All%20Level%20Order%20Siblings%20(medium)%20.py)
* []
  * [199. Binary Tree Right Side View](./Leetcode/199.%20Binary%20Tree%20Right%20Side%20View.py)
  
## Pattern: Tree Depth First Search
```
   ## Time O(N)  Space O (H),
    (H)egiht of the tree, (N)umber of nodes

```
* [Binary Tree Path Sum (easy)](./Patterns/Pattern-Tree%20Depth%20First%20Search/Binary%20Tree%20Path%20Sum%20(easy).py)
  * [112. Path Sum](./Leetcode/112.%20Path%20Sum.py)
* [All Paths for a Sum (medium)]
  * [113. Path Sum II ](./Leetcode/113.%20Path%20Sum%20II.py)
* [Sum of Path Numbers (medium)](./Patterns/Pattern-Tree%20Depth%20First%20Search/Sum%20of%20Path%20Numbers%20(medium).py)
* [Count Paths for a Sum (medium)](./Patterns/Pattern-Tree%20Depth%20First%20Search/Count%20Paths%20for%20a%20Sum%20(medium).py)
  * [437. Path Sum III](./Leetcode/437.%20Path%20Sum%20III.py)

## Patter: Subset
```
   ## Time O(2^N)  Space O (^N)
        0               []                    e.g GivenSet[1,5,3]
                    copy    add 1
        1           []   |  [1]
                   Copy     add 5
        2         [][1]  |  [5] [1,5]
                   copy     add 3
        3  [][1][5][1,5] |  [3][1,3][5,3][1,5,3]

```
* [Subset](./Patterns/Pattern-Subsets/Subset.py)
  - [78. Subsets](./Leetcode/78.%20Subsets.py)
* [Subsets With Duplicates (easy)](./Patterns/Pattern-Subsets/Subsets%20With%20Duplicates%20(easy).py)
  - [90. Subsets II](./Leetcode/90.%20Subsets%20II.py)
* [Permutations (medium)](./Patterns/Pattern-Subsets/Permutations%20(medium).py)
  - [46. Permutations](./Leetcode/46.%20Permutations.py)
  - [47. Permutations](./Leetcode/47.%20Permutations%20II.py)
* [String Permutations by changing case (medium)](./Patterns/Pattern-Subsets/String%20Permutations%20by%20changing%20case%20(medium).py)
  - [784. Letter Case Permutation](./Leetcode/784.%20Letter%20Case%20Permutation.py)
* [Balanced Parentheses (hard)](./Patterns/Pattern-Subsets/Balanced%20Parentheses%20(hard).py)
  - [22. Generate Parentheses.py](./Leetcode/22.%20Generate%20Parentheses.py)


## Pattern: Binary Search
```
   ## Time O(logN)  Space O (1)
   while l <=r:            #    l ,r = 0, n-1
      m = (l+r)//2
      if too small:   r = m -1
      elif too big:  l = m +1

```
* [Order-agnostic Binary Search (easy)](./Patterns/Pattern-binary%20search/Order-agnostic%20Binary%20Search%20(easy).py)
* [Ceiling of a Number (medium)](./Patterns/Pattern-binary%20search/Ceiling%20of%20a%20Number%20(medium).py)
* [Number Range (medium)](./Patterns/Pattern-binary%20search/Number%20Range%20(medium).py)
  * [34. Find First and Last Position of Element in Sorted Array](./Leetcode/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.py)

* 
  * [540. Single Element in a Sorted Array](./Leetcode/540.%20Single%20Element%20in%20a%20Sorted%20Array.py)
* [Minimum Difference Element (medium)](./Patterns/Pattern-binary%20search/Minimum%20Difference%20Element%20(medium).py)
* 
## Twoheaps


  * [295. Find Median from Data Stream.py](./Leetcode/295.%20Find%20Median%20from%20Data%20Stream.py)
## Pattern-Top K element
```
   ## Time O(logK)  Space O ()
   Get largest  k -> minheap, in ascending order
   Get smallest k -> maxheap, in decending order
```
* [Top 'K' Numbers (easy)](./Patterns/Pattern-Top%20K%20element/Top%20'K'%20Numbers%20(easy).py)
  * [215. Kth Largest Element in an Array](./Leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array.py)
* [Kth Smallest Number (easy)](./Patterns/Pattern-Top%20K%20element/Kth%20Smallest%20Number%20(easy).py)
  * [347. Top K Frequent Elements.py](./Leetcode/347.%20Top%20K%20Frequent%20Elements.py)