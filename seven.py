# Variables
string = 'value'
number = 67
number2 = 67
print string
print "I'm printing a number %d" % number

# Conditionals
if number < number2:
  print "Number %d is less than %d" % (number, number2)
elif number > number2:
  print "Number %d is greater than %d" % (number, number2)
else:
  print "%d and %d must be equal then" % (number, number2)

# Collections
list = ['string1', 'string2', 'string3']
print list[1]
list.pop()
print len(list)
list.append('another string')
print len(list)

# Looops
for n in list:
  print "n is: %s" % n

for i in range(0,5):
  print "iteration #%d" % i

# Functions
def printString(strList):
  for s in strList:
    print "from the list: %s" % s

printString(list)

def multiplyNums(numList):
  product = 1
  for n in numList:
    product *= n
    print "product %d" % product

multiplyNums([4,5,6])

# Toy Problem
def largestProdThree(numList):
  one = 0;
  two = 0;
  three = 0;
  temp = 0;

  for n in numList:
    if n > three:
      three = n
    if three > two:
      temp = two
      two = three
      three = temp
    if two > one:
      temp = one
      one = two
      two = temp

  product = one*two*three
  print "Product: %d" % product

largestProdThree([1,2,3,4,5])

# 1. Variables
# 2. Conditionals
# 3. Collections
# 4. Loops
# 5. Functions

# and 2 special secrets:

# 6. Where are the Docs?
# 7. How do I execute the code?