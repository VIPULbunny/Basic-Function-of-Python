def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        i+=1
    print(f)
    return f
    

n = int(input("enter a number: "))
fact(n)