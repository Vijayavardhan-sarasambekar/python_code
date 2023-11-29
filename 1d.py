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


