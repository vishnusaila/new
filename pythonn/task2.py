#Print numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i,end=" ")
    i+=1
#Print even numbers between 1 and 50 using a while loop.
i=0
while i<=50:
    if i%2==0:
        print(i,end=" ")
    i+=1
#Print the multiplication table of a given number (e.g., 5) using a while loop.
i=1
while i<=10:
    print(i,"x","5","=",5*i)
    i+=1
#Calculate the sum of digits of a number using a while loop. e.g., 123 → 6
m=123
i=0
count=0
while i<=2:
    n=m%10
    count+=n
    m=m//10
    i+=1
print(count)
#Reverse a number using a while loop.e.g., 123 → 321
n=int(input("enter a number:"))
i=0
add=0
while i<=2:
    m=n%10
    add=add*10+m
    n=n//10
    i+=1
print(add) 
#Count the number of digits in a given number using a while loop.
m=int(input("enter a number"))
i=0
digit=1
while m>1:
    n=m%10
    m=m//10
    digit+=1  
print(digit)

#polindrome
m=232
p=m
polin=0
while m>1:
    n=m%10
    m=m//10
    polin+=n
if polin==p:
    print("polindrome")
else:
    print("not a polindrome")
#7.Print the Fibonacci series up to N terms using a while loop
n=5
i=0
feb=0
while i<=5:
    feb+=i
    print(feb)
    i+=1

#9 . Create a number guessing game using a while loop
import random as re

u=int(input("enter a number : "))
while True:
    if u>=0 and u<=9:
        ram=re.randint(1,9)
        print(ram)
        if ram==u:
            print("Congratulations")
            break
        else:
            u=int(input("Try again :"))
    else:
        print("Please Kindly enter Numbers Between 0 to 9 Only")
        break

# 10. Keep looping until the user guesses the correct number.
import random as re

u=int(input("enter a number : "))
while True:
    if u>=0 and u<=99:
        ram=re.randint(1,99)
        print(ram)
        if ram==u:
            print("Congratulations")
            break
        else:
            u=int(input("Try again :"))