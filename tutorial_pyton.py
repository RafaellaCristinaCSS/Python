""" Declaring Variables | Declarando variaveis """ 
id = 10
Student = 'aluno'
studentGrade = 8.75
studentRegistered = True

""" Print Variables Types | Imprimindo tipos de variaveis """
print(type(id))
print(type(Student))
print(type(studentGrade))
print(type(studentRegistered))

""" Receiving and Printing user data | Recebendo e imprimindo dados do usuario """
# Student = input("Enter your name: ")
# print(f"Hello {Student}, welcome") 

""" Math Operations | Operações Matematicas"""
x = 10
y = 3
print("x/y == 3.33333")
print("x//y == 3")
print("x%y == 1")
print("abs(x) == 10")
print("pow(x,y) == 1000 or x**y == 1000 equals x^y")

""" Conditional structures | Estruturas condicionais """
a = 5
b = 10
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b") 
else: 
    print("a is greater than b")     

""" Repeating structure | Estrutura de Repetição """
number = 1
while number != 0:
    number = int(input("Enter your number: "))
    if number % 2 == 0:
        print("this number is even!")
    else:
        print("this number is odd") 

name = "word"
for i, letter in enumerate(name):
    print(f"key = {i}, name = {letter}")

""" Replay Control | Controle de Repetição """
# Range
for x in range(5):
    print(x)

# For + Break and continue

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
for i, c in enumerate(text):
    if c == ' ':
        continue
    if c == '.':
       break    
    else:
        print(c, end="") # 2 letters on 1 row 