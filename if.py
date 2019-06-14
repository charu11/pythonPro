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