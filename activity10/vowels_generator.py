#!/usr/bin/env python3

def vowels_in_str( word ):
  vowels = ['a','e','i','o','u'] 
  for letter in word: 
    if letter.lower() in vowels:
      yield letter 
        

# Use the generator 
for i in vowels_in_str("Johanna"): 
    print(i) 


