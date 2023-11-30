# c) Take Input Parameters from a file called in.txt having 5 and 30 in first and second line. Your program should read the first two lines of this file and print Mathematical Tables from 5 to 30.

# with open("in.txt","r") as file:
#     start=int(file.readline())
#     print(start)
#     end=int(file.readline())
#     print(end)

# for i in range(start,end+1):
#     print("---------------------------")
#     for j in range(1,11):
#         result=i*j
#         print(f"{i}*{j}={result}")

file=open("in.txt","r")
start=int(file.readline())
end=int(file.readline())

for i in range(start,end+1):
    print("------------------------")
    for j in range(1,11):
        r=i*j
        i1=str(i)
        j1=str(j)
        result=str(r)
        print(i1+"*"+j1+"="+result)
