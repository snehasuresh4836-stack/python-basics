def sort_and_remove_duplicates(char_list):
    # Remove duplicates by converting to a set, then sort the result
    return sorted(set(char_list))

# Example usage
chars = ['b', 'a', 'd', 'a', 'c', 'b']
result = sort_and_remove_duplicates(chars)
print(result)  # Output: ['a', 'b', 'c', 'd']
