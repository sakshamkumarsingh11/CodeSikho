def check_for_line():
    word=("saksham")
    data= True
    line_no=1
    with open ( "practice.text", "r") as f:
        while data:
            if(word in data):
                print(line_no)
            return 
        line_no+=1
    return -1
print(check_for_line)  