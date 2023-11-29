# b) Take Input Parameters Start=3 and End=20 from User through Keyboard. Print the same Mathematical Tables. If user gives the two inputs as 4 and 25, then the tables should print from 4 to 25.
start=int(input("Enter number frrom 3:"))
end=int(input("Enter the number:"))

for i in range(start,end+1):
    print("---------------------------")
    for j in range(1,11):
        result=i*j
        print(f"{i}*{j}={result}")