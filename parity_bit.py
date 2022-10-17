# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
# This is my version

def parity(x):
  count = 0
  while x:
    if x & 1 == 1:
      count = count+1
      x >>= 1
    else:
      x >>= 1
      continue

  print("Count",count)
  if count %2 == 0:
    return 0
  else:
    return 1


print(parity(60))