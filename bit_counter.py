# Iterative Way
def count_bits(x):
  num_bits = 0
  while x:
    num_bits += x & 1
    x >>=1
  return num_bits


# Reccursive way

def foo(x,num):
  if x == 0:
    return num
  else:
    num += (x & 1)
    x >>= 1
    return foo(x, num)


print(foo(13,0))