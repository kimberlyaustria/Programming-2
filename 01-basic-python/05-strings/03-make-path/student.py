# Write your code here
def make_path(parts):
    string = ''
    for element in parts:
        string += '/' + element
    
    return string[1:]
