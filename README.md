# Immerse Education Project

## Goal of the project

The goal is to write a little Python package of file compression, providing two functions: `Huffman_encode(input_file)` and `Huffman_decode(encoded_file)`. 

The user will provide a local text file that they want to compress/uncompress. 
We could even store the compressed files in a SQLite database, in a more advanced version (to get some training with databases). 


## Sorting algorithms
* By sorting a certain list, it would be easier to process the information provided by the user.
* In our case, the list would definitely need to be sorted, because the Huffman theory is that a continuous repetition of the 2 least frequent characters in the string are merged together, so that it would end up with only one string and a frequency. This will be at the root of the tree. 
* It is also possible to give conditions while sorting the list 
  ***i.e. ascending or descending order, sorting alphabetically, etc.***

~ It is IMPOSSIBLE to sort a dictionary, because in a dictionary, the order doesn't matter. 
### Bubble Sort
↠↠ Continously swapping with the element to the right if they are in the wrong place. this can vary based on the rule (the condition), where it is sorting in ascending or descending order, etc. 
↠↠ They only sort things one at a time????????????
##### *** EXAMPLE : ***
This is the first "analysis" and sorting of the numbers give. This example will be sorted in ASCENDING ORDER
```
First Sorting:
( 5 1 4 2 8 ) –>  (1 5 4 2 8 ) Swap 1 & 5, because 5 > 1
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ) Swap 5 & 4, because 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ) Swap 5 & 2, because 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) The final 2 elements , 5 and 8 are in order where 5 is before 8. Thus the bubble sort won't swap them anymore.
```
##### *** However, these number still aren't in the right ascending order. Therefore, we would need to sort them AGAIN. *** #####
```
Second Sorting:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ) Swap 4 & 2, because 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
```
##### *** At last, we can see that the elemnts are sorted properly. But the sorting algortihm will need to run once more, to make sure and prove that there aren't any elements our of place. *** #####

```
Third Sorting:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
```
##### *** At last, we can see that the elemnts are sorted properly. But the sorting algortihm will need to run once more, to make sure and prove that there aren't any elements our of place. *** #####
### Merge Sort

### Comparison


## Huffman coding
##### *** IDEA : ***
The more frequent a character is, the shorter its Huffman encoding, because it's going to appear more times
##### *** AIM : ***
The aim is to be able to take a string provided by the user and compress the provided string. 
##### *** Steps on how to do it (in English): ***
1. Take the `string` provided by the user and treat it as an input value. 
2. Calculate the frequency of each character in the `string`, and store it in a dictionary.
3. Sort the dictionary() according to its second element (the frequency) in descending          order. 
4. Create another dicitonary for the trees, where the frequency isn't represented visually    (the frequency information will be obtained from the original dictionary)
5. Create a function to merge the frequencies(value) and the character (to form a string),    ONLY OF THE LAST 2 ELEMENTS (least frequent elements), and add them back to the            dicitonary. 
6. Sort the dicitonary once again with the newly merged string(key) and frequency(value). 
7. Create another function to merge the trees beased on the information obtained in the       function merging the frequencies.
8. Create a `while` loop, where if there is more than one string and value (couple), the        process of merging the frequencies (the funtion), will continue. This will be              continuous until there is only 1 couple left in the dicitonary.
9. Inside the while loop, we would also need to pop off keys in the dictionary containing     the final trees. Popping off the keys(the merged string, NOT ALL AT ONCE), would allow     us to see the value of each individual character. This would help the overall Huffman      `function` to use this information(the frequency from the popped keys) to form the           Huffman tree. 
10. 

##### *** Implementation (example) : ***
```python

from collections import OrderedDict
# importing an ordered dictionary from the python library. 
string = "computer science is the study of computers and computational systems"

'''
asking_the_user_for_the_string = input("Please paste the text file that you would like me to compress.")
#somehow attach a variable to the user's answer and name it as string!
'''


def get_encoding(tree, character):
  '''
  Return the Huffman encoding of a character based on a Huffman tree  
  '''
  return None


def Huffman(string):
  frequencies_dict = OrderedDict(sorted([(i, string.count(i)) for i in set(string)], key=lambda couple: couple[1], reverse=True))
  # Anonymous function (lambda): A function which takes the second element of the function and sort it according to the second element. 
  # couple is the brackets list (character, frequency)
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

  # while frequency dictionary has more than one element, pop the last 2 elements and merge them, and add them back to the list. 
  while len(frequencies_dict) > 1:
    # tuple1 looks like ("abc", freq_abc)
    tuple1, tuple2 = frequencies_dict.popitem(), frequencies_dict.popitem()
    label1, freq1 = tuple1
    label2, freq2 = tuple2
    
    # Merge frequencies
    new_label, new_freq = merge_frequencies(tuple1, tuple2)
    frequencies_dict[new_label] = new_freq

    list_frequencies_sorted = sorted(frequencies_dict.items(), key=lambda couple: couple[1], reverse=True) # sorting the list

    frequencies_dict = OrderedDict(list_frequencies_sorted)
    
    # Merge trees
    # del dict["key"] OR dict.pop("key", None)
    tree1 = trees_dict.pop(label1, None)
    tree2 = trees_dict.pop(label2, None)
    print(tree1, tree2)
    # This is to retrieve the value but getting rid of the key
    # Essentially, getting rid of the character to obtain the frequency so we can use this information to let the computer to know how to arrange the characters in the Huffman tree. 
    
    merge_trees(new_label, tree1, tree2)
    
    # tree1, tree2 = trees_dict["abc"], trees_dict["def"]
    
  # Get the whole Huffman tree

  return (new_label)

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
* A heap is a *** COMPLETE BINARY TREE ***
* In binary heaps, there are 2 types of heaps :
1. Min heap
2. Max heap

#### *** Minimum Binary Heap *** ####
In a min heap, the root of the tree (the most top) is the MINIMUM number/frequency of character appearance amongst the other elements. 
#### *** Maximum Binary Heap *** ####
In a max heap, the internal nodes are always either greater than or is equal to the values of the children of the said internal node.



