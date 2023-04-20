Exercise 1: Write a program in Python to calculate the volume of a sphere.
  
sol::
  from math import pi
def valume(r):
    v=((4*pi*r**3)/3)
    return v
print(valume(3))



Exercise 2: Write a program in Python to display a below-given pattern.
  Hint
Input: 6

Expected Output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


sol::
    n=int(input("enter input: "))
for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print("\n")
    
    
    Exercise 3: Range function program to return multiple of 7 within a given range 1,30.
    Hint
Use range() function
Start range from 1

Expected Output
7 14 21 28

sol::
    n=int(input("enter the input: "))
count=0
for i in range(1,50):
    if i%n==0:
        print(i,end=" ")
        count+=1
print("\nno of occuring multiples :",count)



Exercise 4: Write a program in Python to swap between two numbers without using a third variable.
  
  Hint
Input:
a = 4
b = 6

Expected Output
After swapping
a is 6 and b is 4


sol::
    
a=int(input("enter the a: "))
b=int(input("enter the b: "))
a=a+b
b=a-b
a=a-b
print("a = ",a,"and b = ",b)


Exercise 5: Write a program to check wheteher the given word is vowel or consonent.
  Hint 1:
Vowels are ‘a’, ‘e’, ‘i’, ‘o’, ‘u’
Input : a

Expected Output:
a is vowel

Hint 2:
Vowels are ‘a’, ‘e’, ‘i’, ‘o’, ‘u’
Input : d

Expected Output:
d is consonent


sol::
    
ch=input("enter the alphabets: ")
if ch in ['a','e','i','o','u']or['A','E','I','O','U']:
    print("this is a vowel: ",ch)
else:
    print("this is a consonent: ",ch)

  
  
  
  
  # Exercise 6: Write a program to swap two numbers without using a third variable.

sol::
    
    
    
a=int(input("enter the value of a: "))
b=int(input("enter the valur of b: "))
a=a+b
b=a-b
a=a-b
print("a = ",a,"b = ",b)



# Exercise 7: Write a program to count the occurence of even number and odd number between the range 10 – 55.


sol::
    evenNumber=0
oldNumber=0
for i in range(10,55):
    if i%2==0:
        evenNumber+=1
    else:
        oldNumber+=1
print("occurence of even",evenNumber)
print("occurence of old",oldNumber)


  
  
 # Exercise 9: Write a program in Python to calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2.

  
  sol::
      
      
v1=int(input("enter the velocity1: "))
v2=int(input("enter the velocity2: "))
t1=int(input("enter the time1: "))
t2=int(input("enter the time2: "))
a=((v2-v1)/(t2-t1))
print("acceleration: ",a)
  
  
  
  

  def acceleration(v1,v2,t1,t2):
    a=((v2-v1)/(t2-t1))
    return a

v1=int(input("enter the velocity1: "))
v2=int(input("enter the velocity2: "))
t1=int(input("enter the time1: "))
t2=int(input("enter the time2: "))
print("acceleration: ",acceleration(v1,v2,t1,t2))



# Exercise 10: Write a program in Python to sort 3 numbers without using loops or conditional statements.


sol::
    
val1=int(input("enter the val1: "))
val2=int(input("enter the val2: "))
val3=int(input("enter the val3: "))
print("\nbefore sorting : ",val1,val2,val3)
s=[]
s.append(val1)
s.append(val2)
s.append(val3)

s.sort()
print(s)



# Exercise 11: Write a program in Python to print number ranging from 1 to 25 but excluding number which is the multiples of 5.


# sol::

for i in range(10,25):
    if i%5==0:
        # continue
        pass
    else:
        print(i,end=" ")

        
        

        
        
        
        # Exercise 12: Write a program in Python to count the occurrence of a specific value in a list.


# sol::

list=[1,3,3,4,2,3,4,6,3,5,3,3,3]
count=0
for i in range(len(list)):
    if list[i]==3:
        count+=1
    else:
        continue
print("occurrence of 3 are ",count," times")





# Exercise 13: Write a program in Python to count the occurrence of a specific word in a string.


# sol::


string_ = "adam is a boy and adam loves to play cricket."
str=input("enter the word which you want to fine in the string: ")
main=string_.split(" ")
count=0
for i in range(len(main)):
    if main[i]==str:
        count+=1
print(str," occurrence ",count)




\# Exercise 14: Write a  program in Python to check whether the given number is even or odd.



# sol::


a=int(input("enter a number to check whether is even or odd: "))
if a%2==0:
    print("this is an even: ",a)
else:
    print("this is an odd: ",a)

    
    
    # Exercise 15: Given two integer numbers return their product. If the product is greater than 500, then return their sum.


# sol::

a=int(input("enter a number a: "))
b=int(input("enter a number b: "))
if a*b>500:
    print(a*b)
else:
    print(a+b)
    
    other way::
    
    def check(a,b):
    if a*b>500:
        print(a*b)
    else:
        print(a+b)

a=int(input("enter a number a: "))
b=int(input("enter a number b: "))
check(a,b)





# Exercise 16: Write a program to print the greatest of three number.

# sol::

a=int(input("enter the number a: "))
b=int(input("enter the number b: "))
c=int(input("enter the number c: "))
if (a>b and a>c):
    print("a is the greater number: ",a)
elif (b>a and b>c):
    print("b is greater number : ",b)
else: 
    print("c is grater number: ",c)



    
# Exercise 17: Write a program to print all numbers multiple of 5 from the range 10 – 50. 

# sol::


for i in range(10,50):
    if( i%5==0):
        print(i,end=" ")
        
        
        
        
# other  way to sol::

def multiple(x,y):
    for i in range(x,y):
        if( i%5==0):
            print(i,end=" ")

x=int(input("enter initial point x: "))
y=int(input("enter final point y: "))
multiple(x,y)





# other way to sol::

def check(list):
    if(list[0]==list[len(list)-1]):
        print("true")
    else:
        print("false")
    
list=[1,2,3,4,5,6,7,1]
check(list)



# Exercise 19: Write a program to convert, the Fahrenheit value to Celcius. [Formula : F=9/5(c)+32] 

# sol::

# f=int(input("enter the fahrenheit: "))
# c=(f-32)*5/9
# print("fahrenheit to celcius : ",c)

# other way

def fahrenheitToCelcius(f):
    c=(f-32)*5/9
    print("fahrenheit to celcius : ",c)


f=int(input("enter the fahrenheit: "))
fahrenheitToCelcius(f)




# Exercise 20: Write a program to print a right angled triangle pattern,  Please find hint below:-


# sol::


a=int(input("enter the a: "))
def print_pattern(a):
    for i in range(a):
        for j in range(i):
            print("*",end=" ")
        print("\n")
print_pattern(a)








# 21. Write a Python program to sum all the items in a list.


# sol::

def sum_list(list):
    sum=0
    for i in list:
        sum+=i
    print("list sum = ",sum)

list=[2,5,8,3,9]
sum_list(list)



# Write a Python program to multiply all the items in a list.

# sol::


def multi_list(list):
    multipl=1
    for i in list:
        multipl*=i
    print("list multi = ",multipl)

list=[2,5,8,3,9]
multi_list(list)





# 23. Write a Python program to get the largest number from a list.


# sol::

def largest_number_list(list):
    max=0
    for i in list:
        if i>max:
            max=i
    return max


list=[2,5,8,3,9]
print(largest_number_list(list))


# 24. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2



# sol::

def count_string(list):
    count=0
    for x in list:
        if len(x)>1 and x[0]==x[-1]:
            count+=1
    return count


list = ['aba', 'xyx', 'abb', '222']

print(count_string(list))






