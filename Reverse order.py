
# Write a program to display the number in reverse order

 num=6324
rev=0
while num!=0:            
    rem=num%10               
    rev=rev*10+rem       
    num=num//10              
print("reverse number: ",rev)
