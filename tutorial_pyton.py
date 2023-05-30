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

name = 'Rafa'
for i in name:
    print(i)

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

""" Functions | Funcoes """

def sum(x,y):
    return x+y

print(f"\nSum result: {sum(2,6)}")

def convert_upper_case(text, upper_case):
    if upper_case:
        return text.upper()
    else:
        return text.lower()

text = convert_upper_case(upper_case=True, text="Rafa")
print(text)

def print_parameters(*args):
    count_parameters = len(args)
    print(f"Number of parameters in the array, = {count_parameters}")
    
    for i, value in enumerate(args):
        print(f"Position = {i}, value = {value}")

        
print("\n Call 1")        
print_parameters("Subjects", 10, 23.78, "Rafa", {1,2,3,4})

print("\n Call 2")        
print_parameters(10, "Subjects")

""" Anonymous functions | Funções anonimas """
(lambda z: print(z*z))(z=3)

sum = lambda x, y: x + y
print(sum(x=5, y=3))

""" Challenge | Desafio """

def calculate_value(product_value, amount, coin="real", **kwargs):
    gross_value = product_value * amount
    
    if 'discount' in kwargs:
        discount = kwargs['discount']
        net_value = gross_value - (gross_value * (discount / 100))
    elif 'addition' in kwargs:
        addition = kwargs['addition']
        net_value = gross_value + (gross_value * (addition / 100))
    else:
        net_value = gross_value
    
    if coin == 'real':
        return net_value
    elif coin == 'dolar':
        return net_value * 5
    elif coin == 'euro':
        return net_value * 5.7
    else:
        print("This currency has not been registered")
        return 0

amount_to_pay = calculate_value(product_value=32, amount=5, discount=5)
print(f"O valor final da conta é {amount_to_pay}")    

