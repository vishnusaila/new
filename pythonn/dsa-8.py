#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""1. Add an Element to a List
Problem: Write a function to add an element to a list. Explanation: Use append() to add the element to the end. 
Input: [1, 2, 3], add 4 Output: [1, 2, 3, 4]
"""
l=[1,2,3]
l.append(4)
print(l)


# In[3]:


"""2. Remove an Element from a List
Problem: Write a function to remove a specific element from a list. Explanation: Use remove() or pop() if index is known
Input: [1, 2, 3, 4], remove 3 Output: [1, 2, 4]
"""
l=[1,2,3,4]
l.remove(3)
print(l)


# In[4]:


"""3. Find Maximum in List
Problem: Find the maximum value in a list. Explanation: Use max() or iterate manually. Input: [4, 7, 1, 9] Output: 9
"""
l=[4,7,1,9]
k=l[0]
for i in l:
    if i>k:
        k=i
print(k)


# In[5]:


"""4. Find Minimum in List
Problem: Find the minimum value in a list. Explanation: Use min() or iterate manually. Input: [4, 7, 1, 9] Output: 1
_"""
l=[4,7,1,9]
k=l[0]
for i in l:
    if i<k:
        k=i
print(k)


# In[6]:


"""5. Sum of All Elements in List
Problem: Write a function to find the sum of all list elements. Explanation: Use sum() or loop to add all items. 
Input: [1, 2, 3] Output: 6
"""
l=[1,2,3]
s=0
i=0
while i<len(l):
    s+=l[i]
    i+=1
print(s)


# In[7]:


"""6. Count Occurrence of an Element
Problem: Count how many times a value appears in a list. Explanation: Use count() method. Input: [1, 2, 2, 3, 2], value 2
Output: 3
"""
l=[1,2,2,3,2]
print(l.count(2))


# In[1]:


"""7. Reverse a List
Problem: Write a function to reverse the order of list elements. Explanation: Use slicing or reverse() method. 
Input: [1, 2, 3] Output: [3, 2, 1]
"""
l=[1,2,3]
s=[]
i=0
while i<len(l):
    s.insert(0,l[i])
    i+=1
print(s)


# In[3]:


"""8. Sort a List
Problem: Write a function to sort a list in ascending order. Explanation: Use sort() or sorted(). Input: [4, 1, 3, 2] 
Output: [1, 2, 3, 4]
"""
l=[4,1,3,2]
l.sort()
print(l)


# In[5]:


"""9. Remove Duplicates from a List
Problem: Eliminate duplicate values. Explanation: Use set() or manual loop. Input: [1, 2, 2, 3] Output: [1, 2, 3]
"""
l=[1, 2, 2, 3]
i=0
l1=[]
while i<len(l):
    if l[i] not in l1:
        l1.append(l[i])
    i+=1
print(l1)


# In[8]:


"""10. Merge Two Lists
Problem: Merge two lists into one. Explanation: Use + operator or extend(). Input: [1, 2], [3, 4] Output: [1, 2, 3, 4]
"""
l1=[1,2]
l2=[3,4]
print(l1+l2)
l1.extend(l2)
print(l1)


# In[14]:


"""11. Find Common Elements in Two Lists
Problem: Return common elements between two lists. Explanation: Use set() and & or loops. Input: [1, 2, 3], [2, 3, 4] 
Output: [2, 3]
"""
l1=[1,2,3]
l2=[2,3,4]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)


# In[30]:


"""12. Print Even Numbers in a List
Problem: Print only even numbers from a list. Explanation: Use modulo condition in a loop. Input: [1, 2, 3, 4] Output: [2, 4]
"""
l1=[1,2,3,4]
i=0
even=[]
while i<len(l1):
    if l1[i]%2==0:
        even.append(l1[i])
    i+=1
print(even)


# In[33]:


"""13. Print Odd Numbers in a List
Problem: Print only odd numbers from a list. Input: [1, 2, 3, 4] Output: [1, 3]
"""
l1=[1,2,3,4]
i=0
odd=[]
while i<len(l1):
    if l1[i]%2==1:
        odd.append(l1[i])
    i+=1
print(odd)


# In[38]:


"""14. Check if List is Palindrome
Problem: Check if the list reads the same forwards and backwards. Input: [1, 2, 1] Output: True
"""
l1=[1,2,1]
l2=[]
i=0
while i<len(l1):
    l2.insert(0,l1[i])
    i+=1
if l1==l2:
    print(True)
else:
    print(False)


# In[2]:


"""15. Count Positive, Negative, Zero
Problem: Count the number of positive, negative and zero values in a list. Input: [0, -1, 2, -3, 4] Output: Positive: 2, 
Negative: 2, Zero: 1
"""
n=0
p=0
z=0
l=[0,-1,2,-3,4]
i=0
while i<len(l):
    if l[i]<0:
        n+=1
    elif l[i]>0:
        p+=1
    else:
        z+=1
    i+=1
print(f" Positive: {p}\n Negative: {n}\n Zero: {z}")


# In[28]:


"""16. Find Second Largest Number in List
Problem: Find the second highest value. Input: [1, 3, 4, 5, 0] Output: 4
"""
l=[200,203,201,199,202]
l.sort()
sh=l[0]
h=l[0]
i=0
while i<len(l):
    if l[i]>h:
        sh=h
        h=l[i] 
    i+=1
print(sh)


# In[30]:


"""17. Find Second Smallest Number in List
Problem: Find the second lowest value. Input: [5, 1, 4, 2, 3] Output: 2
"""
l=[200,203,201,199,202]
sh=l[0]
h=l[0]
i=0
while i<len(l):
    if l[i]<h:
        sh=h
        h=l[i] 
    i+=1
print(sh)


# In[34]:


"""18. Copy List to Another List
Problem: Copy the contents of one list to another. Explanation: Use slicing or copy(). Input: [1, 2, 3] Output: [1, 2, 3]
"""
l1=[1,2,3]
l2=l1.copy()
print(l2)


# In[37]:


"""19. Print All Prime Numbers in List
Problem: Print all prime numbers from a list. Input: [1, 2, 3, 4, 5] Output: [2, 3, 5]
"""
l=[1,2,3,4,5]
for i in l:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")


# In[41]:


"""20. Replace All Zeroes with a Given Number
Problem: Replace every zero with a specific value (e.g., -1). Input: [0, 2, 0, 4], replace with -1 Output: [-1, 2, -1, 4]
"""
i=0
l=[0,2,0,4]
l1=[]
while i<len(l):
    if l[i]==0:
        l1.insert(l[i+1],-1)    
    else:
        l1.append(l[i])
    i+=1
print(l1)


# In[15]:


"""21. Check if All Elements Are Same
Problem: Check whether all elements in the list are identical. Input: [5, 5, 5, 5] Output: True
"""
l=[5,5,5, 5]
k=l[0]
i=0
res=True
while i<len(l):
    if k not in l:
        res=False
        break
    else:
        res=True
    i+=1
print(res) 


# In[4]:


"""22. Find Frequency of All Elements
Problem: Return a dictionary with the frequency of each element. Input: [1, 2, 2, 3, 1] Output: {1: 2, 2: 2, 3: 1}
"""
d={}
l=[1,2,2,3,1]
for i in l:
    d[i]=l.count(i)
print(d)


# In[5]:


"""23. Flatten a Nested List
Problem: Convert a nested list into a single list. Input: [[1, 2], [3, 4]] Output: [1, 2, 3, 4]
"""
l=[[1, 2], [3, 4]]
l1=[]
for i in l:
    for j in i:
        l1.append(j)
print(l1)
        


# In[6]:


"""24. Split a List into Even and Odd Lists
Problem: Separate even and odd numbers into different lists. Input: [1, 2, 3, 4, 5] Output: Even: [2, 4], Odd: [1, 3, 5]
"""
even=[]
odd=[]
l=[1,2,3,4,5]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even:",even)
print("odd:",odd)


# In[19]:


"""25. Find Pair of Elements with Given Sum
Problem: Find all pairs in the list whose sum equals a given value. Input: [1, 2, 3, 4], sum = 5 Output: [(1, 4), (2, 3)]
"""
l=[1, 2, 3, 4]
k=[]
for i in l:
    for j in l:
        if i+j==5:
            k.append((i,j))
print(k)


# In[21]:


"""26. Remove All Odd Numbers
Problem: Remove all odd numbers from the list. Input: [1, 2, 3, 4, 5] Output: [2, 4]
"""
l=[1, 2, 3, 4, 5]
i=0
while i<len(l):
    if l[i]%2==1:
        l.remove(l[i])
    i+=1
print(l)


# In[22]:


"""27. Remove All Even Numbers
Problem: Remove all even numbers from the list. Input: [1, 2, 3, 4, 5] Output: [1, 3, 5]
"""
l=[1, 2, 3, 4, 5]
i=0
while i<len(l):
    if l[i]%2==0:
        l.remove(l[i])
    i+=1
print(l)


# In[9]:


"""28. Multiply All Elements by a Number
Problem: Multiply every element in the list by a fixed number. Input: [1, 2, 3], multiply by 2 Output: [2, 4, 6]"""
l=[1,2,3]
i=0
l1=[]
while i<len(l):
    l1.append(l[i]*2)
    i+=1
print(l1)


# In[1]:


"""29. Find Difference Between Max and Min
Problem: Return the difference between the largest and smallest element. Input: [4, 2, 7, 1] Output: 6
"""
l=[4,2,7,1]
i=0
low=l[0]
high=l[0]
while i<len(l):
    if l[i]>high:
        high=l[i]
    if l[i]<low:
        low=l[i]
    i+=1
print(high-low)


# In[11]:


"""30. Check if a List is Empty
Problem: Write a function that returns True if the list is empty, else False. Input: [] Output: True
"""
l=[]

def fun(l):
    k=True
    if l:
        k=False
    else:
        k=True
    return k
l=[]
fun(l)


# In[1]:


"""31. Insert Element at Specific Index
Problem: Insert a value at a specific position. Input: [1, 2, 4], insert 3 at index 2 Output: [1, 2, 3, 4]
"""
l=[1, 2, 4]
i=0

l.insert(2,3)
print(l)


# In[2]:


"""32. Remove All Instances of a Value
Problem: Remove all occurrences of a specific value. Input: [1, 2, 2, 3], remove 2 Output: [1, 3]
"""
l=[1, 2, 2, 3]
i=0
while i<len(l):
    if l[i]==2:
        l.remove(2)
    i+=1
print(l)


# In[4]:


"""33. Get Index of an Element
Problem: Return the index of a given value. Input: [10, 20, 30], find index of 20 Output: 1
"""
l=[10, 20, 30]
print(l.index(20))


# In[7]:


"""34. Square All Elements in a List
Problem: Return a list with each element squared. Input: [1, 2, 3] Output: [1, 4, 9]
"""
l=[1,2,3]
l1=[]
i=0
while i<len(l):
    l1.append(l[i]**2)
    i+=1
print(l1)


# In[8]:


"""35. Filter Out Negative Numbers
Problem: Remove all negative values from the list. Input: [-1, 2, -3, 4] Output: [2, 4]
"""
l=[-1, 2, -3, 4]
i=0
while i<len(l):
    if l[i]<0:
        l.remove(l[i])
    i+=1
print(l)


# In[ ]:


"""36. Get Elements Greater Than a Value
Problem: Return elements greater than a specified number. Input: [1, 5, 8, 3], greater than 4 Output: [5, 8]
"""


# In[ ]:





# In[ ]:





# In[ ]:


"""List-Based Interview Questions – Logic & Practice


________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
________________________________________
37. Find Duplicates in List
Problem: Return a list of duplicated values. Input: [1, 2, 2, 3, 3, 4] Output: [2, 3]
________________________________________
38. Rotate List Elements Right
Problem: Rotate list by k positions to the right. Input: [1, 2, 3, 4], k = 2 Output: [3, 4, 1, 2]
________________________________________
39. Check If List Contains a Value
Problem: Return True if list contains a specific value. Input: [1, 2, 3], check 2 Output: True
________________________________________
40. Chunk List into Smaller Lists
Problem: Break a list into chunks of given size. Input: [1, 2, 3, 4, 5, 6], chunk size 2 Output: [[1, 2], [3, 4], [5, 6]]
________________________________________
Would you like to: - 🐍 Add Python code for each question? - 📥 Export this as a PDF? - ➕ Add nested lists or matrix-based problems?
"""

