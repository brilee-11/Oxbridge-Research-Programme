# Object Oriented Language
L = []
for i in range(5):
  if i%2 == 1:
    L.append(i**2)


# Better (more pythonic) this way
# List comprehension (repetitions and the order matters):
L = [i**2 for i in range(5) if i%2 ==1]

# Dictionary comprehension:
d = {i:i**2 for i in range(5) if i%2 ==1}

# Set comprehension (no repetitions and order doesn't matter):
s = {i**2 for i in range(5) if i%2 ==1}


def count(string, char):
  return len([c for c in string if c==char])