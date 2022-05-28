def solution(s):
    
    string_box = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_box = ["0","1","2","3","4","5","6","7","8","9"]
    idx = 0
    answer = " "
    for i in range(len(string_box)) :
        if string_box[i] in s :
            temp1 = string_box[i]
            temp2 = number_box[i]
            s = s.replace(temp1,temp2)
    return int(s)