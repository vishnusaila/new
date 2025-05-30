"""#variables
#interning
#memory pulling
#print() it is user defined method
#id() it is nothing but a address of an object
#type method it is used to define a datatype like that data type belonging to which datatype
#  integers 
# data types" -- primitive data types" (single value,can't change )
#numbers
a=10 #integer 
b=2.3 #float
c=3j #complex
print(type(a))
print(type(b))
print(type(c))
#string
m="krishna"
print(type(m))
#none
n="none"
print(type(n))
#boolean
k=True
print(type(k))

#non-primitive data types(complex , multiple values)
#list
aa=[2,"rama",2.1]
#tuple
b=(3,4,5,1,"ram",4.3)
#set
c={"ram","ram"}
#dict
d={"siva":323,"rama":323,"ramu":232,"sita":323,"siva":"pilla"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a=10
print(id(a))
b=20
c=20
print(id(b))
print(id(c))
print(aa[1])
aa.append("rama")

bb=[2,"rama",2.1]
cc=[2,"rama",2.1]
nn=1
mm=1
print(id(bb))
print(id(cc))
print(id(nn))
print(id(mm))"""

from flask import Flask, render_template, request, redirect, url_for
import random as re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='')

@app.route('/guess', methods=['POST'])
def guess():
    u = int(request.form['number'])
    while True:
        if u>=0 and u<=9:
            ram=re.randint(1,9)
            print(ram)
            if ram==u:
                message = "🎉 Congratulations! You guessed the number."
                break
            else:
                u=int(input("Try again :"))
        else:
            message="Please Kindly enter Numbers Between 0 to 9 Only"
            break


    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)



