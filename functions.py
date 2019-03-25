import os
import tools
import shutil

def ls():
    # ls. Вывести список файлов и директорий для текущей директории.
    print('    '.join(os.listdir(path=".")))
    pass


def pwd():
    # pwd. Вывести полный путь для текущей директории.
    print(os.getcwd())
    pass


def cd(arguments: list):
    # cd <путь>. Переход по относительному или абсолютному пути.
    # print(cd.__name__, 'was just triggered')


    if len(arguments) > 2:
        print(arguments)
        print('cd: too many arguments')

    elif arguments == []:
        print('cd: additional argument required')

    elif arguments == ['..']:
        tools.go_a_dir_up()
    else:
        path = arguments.pop()
        if os.path.exists(path):
            os.chdir(path)
        else:
            print('cd: No such file or directory')


def cp(arguments):
    # cp <путь/имя файла>  <путь/имя файла>. Скопировать файл.

    if len(arguments) > 2:
        print('cd: too many arguments')
    elif len(arguments) == 1:
        src = arguments.pop()
        if os.path.isfile(src):
            #нужно доделать
            print('here should be complicated regex with copying')
            #все
        else:
            print('cp: No such file or directory')
    elif arguments == []:
        print('cd: additional argument required')
    else:
        src = arguments.pop(0)
        dst = arguments.pop()
        try:
            shutil.copy2(src, dst)
            print('successfully copied')
        except FileNotFoundError:
            print('cp: No such file or directory')


def mv(arguments):
    # mv <имя файла> <имя файла>. Переместить файл.

    if len(arguments) > 2:
        print('mv: too many arguments')

    elif len(arguments) != 2:
        print('mv: additional argument required')
    else:
        src = arguments.pop(0)
        dst = arguments.pop()
        try:
            shutil.move(src, dst)
            print('successfully copied')
        except FileNotFoundError:
            print('cp: No such file or directory')

def rm(arguments):
    # rm <имя файла>. Удалить файл.
    if len(arguments) > 1:
        print('rm: too many arguments')

    elif len(arguments) == 0:
        print('rm: additional argument required')
    else:
        path = arguments.pop()
        if os.path.isfile(path):
            try:
                os.remove(path)
            except OSError:
                print('Use rmdir to remove directories')
        else:
            print('rm: No such file')

def rmdir(arguments):
    # rmdir <имя директории>. Удалить директорию в случае, если она пуста.

    if len(arguments) > 1:
        print('rmdir: too many arguments')

    elif len(arguments) == 0:
        print('rmdir: additional argument required')
    else:
        name = arguments.pop()
        path = os.path.join(os.getcwd(), name)
        if os.path.exists(path):
            try:
                os.rmdir(path)
            except OSError:
                print('folder not empty')
        else:
            print('rmdir: No such directory')


def mkdir(arguments):
    # mkdir <имя директории>. Создать директорию, если ее не было.

    if len(arguments) > 1:
        print('mkdir: too many arguments')

    elif len(arguments) == 0:
        print('mkdir: additional argument required')
    else:
        path = arguments.pop()
        try:
            os.mkdir(path)
        except FileExistsError:
            print('mkdir: folder already exists')



