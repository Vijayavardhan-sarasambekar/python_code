start=int(input("Enter number frrom 3:"))
end=int(input("Enter the number:"))

for i in range(start,end+1):
    print("---------------------------")
    for j in range(1,11):
        result=i*j
        print(f"{i}*{j}={result}")