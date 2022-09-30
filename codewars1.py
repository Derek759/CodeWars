def descending_order(num):
    if num >= 0:
        a=num
        nDig=len(str(a))
        dig=list(range(0,nDig))
        for i in range(0,nDig):
            if(i==0):
                x=(num-dig[0])%(10**(i+1))
            else:
                x=((num-dig[i-1])%(10**(i+1)))/10**(i)
                x=int(x)
            dig[i]=x
        print(dig)
        
        dig.sort(reverse=True)
        print(dig)

        final=0
        for i in range(0,nDig):
            final=final+(dig[i]*(10**(nDig-(i+1))))
            print(final)
        
        return num


num=316549848
#print(num)
descending_order(num)
#print(num)