# Immerse Education Project

Website link: [https://brilee-11.github.io/Oxbridge-Research-Programme/](https://brilee-11.github.io/Oxbridge-Research-Programme/)

## Goal of the project

The goal is to write a little Python package of file compression, providing two functions: `Huffman_encode(input_file)` and `Huffman_decode(encoded_file)`.

The user will provide a local text file that they want to compress/uncompress.
In a more advanced future version (to get some training with databases), we could even store the compressed files in a SQLite database.


## Sorting algorithms

* Sorting algortihms arrange pieces of data in a certain order.
* Sorting lists sometimes makes it easier to process the information provided by the user.
* In our case, the list of frequencies would benefit from getting sorted, because in the Huffman algorithm, the 2 least frequent character trees (partial Huffman trees) in the string are merged together (and the algorithm terminates when the list of frequencies has only one element). The corresponding string will be the root of the final partial Huffman tree.
* It is also possible to give conditions when sorting the list:
  ***i.e. ascending or descending order, sorting alphabetically, etc.***

~ It is IMPOSSIBLE to sort a dictionary, because in a dictionary, the order does not matter. 

### Bubble Sort

↠↠ Continuously swapping the pairs of elements that are in the wrong order. This can vary based on the rule (the condition), whether it be sorting in ascending or descending order, etc.

##### ***EXAMPLE:***

This is the execution trace of the first pass of the algorithm. This example will be sorted in ASCENDING ORDER:

```
First Sorting:
( 5 1 4 2 8 ) –>  (1 5 4 2 8 ) Swap 1 & 5, because 5 > 1
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ) Swap 5 & 4, because 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ) Swap 5 & 2, because 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) The final 2 elements, 5 and 8 are in order because 5 is before 8. 
Thus the bubble sort won't swap them anymore.
```

##### ***
However, these numbers are still not in the right ascending order. Therefore, we need a second pass.*** #####

```
Second Sorting:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ) Swap 4 & 2, because 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
```

##### ***At last, we can see that the elements are sorted properly. But the sorting algorithm will need to run one more pass, to make sure that there are no out-of-place elements left.*** #####

```
Third Sorting:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) ✅
```

### Merge Sort

↠↠ This sorting algorithm applies the DIVIDE AND CONQUER paradigm. 

↠↠ The merge sort divides the input into 2 and splits itself to tackle each part recursively. This cycle continues until the recursive call only has 2 input elements to sort (a single comparison then suffices). The "sorting" part of this algorithm is when it combines the sorted lists yielded by the recursive calls. It builds the combined list (merging the two recursively sorted lists) by element-wise comparisons.

![Merge sort example](https://lh3.googleusercontent.com/-TOZuIu1mYzo/X_bdMHbk8xI/AAAAAAAAKf0/A1igakPk4GsW2DB5IbTiGCI19g3KhvBdACK8BGAsYHg/s0/2021-01-07.jpg)

### Comparison of both sorting algortihms

↠↠ The main comparison between the merge sort and the bubble sort, is that once the data or the input file gets larger,the time needed for bubble sort to fully work increases faster than that of the merge sort.

↠↠ This means that bubble sort is less efficient when it comes to the time required to sort a large list, compared to the merge sort. The bubble sort has a quadratic time complexity, whereas the merge sort runs in quasilinear time.

↠↠ Another main difference is that the BUBBLE sort is an ITERATIVE procedure, and the MERGE sort is a RECURSIVE (it calls itself on smaller inputs) procedure.

## Huffman coding

##### *** IDEA : ***

The more frequent a character is, the shorter its Huffman encoding, because it is going to appear more times in the resulting encoded string.

##### *** AIM : ***

The aim is to be able to take a string provided by the user and compress it.

##### *** Steps on how to do it (in English): ***

1. Take the `string` provided by the user and treat it as an input value.
2. Calculate the frequency (number of occurrences) of each character in the `string`, and store it in a dictionary.
3. Sort the dictionary with respect to the frequencies in descending order.
4. Create another dictionary for the (partial Huffman) trees, where the frequency is not represented (the frequency information will be obtained from the first dictionary)
5. Create a function to merge the frequencies (values) and characters (to form a string), and apply it to THE LAST 2 ELEMENTS (ie. the least frequent elements), and add them back to the frequencies dictionary.
6. Sort the dictionary once again with the newly merged string (key) and frequency (value).
7. Create another function to merge the trees based on the information obtained in the function merging the frequencies.
8. Create a `while` loop such that the process of merging the frequencies and trees continues as long as there is more than one string and value (couple) in the frequencies dictionary. This continues until the exit condition is satisfied, that is, there is only 1 couple left in the frequencies dictionary.
9. In the body of the while loop, we would also need to pop off keys of the dictionary containing the partial Huffman trees. Popping off the keys (the merged string, NOT ALL AT ONCE), would allow us to see the value of each individual character. This would help the overall `Huffman` function to use this information (the frequency of the popped keys) to form the final Huffman tree.
10. Then, we can call the function to merge the trees, giving it as arguments the root of the tree, the left child, and the right child.
11. After this, we need to write what happens once the while loop ends, that is, when there is only 1 key left in the trees dictionary.
12. Create a new encoding dictionary that will hold the encodings of each character (key) of the user string.
13. Create a function populating the encoding dictionary: it updates the encoding dictionary as soon as it reaches a leaf (only one key) of the final Huffman tree.
14. But if there is more than one key, then create an `else` statement and apply the divide and conquer paradigm; assigning the left tree with the encoding prefix "0" and the right tree with the encoding prefix "1"
(This else statement basically enables us to keep track of each character's encoding. Once it reaches another internal node, it will add the last tracked encoding and append either a "1" or a "0" depending on its location.)
1.  In this function is then applied to the tree associated to the last remaining label in the trees dictionary (ie. the final Huffman tree).
2.  In the overall `Huffman` function, the encoding dictionary is the one returned, because the information that we want is the ENCODING OF ALL OF THE CHARACTERS IN THE INITIAL STRING.
3.  (Since the aim is to get the user's string and compress it) Create a variable which asks the user for their string and apply the overall `Huffman` function to get a new encoding dictionary.
4.  Construct a list comprehension that ranges over every character in the string provided by the user, find it in the latest dictionary containing the encodings, and print it.


##### *** Python implementation : ***

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

↠↠ `my_array[0]` is `"value 1"`, and `my_array[1]` is `"value 2"`: 

↠↠ ie. the key `0` is associated to the value `"value 1"` (written `0` ⟼ `"value 1"`), and the key `1` is associated to `"value 2"` (written `1` ⟼ `"value 2"`)

#### *** How to use it? *** ####

Create an empty dictionary (no keys, no values):

```python
my_dict = {} 
```

But, you can add a new `key` ⟼ `value` pairing (a value can be anything, but a key can only be _immutable_ (that is, something that has a certain value and cannot be modified), for example: a string, a number, a tuple, etc BUT NOT a list,an array, etc (because these can be modified)).

#### *** In our case... *** ####

↠↠ We would like our keys to be the characters of our `input_string`, and not just integers. 

↠↠ For example, we would like to associate to the key `"H"` (the encoded character) the value `"101"` (the corresponding Huffman code): `"H"` ⟼ `"101"`

A dictionary is EXACTLY the data structure that enables us to do that (In a way, it is a function, where the domain is finite: to each key, you associate a value, but you have a finite number of keys).

### Binary heaps

* A heap is a *** COMPLETE BINARY TREE ***
* There are 2 types of binary heaps :
1. Min heap
2. Max heap

#### *** Minimum Binary Heap *** ####

In a min heap, every parent (internal node) is smaller than its children. Therefore, the root of the tree (the top-most node) is associated to the MINIMUM value. In our case, it is the minimum number/frequency of character occurrences in the user string. 

#### *** Maximum Binary Heap *** ####

Similarly, in a max heap, the internal nodes are always either greater than or is equal to the values of the children of the said internal node.
