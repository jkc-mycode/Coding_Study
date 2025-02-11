def solution(files):
    separated_files = []
    
    for index, file in enumerate(files):
        head = ""
        number = ""
        tail = ""
        i = 0
        
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1
            
        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1
        
        tail = file[i:]
        separated_files.append([head, number, tail, index])
    
    separated_files = sorted(separated_files, key=lambda x: (x[0].lower(), int(x[1]), x[3]))
    
    return ["".join(file[:3]) for file in separated_files]