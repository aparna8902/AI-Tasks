a=[]
b=[]
with open('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-3/file1.txt','r') as f1:
    for line in f1:
        for word in line.split():
            a.append(int(word))

with open('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-3/file2.txt','r') as f2:
    for line in f2:
        for word in line.split():
            b.append(int(word))

print("The number of elements in file 1: ",len(a))
a.sort()
print("The sorted elements of file1: ",a)
print("\n")
print("The number of elements in file 2: ",len(b))
b.sort()
print("The sorted elements of file2: ",b)
print("\n")

c = a + b
c.sort()
print("The number of elements in the new file: ", len(c))
print("The sorted elements of file1 and file 2 are: ",c)

with open('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-3/output.txt','w') as f3:
    for i in c:
        f3.write(str(i)+" ")
