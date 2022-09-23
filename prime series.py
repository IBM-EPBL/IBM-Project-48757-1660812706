lower=int(input("Enter the min value :"))
upper=int(input("Enter the max value :"))
for a in range(lower,upper+1):
    if a>1:
       for i in range(2,a):
           if (a%i)==0:
              break
       else:
           print(a)
