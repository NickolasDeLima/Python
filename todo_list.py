import os

file_split = []

def file_loader():
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as f:
            file = f.read()
    else:
        with open('todo_list.txt', 'w+') as f:
            f.write('')
            file = f.read()
    global file_split
    file_split = file.split(';')

def display_content():
    i = 0
    file_size = int(len(file_split) - 1)
    print('To-do List')
    print('________________________________________')        
    while i < file_size:
        print(str(i) + ' - ' + file_split[i])
        i += 1

def remove():
    index = input("Type the number on the left side to the item that you want to delete : ")
    del file_split[int(index)]
    file = ";".join(file_split)
    with open('todo_list.txt', "w") as f:
        f.write(str(file))
    
def add():
    value = str(input('What do you need to do?: '))
    with open('todo_list.txt', 'a') as f:
        f.write(str(value) + ';')

def main():
    bolean = True
    while bolean:
        file_loader()
        display_content()
        print('------------------------')
        action = str(input('add, remove, exit')).lower()
        if action == 'add':
            add()
        if action == 'remove':
            remove()
        if action == 'exit':
            bolean = False
            
if __name__ == '__main__':
    main()