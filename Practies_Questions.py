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


  
  

