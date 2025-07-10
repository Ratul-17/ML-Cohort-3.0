#while loop 
i=1
while i<10:
    print(i)
    i +=1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #we can stop the current iteration
  print(i)

i=1
while i<6:
   print(i)
   i+=1
else: #we can run a block of code once when the condition no longer is true:
   print("i is no longer less than 6")
print()   
#nested loop (assignment)
#1
number="*"
for i in range(5):
   print(number*4)
print() #mane new line print hobe ekta break akare
#2

number="*"
for i in range(1,5):
    print (number*i)
         
#3   
for i in range (5):
    print(str (i)*i,) 
#4
for i in range(5):
    for j in range (i):
        print(2*j+1, end=" ")
    print() 