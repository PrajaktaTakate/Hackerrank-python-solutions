def mutate_string(string, position, character):
    new_string=string[:position] + str(character) + string[position+1:]
    return new_string

if __name__ == '__main__':
    print(mutate_string("Praj",2,'b'))
