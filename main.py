# How to create a dict in python?
# my_dict["key"] = "value" # adds the association "key" ⟼ "value" to the dictionary
# my_dict[1] = "value" # 1 ⟼ "value" # adds the association 1 ⟼ "value" to the dictionary
# my_dict["something"] = 4 # adds the association "something" ⟼ 4 to the dictionary
# etc...

# You can also directly create some associations right from the start when creating your dictionary: 
# my_dict = {1: "value", "something": 4, "key": "value"} 



input_string = "Hola ba ma"
def huffman(input_string) :
  if "H" in input_string :
      string = input_string.replace("H", "101") 
  else :
      print (" ")

  if "o" in input_string :
      string1 = string.replace("o", "100") 
  else :
      print(" ")

  if "l" in input_string :
      string2 = string1.replace("l", "110") 
  else :
      print(" ")

  if "m" in input_string :
      string3 = string2.replace("m", "001") 
  else :
      print(" ")

  if "b" in input_string :
      string4 =  string3.replace("b", "01") 
  else :
      print(" ")
      
  if "a" in input_string :
      string5 = string4.replace("a", "10")
  else :
      print(" ")

  if " " in input_string :
      string6 = string5.replace(" ", "11")
  else :
      print(" ")

  return()


def Huffman_coding(input_string):
  # apply the Huffman coding algorithm to input_string (with a dictionary, etc) and store the result in output_string

  #return output_string

# This is great but a bit too early, no need to worry about files for the time being: do as if the content of the file was stored in the input_string variable (we will scan the file of the user later and do that)

  with open ("location/of/the/user_file.txt") as file:
    data = file.readlines()

dictionary = {}
data = dictionary



#trial :
input_string = "Computer Science is the study of computers"

dictionary = {}


  # This doesn't work for all possible input_strings unfortunately (for ex: if input_string = "abbbbbbbbbbb", then a won't be encoded by "1" because it's rare, so it's encoding will be a long string, and b will have a very short encoding) 
 
  # The problem with your approach at the moment is that _you_ did all the work by hand to compute the encoding of each character on specific input_string examples. We would like the computer to do that instead. 
  # I would highly recommend to first try and describe the algorithm in english (cf. exercise: https://trello.com/c/1Tq3sS4e/11-write-a-pseudo-code-for-the-huffman-algorithm ), and _then_ only to begin to code, because it's confusing otherwise to directly start coding (especially for beginners, it's totally normal!). 
  # What are we trying to do (in English)? If you could describe what happens without worrying about the specific details of the implementation, it could help. 
  # Example: 
  # STEP 1: take a string (provided by the user) to encode as an input
  # STEP 2: compute the frequencies of each character in this string
  # I mean: computing how many times each character appears in the string. For example, if input_string = "aaabc", then "a" appears 3 times, "b" and "c" one time
  # etc...
  
 
  # Pseudocodes are _crucial_ in CS: you just can't avoid them when the algorithms become too complicated, because then you're lost because of the specifics of the implementation in Python, and these are two very separate steps (describing the algorithm in english VS implementing it in a programming language). Sometimes you can do both at the same time, but not at the beginning, and not when the algorithm is too complicated: even researchers use pseudocode before implementing complicated stuff!

  # Close! len() only gives you the length of input_string, so you'd have len("aaabc") = 5, but it doesn't tell you how many times each character appears. 
  # So that's why I insist so much on the english version: it gives you the big picture (but each step is not necessarily easy to implement!), and _then_: you can try and solve each step by coding. But I do both at the same time, it's too overwhelming.


  
from collections import OrderedDict
# importing an ordered dictionary from the python library. 
string = "computer science is the study of computers and computational systems"

dictionary = {}

for i in set(string):
  dictionary[i] = string.count(i)

list_frequencies = sorted([(i,string.count(i)) for i in set(string)], key=lambda couple: couple[1], reverse=True)
# Anonymous function (lambda): A function which takes the second element of the function and sort it according to the second element. 
# couple is the brackets list (character, frequency)
print(list_frequencies)

frequencies_dict = OrderedDict(list_frequencies)



trees_dict = {}

def merge_tuples(tuple1, tuple2):
  x,y = tuple1, tuple2
  tuple1, tuple2 = frequencies_dict.popitem(), frequencies_dict.popitem()
  t_label, t_frequency = merge_tuples(x,y)
  return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])


def merge_trees(tree1, tree2):
  return None


# t1, t2 = frequencies_dict.popitem(), frequencies_dict.popitem()
# t_label, t_freq = merge_tuples(x, y)

# Then, create the merged tree, and add it to the trees_dict
# Then, add (t_label, t_freq) frequencies_dict 
# AND reorder the frequencies_dict

'''my trial:
for i in string:
  if i in dictionary:
    dictionary[i] += 1
  else:
    dictionary[i] = 1

#print(str(dictionary))
#print(dictionary["c"])

sorted_list = sorted(dictionary, reverse=True)
#sorted_list[:3:2] # ⟶ element 0, 2, but not 3 
#print(str(sorted_list))
'''

# Object Oriented Language
L = []
for i in range(5):
  if i%2 == 1:
    L.append(i**2)


# Better (more pythonic) this way
L = [i**2 for i in range(5) if i%2 ==1]

def count(string, char):
  return len([c for c in string if c==char])


frequencies_dict = OrderedDict(list_frequencies)
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
# popped off the last 2 elements and merged them together, and added them back to the list
# NEXT STEP : Reorder the list AGAIN!!

frequencies_dict = OrderedDict(sorted(frequencies_dict.items(), reverse = True, key=lambda t:t[1]))
print(" ")
print(frequencies_dict)
# reordered list with the merged element
# NEXT STEP : Pop off the last 2 element AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
#AGAIN
t1, t2 = frequencies_dict.popitem(),frequencies_dict.popitem()
print(" ")
print(t1,t2)
print(" ")
merge = (t1[0]+t2[0] , t1[1]+t2[1])
frequencies_dict[merge[0]] = merge[1]
print(frequencies_dict)
# The one above is the last one



