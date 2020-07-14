list=eval(input("Input:"))
count=0
print("Output:",end=" ")
while count<len(list):
    if list[count]>0:
        print(list[count],end=" ")
    count=count+1
