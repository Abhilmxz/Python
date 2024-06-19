from Add import add
from Subt import subtract
from Divi import divide
from Multi import multiply

while True:
    print("Select Operation")
    print("^^^^^^^^^^^^^^^^")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = int (input("select your choice: "))
    if choice==1:
        num1=int(input("First Number: "))
        num2=int(input("Second Number: "))
        result=add(num1,num2)
        print("Your Answser Is: ",result)
        print("__!____!_____!____!_____!__")
    elif choice==2:
        num1=int (input("First Number: "))
        num2=int (input ("Second Number: "))
        result=subtract(num1,num2)    
        print("Your Answser Is: ",result)
        print("__!____!_____!____!_____!__")
    elif choice==3:
        num1=int (input("First Number: "))
        num2=int (input ("Second Number: "))
        result=multiply(num1,num2)    
        print("Your Answser Is: ",result)
        print("__!____!_____!____!_____!__")
    elif choice==4:
        num1=int (input("First Number: "))
        num2=int (input ("Second Number: "))
        result=divide(num1,num2)    
        print("Your Answser Is: ",result)
        print("__!____!_____!____!_____!__")