#python script whether a given number is armstrong are not.
def arm():
    n=int(input("enter a number:"))
    temp=n
    s=0
    while(n!=0):
        rem=n%10
        s=s+(rem**3)
        n=n//10
    if temp==s:
        print ("armstrong number")
    else:
        print("not armstrong")
