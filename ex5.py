#this is the exercise-5
#in this the variables are printing inside " "    
print("today we are going to discuss about  you \n give your inputs:")
name = input('give your name')
age = int(input('give your age'))

height=int(input('give your height'))
#im adding the age =height
total = age + height

occupation = input('student or not')
if occupation == ("student"):
    college=input('college name ')
    year=input('which year :')
    backlogs=input('do you have backlogs:yes/no')
    if backlogs == ("yes"):
          backlogs=int(input('give your backlogs count'))
else:
    occupation=input('what is your occupation')



print(f"today we are going to disscuss about the {name}")
print(f"{name}'s age is {age} years")
print(f"{name}'s height is {height}")
print(f"{name} occupation is {occupation} ")
print(f"here im adding the height:{height} and the age {age} is {total}")


