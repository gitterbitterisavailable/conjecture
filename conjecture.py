
def collatz(a):
    b = []
    b.append(a)



    for n in b:

        if n%2 == 0:
            new = n/2
            b.append(new)
            print("divided(x/2):",new)

        elif n == 1 and len(b) == 1:
            print("your loop will consists of 1,4,2,...")

        elif n == 1:
            ops = len(b) - 1 
            print("done! #of operations done:",ops ,"final list of numbers:",b)


        elif n == -1: 
            print("your loop will consist of -1,-2,-1...")
            

        else:
            new = (3*n)+1
            b.append(new)
            print("multiplied(3x+1) to:",new)

    return b





# with open("output.txt", "a") as f:
#     f.writelines(", ".join(str(e) for e in b))
