#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""1.	Solid Square Pattern
Problem: Print a solid square of stars of size n.
Input: n = 4"""
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()


# In[8]:


"""2.	Solid Rectangle Pattern
Problem: Print a solid rectangle of m rows and n columns.
Input: m = 3, n = 5"""
for i in range(3):
    for j in range(5):
        print("*",end=" ")
    print()


# In[10]:


"""3.	Right-Angled Triangle (Left-Aligned)
Problem: Print a left-aligned right-angled triangle.
Input: n = 5"""
for i in range(5+1):
    for j in range(i):
        print("*",end=" ")
    print()


# In[14]:


"""4.	Right-Angled Triangle (Right-Aligned)
Input: n = 5"""
for i in range(5+1):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()


# In[15]:


"""5.	Inverted Triangle (Left-Aligned)
Input: n = 5"""
for i in range(5+1):
    for j in range(5-i):
        print("*",end=" ")
    print()


# In[17]:


"""6.	Inverted Triangle (Right-Aligned)
Input: n = 5"""
for i in range(5+1):
    for j in range(i):
        print(" ",end=" ")
    for k in range(5-i):
        print("*",end=" ")
    print()


# In[33]:


"""7.	Centered Pyramid Pattern
Input: n = 4"""
i=1
for i in range(5+1):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i*2-1):
        print("*",end=" ")
    print()


# In[114]:


"""8.	Diamond Pattern
Input: n = 3"""
n=3
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i*2-1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range((n-i)*2-1):
        print("*",end=" ")
    print( )


# In[188]:


"""9.	Butterfly Pattern
Input: n = 4"""
n=4
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    for k in range((n-1-i)*2):
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-1-i):
        print("*",end=" ")
    for k in range((i)*2):
        print(" ",end=" ")
    for l in range(n-1-i):
        print("*",end=" ")
    print()


# In[196]:


"""10.	Left-Aligned Half Diamond
Input: n = 4"""
n=4
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print( )
for i in range(n):
    for j in range(n-1-i):
        print("*",end=" ")
    print()


# In[24]:


"""11.	Right-Aligned Half Diamond
Input: n = 4"""
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(n-i-1):
        print("*",end=" ")
    print( )


# In[1]:


"""12.	Sandglass Pattern
Input: n = 4"""
n=4
for i in range(n+1):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i+1):
        print("*",end=" ")
    print( )
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()


# In[2]:


"""13.	Increasing Width Triangle
Input: n = 5"""
n=4
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print( )


# In[3]:


"""14.	Decreasing Width Triangle
Input: n = 5"""
n=5
for i in range(n):
    for j in range(n-1-i):
        print("*",end=" ")
    print()


# In[4]:


"""15.	Right-Aligned Hill Pattern
Input: n = 4"""
n=4
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()


# In[238]:


"""16.	Hollow Square Pattern
Problem: Print a hollow square of stars of size n.
Input: n = 4"""
n=4
for i in range(n):
    for j in range(1):
        print("+",end=" ")
    for k in range(2):
        print(" ",end=" ")
    for l in range(1):
        print("*",end=" ")
    print()


# In[239]:


n=4
for i in range(4):
    for j in range(n):
        if (i==1 and j==1)or(i==1 and j==2)or(i==2 and j==1)or(i==2 and j==2):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[240]:


"""17.	Hollow Rectangle Pattern
Problem: Print a hollow rectangle of m rows and n columns.
Input: m = 4, n = 5"""
for i in range(4):
    for j in range(5):
        if (i==1 and j==1)or(i==1 and j==2)or(i==2 and j==1)or(i==2 and j==2)or (i==1 and j==3)or (i==2 and j==3):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[241]:


"""18.	Hollow Right-Angled Triangle (Left-Aligned)
Input: n = 5"""
n=5
for i in range(n+1):
    for j in range(i):
        if (i==3 and j==1)or(i==4 and j==1)or(i==4 and j==2):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[242]:


"""19.	Hollow Right-Angled Triangle (Right-Aligned)
Input: n = 5"""
n=5
for i in range(n+1):
    for e in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        if (i==3 and j==1)or(i==4 and j==1)or(i==4 and j==2):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[243]:


"""20.	Hollow Inverted Triangle (Left-Aligned)
Input: n = 5"""
n=5
for i in range(n+1):
    for j in range(n-i):
        if (i==1 and j==1)or(i==1 and j==2)or(i==2 and j==1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[244]:


"""21.	Hollow Inverted Triangle (Right-Aligned)
Input: n = 5"""
n=5
for i in range(n+1):
    for k in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        if (i==1 and j==1)or (i==1 and j==2) or (i==2 and j==1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[245]:


"""22.	Hollow Pyramid Pattern
Input: n = 4"""
n=3
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range((i*2)+1):
        if (i==1 and k==1)or (i==2 and k==1)or(i==2 and k==3) or i==2 and k==2:
            print(" ",end=" ")
    
        else:
            print("*",end=" ")
    print()


# In[246]:


"""23.	Hollow Diamond Pattern
Input: n = 3"""
n=3
for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range((i*2)+1):
        if (i==1 and k==1) or (i==2 and k==1)or (i==2 and k==2) or (i==2 and k==3)or (i==3 and k==1)or (i==3 and k==2) or (i==3 and k==3):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print( )
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(((n)*2)-i-i-1):
        if (i==0 and k==1)or(i==0 and k==2)or(i==0 and k==3) or (i==1 and k==1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[247]:


n=3


# In[248]:


n=3
for i in range(n+1):
    for j in range(n-i):
        print(i,j,end= ", ")
    for k in range((i*2)+1):
        print((i,k),end=" ")
    print( )


# In[249]:


"""24.	Hollow Butterfly Pattern
Input: n = 4"""
n=4
for i in range(n+1):
    for j in range(i):
        if (i==3 and j==1)or(i==4 and j==1)or(i==4 and j==2):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    for k in range((n*2)-i-i-1):
        print(" ",end=" ")
    for l in range(i):
        if (i==3 and l==1) or (i==4 and l==0)or (i==4 and l==1) or(i==4 and l==3):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[250]:


n=4
for i in range((n*2)):
    for j in range(5):
        if(i==0 and j==1)or(i==0 and j==2)or(i==0 and j==3)or(i==1 and j==2)or(i==2 and j==1)or(i==2 and j==3)or((i==3)and (j==1 or j==2 or j==3))or((i==4)and (j==1 or j==2 or j==3))or(i==5 and j==1)or(i==5 and j==3)or(i==6 and j==2)or((i==7)and (j==1 or j==2 or j==3)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[251]:


n=4
for i in range(n*2):
    for j in range(5):
        print((i,j),end=" ")
    print()


# In[252]:


"""25.	Hollow Hourglass Pattern
Input: n = 5"""
n=5
for i in range(n+2):
    for j in range(5):
        if ((i==1)and(j==1 or j==2 or j==3))or(i==2 and j==2)or((i==2 or i==3 or i==4)and (j==0))or(i==3 and j==1)or(i==3 and j==3)or((i==2 or i==3 or i==4)and(j==4))or(i==4 and j==2)or((i==5)and(j==1 or j==2 or j==3)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# In[253]:


"""27.	left aligned Number Triangle
Input: n = 5"""
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[254]:


"""27.	Repeating Row Number Triangle
Input: n = 5"""
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


# In[255]:


"""28.	Continuous Number Triangle
Input: n = 4"""
n=4
m=1
for i in range(n+1):
    for j in range(i):
        print(m,end=" ")
        m+=1
    print()


# In[256]:


"""29.	Reverse Row Number Triangle
Input: n = 5"""
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i-j,end=" ")
    print()


# In[257]:


"""30.	Inverted Number Triangle
Input: n = 5"""
n=5
while n!=0:
    for i in range(n,0,-1):
        print(i,end=" ")
    print()
    n-=1


# In[258]:


"""31.	Right-Aligned Number Triangle
Input: n = 5"""
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()


# In[259]:


"""32.	Pyramid Number Pattern
Input: n = 4"""
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()


# In[260]:


"""33.	Even Number Triangle
Input: n = 5"""
n=5
for i in range(1,11,2):
    for j in range(1,i+2):
        if j%2==0:
            print(j,end=" ")
    print()


# In[261]:


"""34.	Odd Number Triangle
Input: n = 5"""
n=5
for i in range(1,11,2):
    for j in range(1,i+2):
        if j%2==1:
            print(j,end=" ")
    print()


# In[271]:


"""35.	Pascal’s Triangle
Input: n = 5"""
n=5
for i in range(1,n+1):
    for j in range(i):
        if (i==3 and j==1):
            print(2,end=" ")
        elif ((i==4)and(j==1 or j==2)):
            print(3,end=" ")
        elif ((i==5)and (j==1 or j==3)):
            print(4,end=" ")
        elif(i==5 and j==2):
            print(6,end=" ")
        else:
            print(1,end=" ")
    print()


# In[ ]:





# In[ ]:


"""
________________________________________
✅ All 35 pattern questions are now fully formatted in an interview-style layout with problem statements, inputs, and expected outputs.
Would you like to:
•	🐍 Add Python code for each?
•	📥 Export as a PDF?
"""

