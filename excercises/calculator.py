#this will enable to make the software to rune on a loop untill error or break
while True:
    #The user needs to select the type of the function he wants to do on a calculator
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Devision")

    #this line of code will help the user to stop using the software
    print("Enter q or Q to Exit")

    #Now we need to ask the user to chosse the option by giving an input
    choice = input("Enter Your Choice : ")
    
    #this will hep the user to break the loop
    if choice == 'q' or choice == 'Q':
        break

    #ask user to enter the numbers
    num1 = float(input("Enter Number 1 :"))
    num2 = float(input("Enter Number 2 :"))

    #check the users choice 1
    if choice == "1":
        print(num1, "+", num2, "=", (num1+num2))
        
    #check if user cossed 2
    elif choice == "2":
            print(num1, "-", num2, "=", (num1-num2))
            
    #check the users choice 3
    if choice == "3":
        print(num1, "*", num2, "=", (num1*num2))
        
    #check the users choice 41
    if choice == "4":
        if num2 == 0.0:
            print("error")
        else:
            print(num1, "/", num2, "=", (num1/num2))
    #if a number that does not work it willgo through this line        
    else:
        print("invailid choice")
        
print()