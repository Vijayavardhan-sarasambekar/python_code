with open("in.txt","r") as file:
    start=int(file.readline())
    print(start)
    end=int(file.readline())
    print(end)

for i in range(start,end+1):
    print("---------------------------")
    for j in range(1,11):
        result=i*j
        print(f"{i}*{j}={result}")
