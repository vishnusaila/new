#!/usr/bin/env python
# coding: utf-8

# In[27]:


"""1. Print All Prime Numbers from m to n
Problem: Given a range from m to n, print all prime numbers in that range.
Input: m = 10, n = 30
Output: 11 13 17 19 23 29
Explanation: A prime number has only two factors: 1 and itself."""
x=[i for i in range(10,30)  if all(i%j !=0 for j in range(2,i))]
print(x)
m=10
n=30
while True:
    for i in range(m,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    else:
        break


# In[45]:


"""2. Count of All Prime Numbers from m to n
Problem: Count how many prime numbers are there between m and n.
Input: m = 1, n = 10
Output: 4
Explanation: Prime numbers are: 2, 3, 5, 7"""
m=1
n=10
x=[i for i in range(m+1,n) if all (i%j!=0 for j in range(2,i))]
print(len(x))
print(x)
count=0
while True:
    for i in range(m,n):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                count+=1
    else:
        break
print(count)


# In[59]:


"""3. Print All Armstrong Numbers in a Range
Problem: Print all Armstrong numbers between m and n.
Input: m = 1, n = 500
Output: 1 153 370 371 407
Explanation: Armstrong number = sum of each digit raised to the power of number of digits."""
m=1
n=500
while True:
    for i in range(m,n+1):
        s=str(i)
        rr=i
        value=i 
        r=0
        if value>9:
            while value!=0:
                v=value%10
                value=value//10
                res=v**len(s)
                r+=res
        if r==i:
            print(i)
    else:
        break


# In[60]:


"""4. First Prime Number from m to n
Problem: Find the first prime number in the given range.
Input: m = 10, n = 25
Output: 11"""
m=10
n=25
for i in range(m,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        break


# In[61]:


"""5. Last Prime Number from m to n
Problem: Find the last prime number in the given range.
Input: m = 10, n = 25
Output: 23"""
m=10
n=25
for i in range(m,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s=i
print(s)
        


# In[64]:


"""6. First Vowel in a Name
Problem: Given a string, find the first vowel in the string.
Input: name = "Krishna"
Output: i
Explanation: First vowel from left is ‘i’"""
name="Krishna"
for i in name:
    if i in "aeiouAEIOU":
        print(i)
        break


# In[65]:


"""7. Last Vowel in a Name
Problem: Given a string, find the last vowel in the string.
Input: name = "Ramakrishna"
Output: a
Explanation: Last vowel is ‘a’"""
name="ramaKrishna"
for i in name:
    if i in "aeiouAEIOU":
        k=i
print(k)


# In[ ]:


"""8. Print All Even Numbers Using Continue
Problem: Use continue statement to skip odd numbers and print only even numbers between 1 and n.
Input: n = 10
Output: 2 4 6 8 10"""
n=10
i=1
while n>=i:
    if i%2==1:
        continue
    else:
        print(i)
    i+=1


# In[1]:


print("ram")


# In[ ]:





# In[ ]:


"""Interview Questions – Logic-Based Programs
________________________________________
🔢 Prime and Armstrong Logic Questions


________________________________________

________________________________________

________________________________________
9. Print All Odd Numbers Using Continue
Problem: Use continue statement to skip even numbers and print only odd numbers.
Input: n = 10
Output: 1 3 5 7 9
________________________________________
10. Count of Prime and Composite Numbers from m to n
Problem: Count how many are prime and how many are composite numbers in range m to n.
Input: m = 1, n = 10
Output: Prime: 4, Composite: 4
Explanation: Prime: 2,3,5,7 | Composite: 4,6,8,9
________________________________________
Would you like to: - 🐍 Add code for these too? - 📥 Merge this into your main pattern document? - ➕ Add more logic/interview questions?
"""

