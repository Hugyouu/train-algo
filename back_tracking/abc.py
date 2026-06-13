ls = ['A', 'B', 'C', 'D']

def backtrack(path = None):
    if path is None:
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
    