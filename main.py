while True:
    # 1- input first number
    # 1- input first number2
    while True:
        try:
          first_num = float(input("enter first number : "))
          break
        except ValueError:
            print("invalid input. please enter a numeric value")
    # 2- input operation 
    while True:
        try:
          operation = input("enter operation type : ")
          if operation in ("+", "-", "*", "/"):
            break
          else:
            raise ValueError
        except ValueError:
            print("invalid operation, please enter + , - , * , / ")

    # 3- input sec0nd number
    while True:
        try:
          secound_number = float(input("enter secound number : "))
          if secound_number == 0 and operation == "/":
            raise ZeroDivisionError
          break
        except ValueError:
            print("invalid input. please enter a numeric value")
        except ZeroDivisionError:
            print("cannot divide by zero, please enter another numeric")
    if operation == "+":
        print(first_num + secound_number)
    elif operation == "-":
        print(first_num + secound_number)     
    elif operation == "*":
        print(first_num * secound_number)   
    elif operation == "/":
        print(first_num / secound_number)  
    else:
        print("error")
    repeat = input("do you want to perform another operation (y/n) : ")
    if repeat == "n":
        break
    elif repeat == 'y':
        continue
    else:
        print("please enter y to counten or n to cancel")
print("program exited")
