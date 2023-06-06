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
print('list = ', list, '\n')

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

""" BUBBLE SORT """
""" First: selects the value at position 0 and compares it with its neighbor – if it is smaller,
    there is an exchange; if not, select the next one and compare, repeating the process. """
""" Second: selects the value at position 0 and compares it with its neighbor, 
    if it is a smaller change, otherwise selects the next one and compares it, repeating the process.  """
""" This process is repeated N-1 times, where N is the length of the list. """

def execute_bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

list = [10, 9, 5, 8, 11, -1, 3]
execute_bubble_sort(list)

""" Insertion sort  """
""" Start: it is assumed that the list has a single value and is therefore sorted """
""" First: it is assumed that a new value needs to be inserted into the list; in this case, 
    it is compared with the existing value to see if a position change needs to be made. """
""" Second: it is assumed that a new value needs to be inserted into the list; in this case, 
    it is compared with the existing values to see if position changes need to be made. """
""" This process is repeated N-1 times, where N is the length of the list """

def execute_insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        entered_value = list[i] 
        j = i - 1
        
        while j >= 0 and list[j] > entered_value:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = entered_value
    
    return list

list = [10, 9, 5, 8, 11, -1, 3]
execute_insertion_sort(list)

""" MERGE SORT """
""" First: Based on the original list, find the middle and separate it into two lists: left_1 and right_2. """
""" Second: Based on the left_1 sublist, if the amount of elements is greater than 1, 
    find the middle and separate it into two lists: left_1_1 and right_1_1. """
""" Third: Repeat the process until you find a list with size 1. """ 
""" Fourth: Call the merge step.  """
""" Fifth: Given two lists, each of which contains 1 value – to sort, 
    simply compare these values and swap, generating a sublist with two sorted values. """
""" Sixth: Given two lists, each of which contains 2 values – to order, 
    just choose the smallest value in each one and generate a sublist with four ordered values. """
""" Repeat the process of comparing and merging the values until you reach the original list, now sorted. """

def execute_merge_sort(list):
    if len(list) <= 1: return list
    else:
        middle = len(list) // 2
        left = execute_merge_sort(list[:middle])
        right = execute_merge_sort(list[middle:])
        return execute_merge(left, right)

    
def execute_merge(left, right):
    sub_list_ordination = []
    top_left, top_right = 0, 0
    while top_left < len(left) and top_right < len(right):
        if left[top_left] <= right[top_right]:
            sub_list_ordination.append(left[top_left])
            top_left += 1
        else:
            sub_list_ordination.append(right[top_right])
            top_right += 1
    sub_list_ordination += left[top_left:]
    sub_list_ordination += right[top_right:]
    return sub_list_ordination


list = [10, 9, 5, 8, 11, -1, 3]
execute_merge_sort(list)

""" QUICKSORT """
""" First: the original list will be broken through a value called a pivot. 
    After the break, the values that are smaller than the pivot should be on its left and the larger ones on its right.
    The pivot is inserted at the proper location, swapping the position with the current value. """
""" Second: now there are two lists, the one to the right and the one to the left of the pivot. Again, 
    two new pivots are chosen and the same process is carried out, placing the smaller ones on the right and the larger ones on the left.
    In the end, the new pivots occupy their correct positions.  """
""" Third: looking at the two new sublists (right and left), the process of choosing pivots and separating is repeated. """
""" In the last iteration, the list will be ordered, as a result of the previous steps. """

def execute_quicksort(list, start, end):
    if start < end:
        pivo = execute_participation(list, start, end)
        execute_quicksort(list, start, pivo-1)
        execute_quicksort(list, pivo+1, end)
    return list

        
def execute_participation(list, start, end):
    pivo = list[end]
    left = start
    for right in range(start, end):
        if list[right] <= pivo:
            list[right], list[left] = list[left], list[right]
            left += 1
    list[left], list[end] = list[end], list[left]
    return left

list = [10, 9, 5, 8, 11, -1, 3]
execute_quicksort(list, start=0, end=len(list)-1)