from functions import *
#nothing new here, just a comment for a pull request

while True:
    a = str(input())

    # here we begin to separate command, flags and arguments
    a = a.split()
    command = a.pop(0)
    flags = []
    arguments = a.copy()
    for word in a:
        if word.startswith('-', 0, 1):
            flags.append(word)
            arguments.remove(word)
    # here we end separation
    if command in tools.commands_list:
        if command == 'ls':
            ls()
        elif command == 'quit' or a == 'break':
            print('bye bye, motherfucker!')
            break
        elif command == 'pwd':
            pwd()
        elif command == "cd":
            cd(arguments)
        elif command == 'cp':
            cp(arguments)
        elif command == 'mv':
            mv(arguments)
        elif command == 'rm':
            rm(arguments)
        elif command == 'rmdir':
            rmdir(arguments)
        elif command == 'mkdir':
            mkdir(arguments)
    else:
        print('{}: No such command'.format(command))





