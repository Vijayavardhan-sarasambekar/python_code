# d) Take Input Parameters 6,12 from a file called in.txt written on the same line separated by a comma. The output should get written to a file called out.txt. To go to next line, f1.write("/n")

# with open("input.txt","r") as file1:
#     start=file1.readline()
#     print(start)
#     end=file1.readline()
#     print(end)

# with open("")
start=open("input1d.txt","r")
end=open("out.txt","w")

# word1=start.readline()
# word2=start.readline()
# print(word1)
# print(word2)
# end.write(word1+"\n")
# end.write(word2)

for line in start:
    numbers=line.strip().split(",")
    for number in numbers:
        end.write(number+"\n")
