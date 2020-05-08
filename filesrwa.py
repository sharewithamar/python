# using with we dont need to close the file
# r+ for read and write
#a -append
# w- write mode starts fresh clears exsisting -if file not exits it
# for navigating filepaths use \

try:
    with open('test2.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)


except FileNotFoundError as err:
    print('file does not exist')
    raise err

except IOError as err:
    print('IO error')
    raise err
