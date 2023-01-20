"""
Day: Friday
Date: 20th Jan 2023
Time: 7:30 PM
Topic: Function programs
Author: Areeb Ahmed
"""

# def greet():
#     print('Hello')
#     # greet()
# greet()

# def greet(n):
#     print('Helo '+n)
# greet('HD')
# greet('PY')    

# def greet(*names):
#     print('Hey',names[-1])
# greet('Python','programming','core','Functions')    

# def details(n,a):
#     print('Hey '+n + '! Your Age is '+str(a))
# details('hd',25)
# details(n='HD',a=26)
# details(a=26,n='HD')    

# def details(n,a):
#     print('Hey '+n +'! Your Age is'+str(a))
# n=input('Enter your Name: ')
# a=input('Enter your Age: ')
# details(n,a)

# def r(x,y):
#     return x*y
# print(r(5,6))

def z(p,q):
    return p*q,p+q
p=int(input())
q=int(input())
print(z(p,q))