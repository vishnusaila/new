#Display count down timer from 10 to 0 using while loop?
import time
i=10
while i>0:
    print(i)
    time.sleep(1)
    i-=1
#Find max digit in number s=2569 using while loop?
s = 2569
max_digit = 0

while s > 0:
    digit = s % 10        
    if digit > max_digit:
        max_digit = digit
    s = s // 10           
print("Maximum digit is:", max_digit)




#simulate a basic login system (max attempts 3)
inp=['kumar','202','84558906' ]
for i in range(3):
    k=input()
    if k in inp:
        print("Login Successfully")
        break
    else:
        print("try again")
else:
    inp.clear()
    print(inp)


