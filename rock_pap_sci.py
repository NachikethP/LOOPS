import random
while(True):
    comp1=random.choice(["r","p","s"])
    comp2=random.choice(["s","p","r"])
    print("comp1:",comp1)
    print("comp2:",comp2)
    if (comp1 =="r") and (comp2=="r"):
        print("match draw")
    elif (comp1 =="r") and (comp2=="p"):
            print("comp2 won")
    elif (comp1 =="r") and (comp2=="s"):
        print("comp1 won")

    elif (comp1 =="p") and (comp2=="r"):
        print("comp1 won")
    elif (comp1 =="p") and (comp2=="p"):
        print("match draw")
    elif (comp1 =="p") and (comp2=="s"):
        print("comp2 won")

    elif (comp1 =="s") and (comp2=="r"):
        print("comp2 won")
    elif (comp1 =="s") and (comp2=="p"):
        print("comp1 won")
    elif (comp1 =="s") and (comp2=="s"):
        print("match draw")

    print("\n")
    cont_input=input("want to try again? (y/n): ").casefold()
    print("\n")

    if(cont_input=='y'):
        continue
    else:
        print("thank u")
        break
