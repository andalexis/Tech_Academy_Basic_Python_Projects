# Python Drill
# Page 100

import os


path = 'C:\\Users\\Student\\Documents\\GitHub\\Tech_Academy_Basic_Python_Projects\\Python Drill 100'

dirs = os.listdir( path )
        
        
# retrieve latest time of file creation/modification
def getTime(result):
    result = os.path.getmtime(result)
    print(result)
    
    
print("Here are the .txt files:")
for file in dirs :
    if file.endswith(".txt"):
        result = os.path.join(path, file)
        print("\n" + result)
        print("Latest Date:")
        getTime(result)

