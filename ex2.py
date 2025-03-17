import random
x=random.randint(1,10)
print(x) 
found=0
while found==0:
   guess=input("Enter a number:")
   if guess == x:
             found+=1
print("Congratulations")     
    
