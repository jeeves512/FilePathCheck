import os
for dirpath, dirnames, filenames in os.walk('C:\\Users\Jeeves\Desktop\\folder'):
    if len(dirpath)>40:
        print(dirpath)
        print(" Too long")

    if len (filenames):
        for file in filenames:
            print (os.path.join(dirpath,file))
            if len(os.path.join(dirpath,file)) > 0:
                print('Too long')
