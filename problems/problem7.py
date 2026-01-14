# loops in python

#question 1
num=int(input("Enter a number: "))
for i in range(1,11):
 print(i*num)

# question 2
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello " + name)
    else:
        continue

# question 3
num = int(input("Enter a number: "))
while i<11:
    print(i*num)

# question 4
num = int(input("Enter a number: "))
for i in range(2, num):
    if num>0 and num==1 or num==2 :
      print("The number is prime")
    elif num >2 and num%i==0:
      print("The number is prime")
    else:
      print("The number is not prime")

# question 5
num = int(input("Enter a number: "))
i = 1
sum = 0
while i<num:
   sum += i
   i += 1
print("The sum of numbers from 1 to", num, "is", sum)

# question 6
num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num):
    factorial = factorial*i
print("The factorial of", num, "is", factorial)

# question 7




   

