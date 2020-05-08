my_file = open('test.txt')

# can read only once since cursor moved to EOF, need to seek the cursor
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

print(my_file.readlines())  # gives  a list
print(my_file.readline())  # read only first line
# print(my_file.readline())

my_file.close()
