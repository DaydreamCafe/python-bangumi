import os


def clean_dist():
    os.chdir("dist")
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        os.remove(file)
    os.chdir("..")
    os.rmdir("dist")
