task 6
def count_occurrences(s, element):
    count = 0
    for char in s:
        if char == element:
            count += 1
    return count


