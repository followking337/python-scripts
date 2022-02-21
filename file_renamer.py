import os
import pathlib

path = r'/Users/dani/Documents/learning-python'


def rename(old_file):
    __doc__ = """Algorithm for renaming files"""
    new_file = old_file.replace('. ', '-').replace(', ', '_').replace(' ', '_')
    return new_file


def show(path):
    __doc__ = """Function previsualices old files names and new files names"""
    files = os.listdir(path)
    for old_file in files:
        new_file = rename(old_file)
        print(old_file, new_file, sep=' --> ')


def commit_rename(path):
    __doc__ = """Function renames recursively files in path"""
    files = os.listdir(path)
    for old_file in files:
        new_file = rename(old_file)
        os.rename(os.path.join(path, old_file), os.path.join(path, new_file))
        if os.path.isdir(path + '/' + old_file):
            commit_rename(path + '/' + old_file)


def delete_idea(path):
    __doc__ = """Function removes .idea directories. Error: Operation not permitted"""
    files = os.listdir(path)
    for old_file in files:
        if os.path.isdir(path + '/' + old_file) and old_file == '.idea':
            os.remove(path + '/.idea')


show(path)
# commit_rename(path)
# delete_idea(path)
