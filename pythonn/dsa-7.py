#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""1. Remove Spaces from Given Text
Problem: Write a function to remove all spaces from the input string. Explanation: Remove any whitespace characters. 
Input: "he llo wor ld" Output: "helloworld"
__"""
s="he llo wor ld"
for i in s:
    if i==" ":
        pass
    else:
        print(i,end="")


# In[5]:


"""2. Reverse a String
Problem: Write a function to reverse the characters in a string. Input: "hello" Output: "olleh"
"""
s="hello"
ss=""
for i in s:
    ss=i+ss
print(ss)


# In[6]:


"""3. Reverse a String After Removing Spaces
Problem: Write a function to reverse a string after removing all spaces. Input: "he llo world" Output: "dlrowolleh"
"""
s= "he llo world"
ss=' '
for i in s:
    if i==" ":
        pass
    else:
        ss=i+ss
print(ss)


# In[8]:


"""4. Convert Snake Case to Camel Case
Problem: Convert a string from snake_case to camelCase. Input: "my_variable_name" Output: "myVariableName"
"""
s="my_variable_name"
i=0
ss=''
while i<len(s):
    if s[i]=="_":
        ss+=s[i+1].upper()
        i+=1
    else:
        ss+=s[i]
    i+=1
print(ss)


# In[10]:


"""5. Convert Snake Case to Pascal Case
Problem: Convert a string from snake_case to PascalCase. Input: "my_variable_name" Output: "MyVariableName"
"""
s="my_variable_name"
i=0
s=s.capitalize()
kk=""
while i<len(s): 
    if s[i]=="_":
        kk+=s[i+1].upper()
        i+=1
    else:
        kk+=s[i]
    i+=1
print(kk)


# In[17]:


"""6.Problem: Convert a string from camelCase to snake_case. Input: "myVariableName" Output: "my_variable_name"
"""
s="myVariableName"
ss=""
for i in range(len(s)):
    if s[i].isupper():
        ss+="_"
        ss+=s[i]
    else:
        ss+=s[i]
print(ss)


# In[50]:


"""7. Convert Camel Case to Pascal Case
Problem: Convert a string from camelCase to PascalCase. Input: "myVariable" Output: "MyVariable"
__"""
s="myVariable"
ss=" "
for i in s:
    if i.startswith("m"):
        ss+=i.upper()
    else:
        ss+=i
print(ss)


# In[63]:


"""8. Convert Pascal Case to Camel Case
Problem: Convert a string from PascalCase to camelCase. Input: "MyVariable" Output: "myVariable"
_"""
s="MyVariable"
ss=" "
for i in s:
    if s.startswith("M"):
        ss+=i.lower()
    else:
        ss+=i
print(ss)


# In[69]:


"""9. Convert Pascal Case to Snake Case
Problem: Convert a string from PascalCase to snake_case. Input: "MyVariable" Output: "my_variable"
"""
s="MyVariable"
ss=" "
for i in range(len(s)):
    if s[i].isupper() :
        ss+="_"
        ss+=s[i].lower()
    else:
        ss+=s[i]
print(ss[2:])       


# In[4]:


"""10. Convert Text to Camel Case
Problem: Convert a space-separated sentence into camelCase. Input: "hello world example" Output: "helloWorldExample"
"""
s="hello world example" 
ss=""
i=0
while i<(len(s)):
    if s[i]==" ":
        ss+=s[i+1].upper()
        i+=1
    else:
        ss+=s[i]
    i+=1
print(ss)


# In[11]:


"""11. Convert Text to Snake Case
Problem: Convert a space-separated sentence into snake_case. Input: "hello world example" Output: "hello_world_example"
"""
s="hello world example"
for i in s:
    if i==" ":
        print("_",end="")
    else:
        print(i,end="")
    


# In[14]:


"""12. Convert Text to Pascal Case
Problem: Convert a space-separated sentence into PascalCase. Input: "hello world example" Output: "HelloWorldExample"
"""
s="hello world example"
s=s.capitalize()
i=0
ss=" "
while i<(len(s)):
    if s[i]==" ":
        ss+=s[i+1].upper()
        i+=1
    else:
        ss+=s[i]
    i+=1
print(ss)


# In[18]:


"""13. Swap Upper and Lower Case
Problem: Swap the case of each letter in a given string. Input: "HeLLo" Output: "hEllO"
"""
s="Hello"
for i in s:
    if i.isupper():
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")
s.swapcase()


# In[56]:


"""14. Separate Digits from Text
Problem: Extract all digits from a given alphanumeric string. Input: "abc123d4" Output: "1234"
"""
s="abc123d4"
for i in s:
    if i.isalpha():  
        pass
    else:
        print(i,end=" ")


# In[81]:


"""15. Print Uppercase, Lowercase, Digits, and Special Characters Separately
Problem: Print each type of character separately from the string. Input: "Abc123!@#" Output:
Uppercase: A
Lowercase: b c
Digits: 1 2 3
Special Characters: ! @ #"""
s="Abc123!@#"
u=" "
l=" "
sp=" "
d=" "
for i in s:
    if (ord(i)>=33 and ord(i)<48) or (ord(i)>58 and ord(i)<65):
        sp+=i
    elif ord(i)>=48 and ord(i)<58:
        d+=i
    elif ord(i)>=65 and ord(i)<91:
        u+=i
    elif ord(i)>=97 and ord(i)<124:
        l+=i
print(f"upper: {u} \nlower: {l}\nspecial character: {sp}\ndigits: {d}")


# In[2]:


"""16. Count of Uppercase, Lowercase, Digits, and Special Characters
Problem: Count each type of character in a string. Input: "AbC@123x!" Output:
Uppercase: 2
Lowercase: 1
Digits: 3
Special Characters: 2"""
s="AbC@123x!"
u=0
l=0
sp=0
d=0
for i in s:
    if (ord(i)>=33 and ord(i)<48) or (ord(i)>58 and ord(i)<65):
        sp+=1
    elif ord(i)>=48 and ord(i)<58:
        d+=1
    elif ord(i)>=65 and ord(i)<91:
        u+=1
    elif ord(i)>=97 and ord(i)<124:
        l+=1
print(f"upper: {u} \nlower: {l}\nspecial character: {sp}\ndigits: {d}")


# In[6]:


"""17. Check Password Strength
Problem: Check if a password contains at least one uppercase, one lowercase, one digit, and one special character.
Input: "Pass123!" Output: "Strong Password"
"""
s= "Pass123!"
u=0
l=0
sp=0
d=0
for i in s:
    if (ord(i)>=33 and ord(i)<48) or (ord(i)>58 and ord(i)<65):
        sp+=1
    elif ord(i)>=48 and ord(i)<58:
        d+=1
    elif ord(i)>=65 and ord(i)<91:
        u+=1
    elif ord(i)>=97 and ord(i)<124:
        l+=1
print(f"upper: {u} \nlower: {l}\nspecial character: {sp}\ndigits: {d}")
if u>=1 and l>=1 and sp>=1 and d>=1:
    print("Strong")
else:
    print("weak")


# In[8]:


"""18. Remove Duplicates in a Given Input
Problem: Remove duplicate characters from a string. Input: aabbcc Output: abc"""
s="aabbcc"
ss=""
for i in s:
    if i not in ss:
        ss+=i
print(ss)


# In[17]:


"""19. Print Duplicates in a Given String
Problem: Identify and print duplicate characters in a string. Input: "aabbccde" Output: a b c"""
s="aabbccde"
ss=""
t=""
for i in s:
    if i not in ss:
        ss+=i
    elif i in ss:
        t+=i
print(ss)
print(t)  


# In[4]:


"""20. Print Next Characters in a Given String
Problem: Replace each character in the string with its next character. """
s="abc"
for i in s:
    print(chr(ord(i)+1),end="")


# In[ ]:




