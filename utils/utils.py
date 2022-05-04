import os

def create_dir_if_not_exist(path):
    if not os.path.isdir(f'{path}'):
        os.mkdir(f'{path}')
        print(f'created dir: {path}')

