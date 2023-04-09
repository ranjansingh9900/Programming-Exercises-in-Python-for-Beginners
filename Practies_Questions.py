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

