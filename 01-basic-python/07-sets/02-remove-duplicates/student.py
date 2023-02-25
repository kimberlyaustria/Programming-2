# Write your code here
def remove_duplicates(xs):
    empty_set = set()
    result = []
    for i in xs:
        if i not in empty_set:
            result.append(i)
            empty_set.add(i)
    
    return result
