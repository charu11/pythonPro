# this is a simple translator it converts every vowel into "g" letter.





def translation(phrase):
    translate = ""
    for letter in phrase:
        if letter.lower() in "aeiou":

            if letter.isupper() :
                translate = translate + "G"
            else:
                translate = translate + "g"

        else:
            translate = translate + letter

    return translate

print(translation(input("Enter a phrase : ")))



#comments

'''
vfhjgldgrghjbfl
t
hthbyyth
rb

tyj

t
yj
et
'''