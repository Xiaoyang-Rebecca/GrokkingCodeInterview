
"""## Merge Intervals (medium)

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
"""

'''
Time O(N*logN)  (   O(N*logN) for sorting +O(N) for merging )
    [2,4] [5,9]   [6,7]      
      p_i   c_i    m_i
    [2,4]  [5,9]  [2,4]
    [5,9]  [6,7]  [5,9]

'''

from __future__ import print_function
import numpy as np

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  merged = []
  # TODO: Write your code here
  # sort intervals starts
  starts = [ i.start for i in intervals]
  sorted_ids = np.argsort(starts)
  # start = intervals[sorted_id[0]].start  # guarantee : start <= i.start
  # end = intervals[sorted_id[0]].end
  p_i =  intervals[sorted_ids[0]] # previous interval    # guarantee : p_i.start <= c_i.start  
  for sorted_id in sorted_ids[1:]:
    c_i = intervals[sorted_id]
    if p_i.end < c_i.start:       # non over lap
      merged.append (p_i)         # push the previous interval
      p_i = c_i                   # update the next intervel as the other non-overlap interval
    else:                         # overlap have p_i.end >=c_i.start:
      m_i = Interval(p_i.start , max (c_i.end, p_i.end))          
      p_i = m_i                   # update the next intervel as the merged interval, might need further merge


 # add the last interval
  merged.append (p_i)
  return merged