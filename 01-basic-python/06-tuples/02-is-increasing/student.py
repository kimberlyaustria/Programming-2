# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    pairs = list(zip(ns, ms))

    for element in pairs:
        if element[0] > element[1]:
            return False

    return True
