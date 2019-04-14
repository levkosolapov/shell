import inspect


def main_func():
    while True:
        a = input()

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
        try:
            if command in commands_dict.keys():
                if not arguments:
                    commands_dict[command]()
                else:
                    commands_dict[command](arguments)
            elif command == 'quit' or a == 'break':
                print('bye bye, motherfucker!')
                break
            else:
                print('{}: No such command'.format(command))
        except Exception as err:
            print(str(err))


commands_dict = dict(inspect.getmembers(functions, inspect.isfunction))

if __name__ == "__main__":
    main_func()
