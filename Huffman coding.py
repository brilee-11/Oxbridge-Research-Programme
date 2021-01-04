string = "computer science is the study of computers and computational systems"
dictionary = {}

for i in string :
  if i in dictionary :
    dictionary[i] += 1
  else :
    dictionary[i] = 1

sorted_list = sorted(dictionary) 
print(str(sorted_list))
# this is sorted from most frequent to least frequent

#thought process 
sorted_list[0] = 1
sorted_list[1] = 0
sorted_list[2] = 11
sorted_list[3] = 10

# thought question : what happens when the entire tree is merged already?
>>> dict.pop(3,None)
9
>>> dict
{0: 0, 1: 1, 2: 4, 4: 16, 5: 25}
>>> 