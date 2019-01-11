def one_out_of_two(string):
    for index in range(0, len(string)):
        if index % 2 == 0:
            string = string[:index]+string[index].upper()+string[index+1:]
        else:
            string = string[:index]+string[index].lower()+string[index+1:]
    return string

def is_isogram(string):
    string = string.lower()
    if len(string) == len(''.join(set(string))):
        return True
    else:
        return False
