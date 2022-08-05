import numpy as np
import pandas as pd
from itertools import permutations

def permutation(lst):
  if len(lst) == 0:
      return []

  if len(lst) == 1:
      return [lst]


  l = [] 

  # Iterate the input(lst) and calculate the permutation
  for i in range(len(lst)):
      m = lst[i]
      remLst = lst[:i] + lst[i+1:]

      for p in permutation(remLst):
          l.append([m] + p)
  return l
 
#   As input features after updating weights
list1=['0.3','0.4','0.1','0.1','0.1']
l2=(permutation(list1))
mySet = set()

for j in range(len(l2)):
  mySet = mySet | set([tuple(l2[j])])

