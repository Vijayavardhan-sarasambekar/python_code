# d) Take Input Parameters 6,12 from a file called in.txt written on the same line separated by a comma. The output should get written to a file called out.txt. To go to next line, f1.write("/n")

# with open("input.txt","r") as file1:
#     start=file1.readline()
#     print(start)
#     end=file1.readline()
#     print(end)

# with open("")
start=open("input.txt","r")
end=open("out.txt","w")

f1=start.split(',')
for num in f1:
    end.write(num+'\n')

start.close()
end.close()


