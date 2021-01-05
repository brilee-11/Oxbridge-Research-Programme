# Immerse Education Project

## Goal of the project

The goal is to write a little Python package of file compression, providing two functions: `Huffman_encode(input_file)` and `Huffman_decode(encoded_file)`. 

The user will provide a local text file that they want to compress/uncompress. 
We could even store the compressed files in a SQLite database, in a more advanced version (to get some training with databases). 


## Sorting algorithms

### Bubble Sort

### Merge Sort

### Comparison


## Huffman coding
##### *** IDEA : ***
The more frequent a character is, the shorter its Huffman encoding, because it's going to appear more times
##### *** AIM : ***
The aim is to be able to take a string provided by the user and compress the provided string. 
##### *** Steps on how to do it (in English): ***
1. Take the string provided by the user and treat it as an input value. 
2. Calculate the frequency of each character in the string.
3. Arrange/sort the characters in order of least frequent to the most frequent. 
4. Create a function which has the properties to make a Huffman Tree. 

##### *** Implementation (example) : ***
```python

from collections import OrderedDict
# importing an ordered dictionary from the python library. 
string = "computer science is the study of computers and computational systems"

# Anonymous function (lambda): A function which takes the second element of the function and sort it according to the second element. 
# couple is the brackets list (character, frequency)

def get_encoding(tree, character):
  '''
  Return the Huffman encoding of a character based on a Huffman tree  
  '''
  return None


def Huffman(string):
  frequencies_dict = OrderedDict(sorted([(i, string.count(i)) for i in set(string)], key=lambda couple: couple[1], reverse=True))

# What this does is that it sorts the set of the string(so no characters) are repeated, and it is reversing the order so that it is sorted based on the second element in the couple and in descending order. 

  # trees_dict = {'a': ["a"],  'c': ["c"]}
  trees_dict = {i:[i] for i in set(string)}

  # In frequencies_dict:
  # "ac" ↦ freq_a + freq_c   # (key/label ↦ value)

  # In trees_dict? 
  # "ac" ↦ ["ac", ["a"], ["c"]]
    
  def merge_frequencies(tuple1, tuple2):
    # Way to use it:
    # t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
    # merge_frequencies(t1, t2)
    return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])

  # label = name of the root of the tree
  # function merge_trees takes labels as arguments
  def merge_trees(new_label, tree1, tree2):
    return [new_label, tree1, tree2]


  while len(frequencies_dict) > 1:
    # tuple1 looks like ("abc", freq_abc)
    tuple1, tuple2 = frequencies_dict.popitem(), frequencies_dict.popitem()
    label1, freq1 = tuple1
    label2, freq2 = tuple2

    # Merge frequencies
    new_label, new_freq = merge_frequencies(tuple1, tuple2)
    frequencies_dict[new_label] = new_freq

    list_frequencies_sorted = sorted(frequencies_dict.items(), key=lambda couple: couple[1], reverse=True)
    #sorting the list again

    frequencies_dict = OrderedDict(list_frequencies_sorted)
    
    # Merge trees
    # del dict["key"] OR dict.pop("key", None)
    tree1 = trees_dict.pop(label1, None)
    tree2 = trees_dict.pop(label2, None)
    # This is to retrieve the value but getting rid of the key
    
    merge_trees(new_label, tree1, tree2)
        
    
    # tree1, tree2 = trees_dict["abc"], trees_dict["def"]
    
  # Get the whole Huffman tree

  return None

```

## Useful data stuctures

### Dictionaries
A dictionary is a data structure (a bit like a list or an array) where you can associate values to certain keys. For example, an array can be seen as dictionary, where the keys are always natural numbers: 

```python
my_array = ["value 1", "value 2"]
```
↠↠ my_array[0] is "value 1", and my_array[1] is "value 2": 
↠↠ ie. the key 0 is associated to the value "value 1" (written 0 ⟼ "value 1"), and the key 1 is associated to "value 2" (written 1 ⟼ "value 2")

#### *** How to use it? *** ####
 ```python
 my_dict = {} 
 ```
 Empty dictionary: no keys, no values
 But, you can add a new "key" ⟼ "value" pairing (a value can be anything, but a key can only _immutable_ (we'll talk about it next time: that is, something that has a certain value and can't be modified): for ex: a string, a number, a tuple, etc BUT NOT a list,an array, etc (because these can be modified):

#### *** In our case... *** ####
↠↠ We would like our keys to be the characters of our input_string, and not just integers. 
↠↠ For example, we'd like to associate to the key "H" (the encoded character) the value "101" (the corresponding Huffman code): "H" ⟼ "101"
A dictionary is EXACTLY the data structure that enables us to do that! (In a way, it's a function, where the domain is finite: to each key, you associate a value, but you have a finite number of keys)

### Binary heaps

## I/O in Python


