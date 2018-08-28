"""
Create a function that takes a list of numbers 
and returns a list where each number is the sum of 
itself + all previous numbers in the list.
"""

def cumulative_sum(lst):
  return [sum(lst[:i+1]) for i in range(len(lst))]
