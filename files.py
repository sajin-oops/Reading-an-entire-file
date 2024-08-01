# Opening a file and reading its content
with open('test.txt') as file:
    print(file.read())
    '''
    hii
welcome to coding
    '''
print(file.closed)
# - True