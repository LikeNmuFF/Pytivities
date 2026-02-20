#activity 1
#print Hello World
print("Hello World!")
print()
print()

#activity 2
#Python program to add two numbers
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1,num2,sum))
print()
print()

#activity 3
#Add two numbers with user input
num2 = input("Enter first number: ")
num3 = input("Enter second number: ")
sum = float(num2) + float(num3)
print('The sum of {0} and {1} is {2}'.format(num2,num3,sum))
print()
print()

#activity 4
#python program to find square root
#for positive numbers
num = 8
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num,num_sqrt))
print()
print()

#activity 5
#for real or complex numbers
import cmath
num = 1+2j
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f} + {2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))
print()
print()
#activity 6
#Calculate the area of a triangle

a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f' %area)

print()
print()
#Python Program to Solve Quadratic Equation
#ACTIVITY 7
import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
print()
print()

#The solutions are (-3+0j) and (-2+0j)
#Python Program to Swap Two Variables
#ACTIVITY 8
x = 5
y = 10
temp = x
x =y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}' .format(y))
