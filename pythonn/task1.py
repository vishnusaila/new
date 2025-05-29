#.Count how many numbers between 1 and 50 are divisible by 7
for i in range(1,50):
    if i%7==0:
        print(i)
#Print the factorial of a number (e.g., 5!) using a for loop
fact=1
for i in range(1,6):
    fact=fact*i
    print(fact)
#print all numbers b/w 1 to 40 which are divisible by both 5 and 7
for i in range(1,40):
    if i%5==0 and i%7==0:
        print(i)
