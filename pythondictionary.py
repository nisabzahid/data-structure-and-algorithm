def group_by_owners(files):
    fileown = {}
    for key,value in files.items():
        if value not in fileown:
            fileown[value] = []
            fileown[value].append(key)
        else:
            fileown[value].append(key)
            
    return fileown

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files)) # should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
