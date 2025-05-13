# two major operations read & write 


# algorithm 
'''
    1. open file in read mode 
    2. store all the lines in a variable
    3. open in write mode 
    4. update the detail
'''
import os
def updateServerConfig(file_path,property_to_update,new_value):

    with open(file_path,"r")as file:
        lines = file.readlines()

    with open(file_path,'w')as file:
        for line in lines:
            if property_to_update in lines:
                file.write(property_to_update + "=" + new_value + "\n")
            else:
                file.write(line)

                
