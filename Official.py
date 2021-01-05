######################################
#            OFFICIAL WAY            #
######################################

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

#########################################################################################

from collections import OrderedDict
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
    tree1 = trees_dict.pop(label1, None)
    tree2 = trees_dict.pop(label2, None)
    print(tree1, tree2)
    # This is to retrieve the value but getting rid of the key
    # Essentially, getting rid of the character to obtain the frequency so we can use this information to let the computer to know how to arrange the characters in the Huffman tree. 
    
    merge_trees(new_label, tree1, tree2)

print(new_label) 
#new label is etsyrumdhfl coainp