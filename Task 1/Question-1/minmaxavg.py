l=[]
file=input("Enter the path of the filename with extension: ")
with open(file,'r') as file1: 
    # reading each line    
    for line in file1:
   
        # reading each word        
        for word in line.split():
            l.append(float(word))        

print("The file is: ") 
with open(file,'r') as f:
    print(f.read())

avg=sum(l)/len(l)
print("Maximum number in the file is: " + str(max(l)))
print("Minimum number in the file is: " + str(min(l)))
print("The average of the numbers in the file is: "+ str(avg))
   