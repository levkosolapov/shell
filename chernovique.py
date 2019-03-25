import os
import shutil
a = "cd -a -b -d -c -f /home zaloopa"
# a = a.split()
# print(a)
# print(len(a))
# print(a.pop())
# print(a)
#
# print(len(a))
# if len(a) > 2:
#     print('cd: wrong arguments')

#
# a = a.split()
# command = a.pop(0)
#
# flags = []
# arguments = a.copy()
# for word in a:
#     if word.startswith('-', 0, 1):
#         flags.append(word)
#         arguments.remove(word)
#
# print('finally, flags:{}'.format(flags))
#
# print('finally, arguments:{}'.format(arguments))
# src='/home/pchome/Documents/experiments/shit.txt'
# dst = '/home/pchome/Documents/experiments/Untitled'
# try:
#     shutil.copy2(src, dst)
# except FileNotFoundError:
#     print('cp: No such file or directory')
#
name = 'new_folder'
path = os.path.join(os.getcwd(), name)
os.rmdir('/home/pchome/Documents/experiments/folder')