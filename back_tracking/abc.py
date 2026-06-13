ls = ['A', 'B', 'C']

def backtrack(path = None):
    if path == None:
        path = []
        
    if len(path) == len(ls):
        print(path)
        return
    
    for char in ls:
        if char not in path:
            path.append(char)
            backtrack(path)
            path.pop()
            
    return path
            
backtrack()    
    