import os

def create_dir_if_not_exist(path):
    if not os.path.isdir(f'{path}'):
        os.mkdir(f'{path}')
        print(f'created dir: {path}')

def check_if_url_is_film(string) -> bool:
    if string.endswith('.mp4') or string.endswith('.flv') or string.endswith('.mov') or string.endswith('.avi') or string.endswith('.mpeg4') or string.endswith('.3gpp'):
        return True
    else:
        return False

def check_if_url_is_img(string)->bool:
    if string.endswith('.png') or string.endswith('.jpg') or string.endswith('.gif'):
        return True
    else:
        return False