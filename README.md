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
↠↠ This sorting algorithm takes the theory of DIVIDE AND CONQUER. 
↠↠ The merge sort divides the input into 2 and splits itself to tackle each algortihm. This cycle is continuous until the result only has 2 elelments of the inpts together. The "sort" part of this algortihm is where it rearranges the last 2 merged elements to its right condition. After this, it is going to rebuild the input, by merging with other merged elements. 

### Comparison of both sorting algortihms
The main comparison between the merge sort and the bubble sort, is that once the data or the input file gets larger,the time needed for bubble sort to fully work increases as well. 
This means that bubble sort is less efficient in terms of the time consumed to sort a large file, compared to the merge sort. The bubble sort has a linear time in sorting.

## Huffman coding
##### *** IDEA : ***
The more frequent a character is, the shorter its Huffman encoding, because it's going to appear more times
##### *** AIM : ***
The aim is to be able to take a string provided by the user and compress the provided string. 
##### *** Steps on how to do it (in English): ***
1. Take the `string` provided by the user and treat it as an input value. 
2. Calculate the frequency of each character in the `string`, and store it in a dictionary.
3. Sort the dictionary() according to its second element (the frequency) in descending order. 
4. Create another dicitonary for the trees, where the frequency isn't represented visually (the frequency information will be obtained from the original dictionary)
5. Create a function to merge the frequencies(value) and the character (to form a string), ONLY OF THE LAST 2 ELEMENTS (least frequent elements), and add them back to the dicitonary. 
6. Sort the dicitonary once again with the newly merged string(key) and frequency(value). 
7. Create another function to merge the trees beased on the information obtained in the function merging the frequencies.
8. Create a `while` loop, where if there is more than one string and value (couple), the process of merging the frequencies (the funtion), will continue. This will be continuous until there is only 1 couple left in the dicitonary.
9. Inside the while loop, we would also need to pop off keys in the dictionary containing the final trees. Popping off the keys(the merged string, NOT ALL AT ONCE), would allow us to see the value of each individual character. This would help the overall Huffman  `function` to use this information(the frequency from the popped keys) to form the Huffman tree. 
10. Then, we can assign the arguments in the function to merge the trees, according to the root of the tree, the left child, and the right child. 
11. After this, we need to write what would happen once the while loop ends. Essentially, when there is only 1 key left in the trees dictionary. 
12. Create a new `dictionary` that will hold the encodings of each character (key) in the string or in the trees dictionary.
13. Create a function where if the tree constructed has reached a leaf (only one key), we need to update the encoding dictionary. 
14. But if there is more than one key, then create an else statement where the divide and conquer algorithm will take place ; assigning the left tree with the encoding "0" and the right tree with the encoding "1"
(This else statement is basically keeping track of each character's encoding. Once it reaches another internal node, it will add the last tracked encoding and adding either a "1" or a "0" depending on its location. )
15. In this function we would then need to return the last remaining label in the trees dictionary.
16. In the overall Huffman function, the encoding dictionary will be the one needed to be returned, because the information that we want is the ENCODING OF ALL OF THE CHARACTERS IN THE INITIAL STRING.
17. (Since the aim is to get the user's string and compress it) Create a variable which asks the user for their text file, apply the overall function (Huffman) to it, and use it to make a new dictionary.
18.  Print a list comprehension that says, for every character in the string provided by the user, find it in the latest dictionary containing the encodings for the characters in the string provided, and print it. 

##### *** Implementation (example) : ***
```python

######################################
#            OFFICIAL WAY            #
######################################

from collections import OrderedDict
# importing an ordered dictionary from the python library. 



def Huffman(string):
  # Keys are mapped to Values
  # Keys have to be _immutable_ (ie not lists, dictionaries, sets, etc)
  # Labels (= keys) will be the strings that are the concatenated characters appearing in the corresponding partial Huffman tree

  set_string = set(string)
  # frequencies_dict: Labels are mapped to frequencies 
  frequencies_dict = OrderedDict(sorted([(i, string.count(i)) for i in set_string], key=lambda couple: couple[1], reverse=True))

  # Anonymous function (lambda): A function which takes the second element of the function and sort it according to the second element. 
  # couple is the brackets list (character, frequency)
  # What this does is that it sorts the set of the string(so no characters) are repeated, and it is reversing the order so that it is sorted based on the second element in the couple and in descending order. 



  # trees_dict: Labels are mapped to partial Huffman trees (represented by nested lists)
  # Ex: trees_dict = {'a': ["a"],  'c': ["c"]}
  trees_dict = {i:[i] for i in set_string}

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
    # tree1, tree2 = trees_dict["abc"], trees_dict["def"]
    # del dict["key"] OR dict.pop("key", None)
    tree1 = trees_dict.pop(label1, None)
    tree2 = trees_dict.pop(label2, None)

    # tree1 & tree2 are associated to the 2 labels that have the least frequencies (because they were the last elements of the ordered dictionary frequencies_dict)
    # This is to retrieve the value but getting rid of the key
    # Essentially, getting rid of the character to obtain the frequency so we can use this information to let the computer to know how to arrange the characters in the Huffman tree. 
    
    trees_dict[new_label] = merge_trees(new_label, tree1, tree2)
    # trees_dict [what key is representing the entire thing on the right side of the equal]
    # new_label = root of the tree
    # tree1 = left hand side (left child)
    # tree2 = right hand side (right child)
    
  # Get the whole Huffman tree
  last_remaining_label = new_label
  huffman_tree = trees_dict[last_remaining_label]

  encodings_dict = {}

  # Return the Huffman encoding of all characters based on a Huffman tree 
  def get_encoding(tree, beginning_of_encoding=""):
    if len(tree) == 1:
      # We're on a leaf, so we need to update the dictionary
      # Ex: our tree looks ['c']
      leaf_label = tree[0]
      encodings_dict[leaf_label] = beginning_of_encoding
      # updates the encoding dictionary
    else:
      left_tree, right_tree = tree[1], tree[2]
      get_encoding(left_tree, beginning_of_encoding + "0")
      get_encoding(right_tree, beginning_of_encoding + "1")
    # This counts as a merge sort, where we divide and conquer. 

  get_encoding(huffman_tree)
  
  return encodings_dict

#########################################################################################

user_string = input("Please paste the text file that you would like me to compress.")

huffman_dict = Huffman(user_string)

print(''.join([huffman_dict[i] for i in user_string]))
# getting the encoding for the character in the user string using the huffman dictionary.
# ''.join means that we are joining all of the encoding together and it is seprated by nothing. 

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



