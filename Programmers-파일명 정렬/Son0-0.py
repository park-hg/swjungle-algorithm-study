def solution(files):
    file_name = []
    for idx, file in enumerate(files):
        ptr = 0
        temp_str, temp_int = '', ''
        while ptr < len(file):
            target = file[ptr]
            if target.isdigit():
                temp_int += target
            else:
                if temp_int != '':
                    break
                temp_str += target.upper()
            ptr += 1
        file_name.append([idx, temp_str, int(temp_int)])
    
    file_name.sort(key = lambda x: (x[1], x[2]))
         
    return [files[fn[0]] for fn in file_name]
