s= input("Enter score:")
try:
    x=float(s)
    if x>1 or x<0 :
        print("Bad Score")
    elif x>= .9:
        print("A")
    elif x>=.8:
        print("B")
    elif x>=.7:
        print("C")
    elif x>=.6:
        print("D")
    elif x<.6:
        print("F")
except:
    print("Bad score")
    quit()
