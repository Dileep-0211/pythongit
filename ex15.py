# in this we are learning about how to call another file & read it out 

from sys import argv
script, filename = argv 
txt = open(filename)

print(f"here is your file{filename}")
print(txt.read())

print("type your file name again:")
file_again = input(">>>> ")

txt2=open(file_again)
print(txt2.read())
