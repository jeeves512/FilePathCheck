import os
import re
print()
words_to_shorten = ['program', 'information', 'management', 'technology']
shortened_words = ['prgm', 'info', 'mgmnt', 'tech']
index = 0
for dirpath, dirnames, filenames in os.walk('C:\\Users\\jeevan.james\\Desktop\\new test folder one'):
    dirpath = dirpath.lower()
    print(os.path.basename(dirpath))
    while index < len(words_to_shorten):
        key_word = words_to_shorten[index]
        if key_word in dirpath:

            dir_name = os.path.basename(dirpath)
            new_name = dirpath.split(dir_name)
            os.rename(dirpath, os.path.join(new_name[0], dir_name.replace(key_word, shortened_words[index])))
            dirpath = os.path.join(new_name[0], dir_name.replace(key_word, shortened_words[index]))
            print(dirpath)
        index = index + 1
    index = 0
    if len(filenames):
        for file in filenames:
            file = file.lower()
            # print (os.path.join(dirpath, file))
            if len(os.path.join(dirpath, file)) > 0:
                while index < 4:
                    key_word = words_to_shorten[index]
                    if key_word in file:
                        new_name = shortened_words[index]
                        os.rename(os.path.join(dirpath, file), os.path.join(dirpath, file.replace(key_word, new_name)))
                        print(dirpath)
                    index = index + 1
                index = 0
