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

  get_encoding(huffman_tree)
  
  return encodings_dict

#########################################################################################

user_string = input("Please paste the text file that you would like me to compress.")

huffman_dict = Huffman(user_string)

print(''.join([huffman_dict[i] for i in user_string]))
# getting the encoding for the character in the user string using the huffman dictionary.


'''
a: 0
d: 11
b: 100
c: 101

  abcd
a       bcd
     bc     d
    b  c
'''