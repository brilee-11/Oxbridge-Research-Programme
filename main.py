# STEPS :
'''
 Replace each character (for example 'M', 't', 'b', etc) by its Huffman encoding (ex: 'M' corresponds to "10")return "0110110"
 Idea: the more frequent a character is, the shorter its Huffman encoding, because it's going to appear more times") 


* Useful notion: dictionaries
-> A dictionary is a data structure (a bit like a list or an array) where you can associate values to certain keys. For example, an array can be seen as dictionary, where the keys are always natural numbers: 

my_array = ["value 1", "value 2"]

-> my_array[0] is "value 1", and my_array[1] is "value 2": 
-> ie. the key 0 is associated to the value "value 1" (written 0 ⟼ "value 1"), and the key 1 is associated to "value 2" (written 1 ⟼ "value 2")

-> BUT: in our case, we would like our keys to be the characters of our input_string, and not just integers. 
-> For example, we'd like to associate to the key "H" (the encoded character) the value "101" (the corresponding Huffman code): "H" ⟼ "101"

-> A dictionary is _exactly_ the data structure that enables us to do that! (In a way, it's a function, where the domain is finite: to each key, you associate a value, but you have a finite number of keys)

-> How to create a dictionary in Python? 

-> my_dict = {} # Empty dictionary: no keys, no values
# and then you can add a new "key" ⟼ "value" pairing (a value can be anything, but a key can only _immutable_ (we'll talk about it next time: that is, something that has a certain value and can't be modified): for ex: a string, a number, a tuple, etc BUT NOT a list, an array, etc (because these can be modified)):

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

'''
  

string = "computer science is the study of computers and computational systems"
dictionary = {}

for i in string :
  if i in dictionary :
    dictionary[i] += 1
  else :
    dictionary[i] = 1
print(str(dictionary))

sorted_list = sorted(dictionary) 
print(str(sorted_list))
# this is sorted from most frequent to least frequent



