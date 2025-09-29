print("jamiz qamar")
# it is used to make single line of comment 
"""
this is used to make 
multiple line of comments 
"""
print("hello, jamiz qamar")

# variables are the containers to store the data in it
x= 10 # integer variable
z= 'jamiz alam' # string variable
y= 20.5 # float variable
name= "jamiz qamar alam" # string variable
is_student= True # boolean variable
print(x)
print(z)
print(y)
print(name)
print(is_student)
print(type(x))
print(type(y))
print(type(name))
print(type(is_student))


# python is a case sensitive langugage means uppercase lowercase matter 


"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

"""

# multiple variable assignment
a, b, c = 5, 10.5, "jamiz"
print(a,b,c)

# assigning same value to multiple variables
w = q = r = "jamiz"
print(w,q,r)


"""
If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. 
This is called unpacking.

"""
fruits = ["apple", "banana", "cherry"]
p, q, r = fruits
print(p)
print(q)
print(r)


# use + operator to output multiple variable 
# when you try to combine a string and a number with the + operator, Python will give you an error:
first_name = "jamiz"
last_name = "qamar"
full_name = first_name + " " + last_name
print(full_name)

g = 78
h = 22
print(g + h)
print(g - h)
print(g * h)
print(g / h) 
print(g % h)
print(g // h) 
print(g ** h)



# global variable 
#variable that are defined outside funcation are called global variable
x = "jamiz qamar"
def myfunc():
    y = "hello" # hello is a local variabe
    print(y + x)
myfunc()  
print(x) 


# to create global variable inside a function we use word "global"
x = "jamiz qamar"
def myfunc():
    global y
    y = "hello" 
myfunc()  
print(x + y)