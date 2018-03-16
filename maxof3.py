def maxOfThree(no1,no2,no3):
    if(no1>no2):
        if(no1>no3):
            return no1
        else:
            return no3
    else:
        if(no2>no3):
            return no2
        else:
            return no3

ans=maxOfThree(10,20,30)
print "max of three is ",ans,"\n"
