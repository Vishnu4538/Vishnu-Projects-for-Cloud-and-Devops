def patter_match(pattern,filename):
    file=open(filename,'r')
    lines= file.readlines()
    for line in lines:
        if pattern in line:
            print(f"we found the {pattern}  at {filename}")
            print('Exactly line in file is' , f"{line}")
            break
        else:
            continue


patter_match("error","/home/vishnu/error.log")
