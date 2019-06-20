#try_except is used to display error by ourselves thsn msg without displaying the error msg by the program
try:
    value = 1/0
    number = int(input("enter a number : "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

#we can use a variable to store those errors. like in the example above.
# the ZeroDivisionError is stored as the variable