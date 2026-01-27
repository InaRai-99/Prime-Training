try:
    a = int(input("enter first no"))
    b = int(input("enter second no"))
    c= a/b
    print("Division is",c)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("You cannot divide any number by 0")
    