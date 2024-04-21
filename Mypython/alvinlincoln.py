#the variable some_string is assigned the string 'Python is fun'
some_string = 'Python is fun' 
#variables a, b and c are assigned the values 5, 3.2  and 'Hello' respectively
a, b, c = 5, 3.2, 'Hello'

print(a)  # the print statement displays the value of variable a
print(b)  # the print statement displays the value of variable b
print(c)  # the print statement displays the value of variable c

#the variable num1 is assigned the interger value of 5
num1 = 5
#the print statement displays the value of num1 as well as its data type
print(num1, 'is of type', type(num1))
#the variable num2 is assigned the float value of 2.0
num2 = 2.0
#the print statement displays the value of num2 as well as its data type
print(num2, 'is of type', type(num2))
#the variable num3 is assigned the complex number 1+2j
num3 = 1+2j
#the print statement displays the value of num3 as well as its data type
print(num3, 'is of type', type(num3))
#the list languages contains three strings namely "swift", "java" and "python"
languages = ["Swift", "Java", "Python"]

# this statement displays the first element of the list languages
print(languages[0])   # 

# this statement displays the third element of the list languages
print(languages[2])   # 

#  the tuple product contains three elements namely "microsoft", "xbox" and 499.99
product = ('Microsoft', 'Xbox', 499.99)

# this print statement displays the first element of the tuple product
print(product[0])   # Microsoft

# this print statement displays the second element of the tuple product
print(product[1])   # Xbox


# the dictionary capital_city maps countries to their capital cities
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
#this statement will display the above dictionaary
print(capital_city)


# the set student_id contains student ID values
student_id = {112, 114, 116, 118, 115}

# this print statement displays the values in the set
print(student_id)

# this print statement displays the data type of the set student_id
print(type(student_id))

# the list fruits contains three strings namely "apple", "mango" and "orange"
fruits = ["apple", "mango", "orange"] 
#this print statement displays the list fruits
print(fruits)

# the tuple numbers contains three intergers
numbers = (1, 2, 3) 
#this print statement displays the tuple numbers    
print(numbers)

# the dictionary alphabet maps alphabets to words starting with the same alphabet
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#this print statement displays the dictionary
print(alphabets)

#the print statement displays the vowels in the set
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


# the set student_id contains student ID values 
student_id = {112, 114, 116, 118, 115}

# the print statement displays the set student_id
print(student_id)

# this print statement displays the datatype of the set student_id
print(type(student_id))
# the tuple product contains three elements namely "microsoft", "xbox"  and 499.99
product = ('Microsoft', 'Xbox', 499.99)

#this print statement displays the first element of the tuple product
print(product[0])   # microsoft

# this print statement displays the second element of the tuple product
print(product[1])   # Xbox




#variable a is assigned a value of 7 and variable b is assigned a value of 2
a = 7
b = 2

# this print statememt displays the sum of a and b
print ('Sum: ', a + b)  

#this print statement displays the subtraction of b from a 
print ('Subtraction: ', a - b)   

# this print statement displays the multiplication of a and b
print ('Multiplication: ', a * b)  

# this print statement displays the division of a by b
print ('Division: ', a / b) 

# this print statement displays the floor division of a by b
print ('Floor Division: ', a // b)

# this print statement displays the modulo of a by b
print ('Modulo: ', a % b)  

# this print statement displays a raised to the power of b
print ('Power: ', a ** b)   


# variable a is assigned a value of 10 
a = 10

# variable b is assigned a value of 5
b = 5 

# value a is += value b
a += b      # a = a + b
print(a)
# Output: 15


# this print statement displays whether  a is equal to b
print('a == b =', a == b)

# this print statement displays whether a is not equal to b
print('a != b =', a != b)

# this print statement displays whether a is greater than b
print('a > b =', a > b)

# this print statement displays whether a is less than b
print('a < b =', a < b)

# this print statement displays whether a is greater than or equal to b
print('a >= b =', a >= b)

# this print statement displays whether a is less than or equal to b
print('a <= b =', a <= b)
#this print statement checks if a is greater than 2 and if b is greater than or equal to 6
print((a > 2) and (b >= 6)) 

# logical operator and checks whether two conditions are met and if so it prints True and where one of the conditions is not met it prints False
print(True and True)     # True
print(True and False)    # False

# logical OR checks whether at least one of the conditions is True which it is and so it prints True
print(True or False)     # True

# this statement uses logical Not operator to nullify the True value in so doing printing False
print(not True)          # False

#variable x1 is assigned a value of 5, variable y1 is assigned a value of 5, variable x2 is assigned a value of 'Hello', variable y2 is assigned a value of 'Hello', variable x3 is assigned a list [1, 2, 3] and variable y3 is assigned a list [1, 2, 3]
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
#this statement checks if x1 is not the same object as y1 which is false because they have the same value 
print(x1 is not y1)  # False
#this statement checks if x2 is the same object as y2 which is true because both variables contain the same string value 
print(x2 is y2)  # True
#this statement checks if x3 is the same object as y3 which is false because much as they contain the same values, the two lists are different
print(x3 is y3)  # False
#this staed statement assigns the string 'Hello world" to the variable message
message = 'Hello world'
#this statement creates a dictionaary dict1 with keys 1 and 2 and values 'a' and 'b'
dict1 = {1:'a', 2:'b'}
# this statement checks if the character 'H' is present in the string message which is True
print('H' in message)  # True

# this statement checks if the string 'hello' is not present in the string message which is True
print('hello' not in message)  # True

# this statement checks if the key 1 is present in the dictionary dict1 which is True
print(1 in dict1)  # True

# this statement checks if the key 'a' is present in the dictionary dict1 which is False
print('a' in dict1)  # False