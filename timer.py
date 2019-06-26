import time

#seconds = input(("how much time do you want us to wait: "))


def countdown(n):
    while n > 0:
       print(n)
       n = n-1
       if n == 0:
        print("the time is up")
countdown(10)
