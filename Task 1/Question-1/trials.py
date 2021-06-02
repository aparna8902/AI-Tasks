with open('file1.txt','r') as f:
    size_to_read = 1
    f_content = f.read(size_to_read)
    while len(f_content)>0:
        print(f_content, end='')
        f_content = f.read(size_to_read)