is_male = True

if is_male:
    print("you are a male")
else:
    print("you are not a male")



is_tall = False

if is_tall and is_male:
    print("you are  male and tall")
elif is_male and not(is_tall):
    print("you are male but short")
else:

    print("you are neither tall nor male")




def max_num(num1, num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num3
    else:
        return num3

print(max_num(1,2,3))
