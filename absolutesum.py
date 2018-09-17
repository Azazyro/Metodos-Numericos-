"""
Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
"""

def get_abs_sum(nums):
  return sum(map(abs, nums))
