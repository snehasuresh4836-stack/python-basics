def sort_char_num(lst):
    # Separate numbers and letters
    numbers = [x for x in lst if isinstance(x, (int, float))]
    letters = [x for x in lst if isinstance(x, str)]
    
    # Sort 
    numbers.sort()
    letters.sort()
    
    # Combine letters first, then numbers
    return letters + numbers

#eg:
my_list = [5, 'b', 2, 'a', 9, 'c', 1]
sorted_list = sort_char_num(my_list)
print("Original list:", my_list)
print("Sorted list:", sorted_list)
