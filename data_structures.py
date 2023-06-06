""" Variables for Example -  start """
x = 9
y = 10
subjective = "python"
type = " language"
array = 1,2,3,4,5,6
"""  Variables for Example - end """

""" Useful Functions """
print(f"{x == y}")  # Check equality 
print(f"{x + y}") # when made with two int variables it is a common sum 
print(f"{subjective + type}") # however, when used between variables of type string, it performs a concatenation
print(f"{subjective[0]}") # Accesses the value from position i
print(f"{subjective[0:2]}") # Accesses the values from position i to j
print(f"{len(type)}") # count the size of the variable
print(f"{min(array)}") # find the minimum value of the array  
print(f"{max(array)}") # find the maximum value of the array 
print(f"{array.count(2)}") # count how many times the element inside the parenthesis appears in the array
print(subjective.replace("t", 'XX')) # replacement

""" Example One - Function map() """ 
newArray = list(map(lambda x: x*x, array)) #The map() function is used to apply a given function to each item of an iterable object.
print(f" New list = {newArray}\n") # new list with all numbers from the previous list raised to the power of two

""" Example Two - Function map() """ 
languages = 'PYTHON', 'PHP', 'JAVA', 'JAVASCRIPT'
new_list = map(lambda x: x.lower(), languages)
print(f"New list = {new_list}\n")
new_list = list(new_list)
print(f"Now yes, the new list is = {new_list}")

""" filtering data """
def extract_email_list(list_1, list_2):
    list_1 = list(zip(list_1['name'], list_1['email'], list_1['sent']))
    print(f"List sample 1 = {list_1[0]}")

    list_2 = list(zip(list_2['name'], list_2['email'], list_2['sent']))

    data = list_1 + list_2

    print(f"\n Data sample = \n{data[:2]}\n\n")
    
    emails = [x[1] for x in data if not x[2]]
    return emails


data_1 = {
    'name': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'sent': [False, False, False, False, False, False, False, True, False, False]
}

data_2 = {
    'name': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'sent': [False, False, False, True, True, True, False, True, True, False]
}

emails = extract_email_list(list_1=data_1, list_2=data_2)
print(f"E-mails to be sent = \n {emails}")

""" ordenation """
print('\nOrdenation:\n')

list = [10, 4, 1, 15, -3]
print('list = ', list, '\n')
""" to sort a list: """
first_ordered_list = sorted(list)
print('First ordered list = ', first_ordered_list)

""" or: """
list.sort()
print('lista = ', list, '\n')

""" SELECTION SORT """
""" How is works selection sort """
""" First: go through the entire list, looking for the smallest value to occupy position 0 """
""" Second: starting from position 1, it goes through the entire list, looking for the smallest value to occupy position 1. """
""" Third: starting from position 2, it goes through the entire list, looking for the smallest value to occupy position 2."""
""" This process is repeated N-1 times, where N is the length of the list. """

def execute_selection_sort(list):
    n = len(list)
    
    for i in range(0, n):
        index_min = i
        for j in range(i+1, n):
            if list[j] < list[index_min]:
                index_min = j
        list[i], list[index_min] = list[index_min], list[i]
    return list

list = [10, 9, 5, 8, 11, -1, 3]
print(execute_selection_sort(list))

