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
