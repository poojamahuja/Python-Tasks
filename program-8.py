line=input("enter a string: ")

print("your string is: ",line)
count={}

for i in line:

    if i in count.keys():

        count[i]+=1

    else:

        count[i]=1

print(count)