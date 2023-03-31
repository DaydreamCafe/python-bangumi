import os


def p():
    # print("clean had been run")
    # import os
    # print(os.getcwd())
    os.chdir("dist")
    a=os.listdir(os.getcwd())
    print(a)
    for i in a:
        os.remove(i)
    os.chdir("..")
    os.rmdir("dist")
