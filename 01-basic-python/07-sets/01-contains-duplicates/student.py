# Write your code here
def contains_duplicates(xs):
    if len(xs) != len(set(xs)):
        return True
    return False
