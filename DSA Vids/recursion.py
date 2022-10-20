# Best recursion example


# How to find the sum of digits of a positive integer number using recusion?

def sum_pos_int(x):
  assert x>=0 and int(x) == x, 'The number has to be a postive integer only'
  if x//10 == 0:
    return x%10
  else:
    return x%10+sum_pos_int(x//10)


# How to calculate power of a number using recursion ?

def power_number(num,pow):
  if pow == 0:
    return 1
  else:
    return num* power_number(num,pow-1)



# How to find GCD of two numbers using recursion

def gcd(x,y):
  temp = x
  while temp>1:
    if y%temp == 0 and x%temp ==0:
      return temp
    if temp == 1:
      return 1
    temp = temp-1