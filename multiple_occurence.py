def repetative(s):
    if(s>0):
        i=int(input("\n enter the value:"))
        if i>= 100000 and i <= 999999:
            print(i)
            i=str(i)
            inputs=[a for a,b in zip(i,i[2:]) if a==b]
            x=len(inputs)
            print(x)
            if x>0:
                print("This is a repetative number:",i)
            else:
                print("This is not a repetative Number:",i) 
if __name__ == '__main__':
    print(repetative)
    repetative(1)
