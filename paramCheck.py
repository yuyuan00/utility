# read a file and check specific parameter exists
# if not, add it

fn = 'paramtest.txt'
param = input("please type in parameter: ")
value = input("please type in default value: ")

if (param == '')  or (value == ''): 
    exit()

paramExist = 0
fileError = 0
with open(fn) as file_obj:
    obj_list = file_obj.readlines()


index = 0
for line in obj_list:
    if line == '\n':
        # print("Blank line...")
        obj_list.pop(index)  
    if  (line != '\n') and ('=' not in line):
        print("File type error.")
        fileError = 1
        break
    if param in line:
        paramExist = 1
        obj_list[index] = param + '=' + value + '\n'
    index += 1    

if fileError == 0 and paramExist == 0:
    obj_list.append('\n' + param + '=' + value)  

#print(obj_list)
if fileError == 0:
    with open(fn, 'w') as file_obj:
        file_obj.writelines(obj_list)
