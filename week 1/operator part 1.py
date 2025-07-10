
#task1

x = input("Enter value of x: ")
y = input("Enter value of y: ")
z = input("Enter value of z: ")


if x >= y and x >= z:
    print("x is the largest:", x)
elif y >= x and y >= z:
    print("y is the largest:", y)
else:
    print("z is the largest:", z)

#task2
x=float(input("enter the 1st frnd cgpa: "))
y=float(input("enter the 2nd frnd cgpa: "))
z=float(input("enter the 3rd frnd cgpa: "))

if x >= y and x >= z:
    print("x is the largest:", x)
elif y >= x and y >= z:
    print("y is the largest:", y)
else:
    print("z is the largest:", z)


#task 3
a=7
b=4
c= a ^ b
print(c)