#====================================
#activity 6                         |
#Calculate the area of a triangle   |
#====================================
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f' %area)