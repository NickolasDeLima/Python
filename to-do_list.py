## To-do list
import os

cwd = os.getcwd()

def main():

    # File handler
    if os.path.exists('{}\\todo_files\\todolist1.txt'.format(cwd)):
        with open('{}\\todo_files\\todolist1.txt'.format(cwd), 'r') as f:
            file = f.read()

    else:
        os.mkdir('{}\\todo_files'.format(cwd))
        with open('{}\\todo_files\\todolist1.txt'.format(cwd), 'w+') as f:
            f.write('')
            file = f.read()
    

    # Read content
    if file == '':
        pass
    
    else:
        i = 0
        file_split = file.split(';')
        file_size = int(len(file_split) - 1)
        print('To-do List')
        print('________________________________________')        
        while i < file_size:
            print(str(i) + ' - ' + file_split[i])
            i += 1


    # User input
    print('________________________________________')    
    print('If you want to add more tasks type "A"')
    print('If you want to delete a task type "R"')
    print('If You want to exit type "E"')
    action = input(': ').lower()



    # Options
    if action == 'a' :
        todo = input('What do you need to do? :')
        with open('{}\\todo_files\\todolist1.txt'.format(cwd), "a") as f:
            f.write(str(todo) + ' ; ')
            pass
            main()
        
    elif action == 'r':
        index = input("Yype the number on the left side to the item that you want to delete : ")
        del file_split[int(index)]
        file_write = ";".join(file_split)
        with open('{}\\todo_files\\todolist1.txt'.format(cwd), "w") as f:
            f.write(str(file_write))
            main()

    elif action == 'e':
        pass

main()