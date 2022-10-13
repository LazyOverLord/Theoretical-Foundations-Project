import sys
import os


try:

    file_path = sys.argv[1]

    if(os.path.exists(sys.argv[1]) == False):

        print("Cannot find file " + sys.argv[1])

        file_path = input("Please enter the name of config file: ")

        sys.exit()

except IndexError:

    file_path = input("Please enter the name of the config file: ")




file = open(file_path,'r')

data = file.readlines()


print("Using the file "+ file_path + " for config")


for i in range(len(data)):

    data[i] = data[i].replace('{','').replace('}','').replace('\n','')
    data[i] = data[i].replace('(','').replace(')','')


alpha = data[0].split(',')
states = data[1].split(',')
start_state = data[2]
end_states = data[3].split(',')

data_holder = {}

for item in states:

    data_holder[item] = {}


for item in data[4:]:

    if item!='':
        
        temp = item.split('->')
        left = temp[0].split(',')
        data_holder[left[0]][left[1]] = temp[1]






#user_input = "0001"

user_input = input("Please enter a string: ")


for item in user_input:

    start_state = data_holder[start_state][(item)]


if end_states.__contains__(start_state)== True:

    print("The machine will accept the string " + user_input)


else:

    print("The machine will not accept the string " + user_input)


