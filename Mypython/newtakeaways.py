#i have learned that a loop is a mechanism or means of writing instructions to a computer to repeatedly do an action until a certain condition is met
#i have learned that we have two types of loops namely for and while
#below is an example of each loop
def loop1():
    list = [2,4,5,6,7,8,9]
    for i in list:
        print(i)
loop1()        

#above is a for loop that I executed by invoking a function however I could still run the same example without calling rather using a print statement
list = [2,4,5,6,7,8,9]

for i in list:
    print(i)

#another example using a invokation
def loop2():
    for  i in range(1,10):
        print(i)
loop2()             
#in the above example 1 represents the start of the range and 10 is the end of the range
#you notice the above example is indented which signals its a block of code. a block of code is a collection of related statements
#in order to make example 1 and example 3 run, we have to invoke them as seen on line 8 and 20 and only then shall you see an output in the terminal

#I also learned that loops can have conditions within them as illustrated in the following example;
for num in range(1, 10):
    if num > 10:
        print("figures exceed")
    else:
        print("figures are within")    

#I also learned about the while loops and the examples below shows how they behave;
start = 5
end = 10
while start <= end:
    print(start)
    start += 2        

counter = 6
while counter < 13:
    print("numbers fall in the range")
    counter += 1
else:
    print("beyond the range")    


#I also learned about functions where I learned that they are a group of statements related to one another and perform a specific task. Earlier I talked about a block of code and said they are related functions meaning a function is a block of code
#i learned that we have two types of functions namely static and dynamic functions
#static functions are functions without parameters in the parenthesis plus they cant be changed while dynamic functions are functions that have parameters in the parenthesis and can be changed
# i also learned that functions are not created but instead they are defined and thats why they are invoked by def then a function name
# below is an example of a static function
def condition():
    num = 8
    if num > 0:
        print("its positive")
    print("straightforward")    
condition()        
#below is a distinction between the use of a print statement and invoking a function both yielding the same result with the exception of the second condition in the function
num = 8
if num > 0:
   print("its positive")

#i also learned about dynamic programming and that the values within the parentheses are known as arguments to the function
#below are some examples on dynamic functions;
def add(num1, num2, num3):
    sum = num1 + num2 + num3
    print(sum)
add(20, 30, 55)

def multiply(num1, num2):
    product = num1 * num2
    print(product)
multiply(20, 30)    

#I learned that we have local variables that work within the function and we also have global variables that can be accessed at anytime within the file
#i also learned that we can invoke a function at anytime in the file even after 200 lines of code
#I also learned that a return statement is the last statement in a function and anything typed after it is not executed by the computer
#below is an example of how a global variable can be accessed;
age = 18
def sum(a, b):
    product = a * b
    print(product)

def sum1(a, b): 
    product = a * b + age
    age1 = 30
    print(product)  
    print(age1)
sum1(8, 5)    
#age being the global variable in the above example

#I also learned about dictionary datatype under mapping and we use {} when using them. under mapping, we use keys that correspond to different values in the dictionary for instance;
person = {
    "name": "Alvin",
    "age": 25,
    "city": "kampala"
}
print(person)

#yesterday I learned how to create a folder/directory using the command prompt
#i also learned how to create a package that can accessed by another developer and this can be through creating a python script with the name __init__.py, importing a file into another run script and running it within the terminal  