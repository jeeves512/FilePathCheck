import os
length = 10
for dirpath, dirnames, filenames in os.walk('C:\\Users\\jeevan.james\\Desktop\\new test folder one'):
    if len(dirpath) > length:
        print(dirpath)
    if len(filenames):
        for file in filenames:
            if len(file) > length:
                print(os.path.join(dirpath,file))