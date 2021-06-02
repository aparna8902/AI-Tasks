a=[]
b=[]
with open('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-2/F1.txt','r') as f1:
    for line in f1:
        for word in line.split():
            a.append(word)

with open('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-2/F2.txt','r') as f2:
    for line in f2:
        for word in line.split():
            b.append(word)

with open('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-2/F3.txt','w') as f3:
    i=0
    j=0
    while(i<len(a) or j<len(b)):
        if(i<len(a)):
            w = a[i]
            f3.write(w+" ")
            i+=1
        if(j<len(b)):
            u = b[j]
            f3.write(u+" ")
            j+=1
    
#C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-5/input.csv