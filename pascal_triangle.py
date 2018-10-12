number=int(input("Enter number of rows: "))
output=[]
for i in range(number):
    output.append([])
    output[i].append(1)
    for j in range(1,i):
        output[i].append(output[i-1][j-1]+output[i-1][j])
    if(number!=0):
        output[i].append(1)
for i in range(number):
    print("   "*(number-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(output[i][j]),end=" ",sep=" ")
    print()
