#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1. Area of Square
Question: Calculate the area of a square. - 
Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25"""
area=5*5
print(area)


# In[ ]:





# In[2]:


"""2. Area of Rectangle
Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - 
Input: - Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24
"""
arectangle=6*4
print(arectangle)


# In[4]:


"""3.   Area of Triangle
Question: Calculate the area of a triangle using base and height. -Formula: Area = (1/2)×base×height 
- Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0
"""

base=8
height=5
atriangle=0.5*base*height
print(atriangle)


# In[5]:


"""4. Perimeter of Square
Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - 
Input: - Side = 6 - Output: - Perimeter of square is: 24
_"""
side=6
psquare=4*side
print(psquare)


# In[7]:


"""5. Perimeter of Rectangle
Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) -
Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16
"""
length=5
breadth=3
prectangle=(length+breadth)*2
print(prectangle)


# In[9]:


"""6. Perimeter of Triangle
Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 - 
Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18
_"""
side1=5
side2=6
side3=7
ptriangle=side1+side2+side3
print(ptriangle)


# In[16]:


"""7. Break Amount into 1000s, 500s, and Remaining Change
Question: Break the total amount into denominations. - Input: - Amount = 3700 - 
Output: - 1000s: 3 - 500s: 1 - Remaining: 200
"""
amount=3700
t=amount//1000
amount=3700%1000
f=amount//500
amount=amount%500
print(f"1000 notes: {t}, 500 notes: {f}, remaining change : {amount}" )


# In[18]:


"""8. Convert Seconds into Hours, Minutes, and Seconds
Question: Convert total seconds into hours, minutes, and seconds. - 
Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
"""
seconds=3672
h=seconds//3600
seconds=seconds%3600
m=seconds//60
seconds=m%60
print(f" hours: {h}, minutes: {m}, seconds: {seconds}")


# In[19]:


"""9. Sum of Marks (Maths, Physics, Chemistry)
Question: Calculate the sum of marks in 3 subjects. - 
Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263
"""
math=85
physics=90
chemistry=88
cal=math+physics+chemistry
print(cal)


# In[20]:


"""10. Average of Marks (Maths, Physics, Chemistry)
Question: Calculate the average of marks in 3 subjects. -
Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67
"""
math=85
physics=90
chemistry=88
avarage=math+physics+chemistry/3
print(avara)


# In[ ]:




