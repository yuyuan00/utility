# read a file and check some specific parameters with specific values
# if not, add it

fn = 'paramtest.txt'
param_list = ['school', 'nationality', 'number']
value_list = ['eastpretty', 'Taiwan', '20']
paramExist_list = ['0', '0', '0']

with open(fn) as file_obj:
    obj_list = file_obj.readlines()

index = 0
for line in obj_list:
    if line == '\n':
        obj_list.pop(index) 
    index += 1 

index = 0
for line in obj_list:
    index_param = 0
    if  (line != '\n') and ('=' not in line):
        print("File type error.")
        exit()
    for param in param_list:
        if param in line:
            # print('param: ', param)
            # print('value: ', value_list[index_param])
            obj_list[index] = param + '=' + value_list[index_param] + '\n'
            paramExist_list[index_param] = '1'
            break
        index_param += 1
    index += 1    

index_param = 0
for paramExist in paramExist_list:
    if paramExist == '0':
        # print('param: ', param_list[index_param])
        # print('value: ', value_list[index_param])        
        obj_list.append('\n' + param_list[index_param] + '=' + value_list[index_param])  
    index_param += 1

#print(obj_list)
with open(fn, 'w') as file_obj:
    file_obj.writelines(obj_list)
