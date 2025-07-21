#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1. Check Even or Odd
Question: Determine whether a number is even or odd. Explanation: A number is even 
if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number
"""
n=int(input("enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")


# In[3]:


"""2. Divisible by 5 but Not by 10
Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check
if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy
"""
n=25
if n%5==0 and n%10!=0:
    print("divisible by 5 but not by 10")
else:
    print("not divisible by 5 but not by 10")


# In[4]:


"""3. Biggest Among Two Numbers
Question: Find the biggest number among two. Explanation: Use comparison operators (>) 
to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7
"""
n1=int(input())
n2=int(input())
if n1>n2:
    print(n1,"is big")
else:
    print(n2,"is big")


# In[5]:


"""4. Smallest Among Two Numbers
Question: Find the smallest number among two. Explanation: Use comparison operators (<) 
to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4
"""
n1=int(input())
n2=int(input())
if n1>n2:
    print(n2,"is small")
else:
    print(n1,"is small")


# In[6]:


"""5. Divisible by 2, 3, and 6
Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible
by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy
"""
n=int(input("enter a number:"))
if n%2==0 and n%3==0 and n%6==0:
    print("satisfy")
else:
    print("not satisfy")


# In[7]:


"""6. Voting Eligibility
Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible
to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote
"""
age=int(input("enter a age:"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
    


# In[9]:


"""7. Student Pass/Fail Based on All Subjects >= 35
Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation:Student 
passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30
"""
m=int(input("enter a math marks:"))
p=int(input("enter a physics marks:"))
c=int(input("enter a chemistry marks:"))
if m>=35 and p>=35 and c>=35:
    print("pass")
else:
    print("fail")


# In[10]:


"""8. Student Pass if Passed Any One Subject (>= 35)
Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if 
any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25
"""
m=int(input("enter a math marks:"))
p=int(input("enter a physics marks:"))
c=int(input("enter a chemistry marks:"))
if m>=35 or p>=35 or c>=35:
    print("pass")
else:
    print("fail")


# In[12]:


"""9. Student Pass if Passed Any Two Subjects
Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or 
logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 
"""
m=int(input("enter a math marks:"))
p=int(input("enter a physics marks:"))
c=int(input("enter a chemistry marks:"))
if (m>=35 and p>=35) or (m>=35 and c>=35) or (p>=35 and m>=35) or (p>=35 and c>=35):
    print("pass")
else:
    print("fail")


# In[14]:


"""10. Biggest Among Three Numbers
Question: Find the biggest number among three. Explanation: Compare each pair of numbers using 
if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9
"""
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
if a>b and a>c:
    print(a,"is big")
elif b>a and b>c:
    print(b,"is big")
else:
    print(c,"is big")


# In[16]:


"""11. Smallest Among Three Numbers
Question: Find the smallest number among three. Explanation: Use comparison logic to determine the 
minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4
"""
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
if a<b and a<c:
    print(a,"is small")
elif b<a and b<c:
    print(b,"is small")
else:
    print(c,"is small")


# In[28]:


"""12. Perfect Square or Not
Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the
square of its square root equals the number. - Input: Number = 49 - Output: Perfect square
"""
n=int(input("enter a number:"))
res="Not Perfect"
for i in range(n):
    s=i*i
    if s==n:
        res="Perfect"
        break
    else:
        res="Not Perfect"
print(res)


# In[30]:


"""13. Cars Required for Members (Max 5 per car)
Question: Calculate how many cars are needed for a given number of people. Explanation: Divide 
total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4
"""
members=int(input("enter a number of peopel"))
print(((members+4)//5),"cars needed")


# In[40]:


"""14. Second Biggest Among Three Numbers
Question: Find the second largest number among three inputs. Explanation: Use sorting or nested
conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second bigges18
"""
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
if a>b and a>c:
    if b>c:
        print(b,"is 2nd big")
    else:
        print(c,"is 2nd big")
elif b>a and b>c:
    if a>c:
        print(a,"is 2nd big")
    else:
        print(c,"is 2nd big")
else:
    if a>b:
        print(a,"is 2nd big")
    else:
        print(b,"is 2nd big")


# In[50]:


"""15. Leap Year or Not
Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible 
by 4,and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
"""
year=int(input("enter a year:"))
if (year%4==0 and (year%100!=0 or year%400==0)):
    print("leap year")
else:
    print("not a leap year")


# In[ ]:




