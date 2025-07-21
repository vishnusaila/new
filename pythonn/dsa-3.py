#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""1. Print Numbers from 1 to n
Question: Write a program to print numbers from 1 to n. Explanation: Use a loop starting from 1 
to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5
"""
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i,end=" ")
i=1
print()
while n>=i:
    print(i,end=" ")
    i+=1


# In[35]:


"""2. Print Numbers from m to n
Question: Write a program to print numbers from m to n. Explanation: Loop from m to n
and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7
"""
for i in range(3,7):
    print(i,end=" ")
i=3
print()
while i<7:
    print(i,end=" ")
    i+=1


# In[39]:


"""3. Print Numbers from n to 1 in Reverse
Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop 
starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1
"""
for i in range(5,0,-1):
    print(i,end=" ")
print()
i=5
while i!=0:
    print(i,end=" ")
    i-=1


# In[43]:


"""4. Print Numbers from n to m in Reverse
Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n 
and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6
"""
for i in range(10,5,-1):
    print(i,end=" ")
print()
i=10
while i!=5:
    print(i,end=" ")
    i-=1


# In[42]:


n=10
num=2
while n!=0:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num,end=" ")
        n-=1
    num+=1


# In[52]:


"""5. Sum of n Natural Numbers
Question: Write a program to calculate the sum of first n natural numbers. Explanation: 
Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15
"""
s=0
for i in range(6):
    s+=i
print(s)
ss=[i for i in range(6)]
print(sum(ss))


# In[59]:


"""6. Factorial of a Number
Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers
from 1 to n. - Input: n = 5 - Output: 120
"""
s=1
for i in range(5):
    s+=s*i
print(s)
ss=[x for x in range(1,6)]
print(ss)


# In[60]:


"""7. Sum of m to n Numbers
Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to
n and add values. - Input: m = 3, n = 6 - Output: 18
"""
s=0
for i in range(3,7):
    s+=i
print(s)


# In[84]:


"""8. Product of m to n Numbers
Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m 
to n and multiply values. - Input: m = 2, n = 4 - Output: 24
"""
s=1
for i in range(2,5):
    s=s*i
print(s)


# In[80]:


s=1
for i in range(2,5):
    s*=i
print(s)


# In[86]:


"""9. Print Factors of a Number
Question: Write a program to print all factors of a given number. Explanation: Check divisibility 
of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6
"""
n=6
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


# In[88]:


"""10. Count of Factors
Question: Write a program to count how many factors a number has. Explanation: Increment count
when divisible. - Input: n = 6 - Output: 4
"""
n=6
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)


# In[5]:


"""12. Even Numbers from m to n
Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - 
Input: m = 3, n = 10 - Output: 4 6 8 10
"""
for i in range(3+1,11,2):
    print(i,end=" ")
s=[x for x in range(3,11) if x%2==0]
print(s)


# In[8]:


"""13. Odd Numbers from m to n
Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9
"""
for i in range(3,10,2):
    print(i,end=" ")
s=[x for x in range(3,10) if x%2==1]
print(s)


# In[9]:


"""14. Count of Even and Odd Numbers
Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even 
and odd. - Input: m = 3, n = 7 -Output: Even = 2, Odd = 3
"""
even=0
odd=0
for i in range(3,7+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even:",even   ,"odd:",odd)


# In[11]:


"""15. Reverse a String
Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”
"""
s="Hello"
res=''
for i in s:
    res=i+res
print(res)


# In[14]:


"""16. Check for Palindrome String
Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome
"""
s=input("enter a string")
res=''
for i in s:
    res=i+res
if s==res:
    print("polindrome")
else:
    print("not a polindrome")


# In[19]:


"""17. Sum of Digits
Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6
"""
n=int(input("enter a number:"))
s=0
while n!=0:
    m=n%10
    s+=m
    n=n//10
print(s)    


# In[23]:


"""18. Product of Digits
Question: Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6
"""
p=1
n=int(input("enter a number:"))
while n!=0:
    m=n%10
    n=n//10
    p=p*m
print(p)


# In[30]:


"""Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime"""
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")


# In[34]:


"""19. Armstrong Number Check
Question: Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - 
Input: 153 - Output: Armstrong number
"""
n=int(input("enter a number:"))
k=len(str(n))
count=0
while n!=0:
    m=n%10
    n=n//10
    s=m*k
if s==k:
    print("armstrong")
else:
    print("not armstrong")


# In[35]:


"""20. Reverse a Number
Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321
"""
k=0
n=int(input("enter a number:"))
while n!=0:
    m=n%10
    n=n//10
    k=k*10+m
print(k)


# In[37]:


"""21. Palindrome Number Check
Question: Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome
"""
k=0
n=int(input("enter a number:"))
s=n
while n!=0:
    m=n%10
    n=n//10
    k=k*10+m
if k==s:
    print("polindrome")
else:
    print("not a polindrome")


# In[38]:


"""22. Count Vowels in String
Question: Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2
"""
s="ramkrishna"
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1
print(count)


# In[39]:


"""23. Count Consonants in String
Question: Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 3
"""
s="ramkrishna"
count=0
for i in s:
    if i not in "aeiouAEIOU":
        count+=1
print(count)


# In[40]:


"""24. Count Vowels and Consonants
Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - 
Output: Vowels = 2, Consonants = 3
"""
s="ramkrishna"
consonent=0
vowel=0
for i in s:
    if i not in "aeiouAEIOU":
        consonent+=1
    else:
        vowel+=1
print("consonents",consonent)
print("vowels",vowel)


# In[41]:


"""25. Perfect Number Check
Question: Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - 
Output: Perfect number
_"""
s=0
n=int(input("enter a number:"))
for i in range(1,n):
    if n%i==0:
        s+=i
if n==s:
    print("perfect number")
else:
    print("not a perfect number")


# In[1]:


"""26. Neon Number Check
Question: Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - 
Input: 9 - Output: Neon number
"""
n=int(input("enter a number:"))
m=n**2
s=0
while m!=0:
    l=m%10
    m//=10
    s+=l
if s==n:
    print("neon number")
else:
    print("non neon number")


# In[60]:


"""27. Strong Number Check
Question: Check if a number is a strong number. Explanation: Sum of factorial of digits equals the number. - 
Input: 145 - Output: Strong number
"""
m=int(input("enter a number:"))
t=m
s=0
while m!=0:
    l=m%10
    m//=10
    p=1
    for i in range(1,l+1):
        p=p*i
    s+=p
if s==t:
    print("strong")
else:
    print("not strong")


# In[62]:


"""28. Harshad Number Check
Question: Check if a number is divisible by the sum of its digits. Explanation: Calculate digit sum and check divisibility.
- Input: 18 - Output: Harshad number
"""
n=int(input("enter a number:"))
l=n
s=0
while n!=0:
    m=n%10
    n=n//10
    s+=m
if l%s==0:
    print("harshad")
else:
    print("not hardhad")


# In[65]:


"""29. Fibonacci Series
Question: Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - 
Input: n = 5 - Output: 0 1 1 2 3
"""
a=0
b=1
n=int(input("enter a number"))
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


# In[ ]:


"""30. Check for Neon Number (Repeated)
Question: Again, check for a neon number (example). Explanation: Square number and sum digits. - Input: 9 -
Output: Neon number
"""
class Neon:
    def repet(self,n):
        self.n=n
        self.k=self.n
        self.s=0
        while self.n!=0:
            self.m=n%10
            self.n=n//10
            self.s+=self.m
        if self.k==self.s:
            print("Neon number")
        else:
            print("not a neno number")
obj=Neon()
while True:
    print("if u want to continue enter 1 else enter 0")
    option=int(input("enter a number:"))
    if option==1:
        n=int(input("enter a number:"))
        obj.repet(n)
    elif option==0:
        break
    else:
        print("enter valid option:")


# In[ ]:





# In[ ]:





# In[ ]:




