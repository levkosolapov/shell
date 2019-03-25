import os


commands_list = ['ls', 'quit', 'break', 'pwd', 'cd', 'cp', 'mv', 'rm', 'rmdir', 'mkdir']


def flag_decorator(*args):
    pass


def go_a_dir_up():
    cur_path = os.getcwd()
    if cur_path == '/':
        pass
    else:
        arr = cur_path.split('/')
        del arr[-1]
        new_path = '/'.join(arr)
        try:
            os.chdir(new_path)
        except FileNotFoundError:
            os.chdir('/')
