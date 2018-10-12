'''
Created on 11-Oct-2018

@author: 10086
'''
def group_by_owners(files):
    result = {}
    for file, owner in files.items():  
        result[owner] = result.get(owner, []) + [file]  
    return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

if __name__ == '__main__':
    print(group_by_owners(files))