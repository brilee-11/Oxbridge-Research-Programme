'''
1st trial  (linked to the file named huffman string) :
data = []
with open ("huffman string") as file :
  data = file.readlines()

print(data)

def Huffman(data):
  data = file.replace ('H' , "111")
  return "111"
  data = file.replace ('o' , "100")
  return "100"
  data = file.replace ('l' , "101")
  return "101"
  data = file.replace ('b' , "10")
  return "10"
  data = file.replace ('a' , "01")
  return "01"
  data = file.replace (' ' , "11")
  return "11"

'''


print("Idea: the more frequent a character is, the shorter its Huffman encoding, because it's going to appear more times")

# the previous comment is called a docstring

# Replace each character (for example 'M', 't', 'b', etc) by its Huffman encoding (ex: 'M' corresponds to "10")return "0110110"


input_string = "Hola ba ma"
   
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
    print(string6)
else :
    print(" ")




'''
the "key" :

string = input_string.replace("H", "101")
string = input_string.replace("o", "100")
string = input_string.replace("l", "110")
string = input_string.replace("m", "001")
string = input_string.replace("b", "01")
string = input_string.replace("a", "10")
string = input_string.replace(" ", "11")

'''

