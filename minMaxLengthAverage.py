"""
Create a function that takes a list of numbers and returns the following statistics:

    Minimum Value
    Maximum Value
    Sequence Length
    Average Value
"""

def minMaxLengthAverage(lst):
	return[min(lst), max(lst), len(lst), sum(lst)/len(lst)]
