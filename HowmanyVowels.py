"""
Create a function that takes a string and 
returns the number (count) of vowels contained 
within it
"""
def count_vowels(txt):
	return sum([1 for x in txt.lower() if x in 'aeiou'])
