# 1a)a) Print Mathematical tables from 3 to 20.
# 3 * 1 = 3
# 3 * 2 = 6

# 3 * 10 = 30

# 4 * 1 = 4
# 4 * 2 = 8

# 20 * 1 = 20
# 20 * 2 = 40

start=3
end=20
file=open("out1a.txt","w")
for i in range(3,21):
    print("------------------------")
    file.write("-----------------------"+"\n")
    for j in range(1,11):
        r=i*j
        result=str(r)
        i1=str(i)
        j1=str(j)
        # print("%d*%d=%d" %(i,j,r))
        # print(f"{i}*{j}={r}")
        print(i1+"*"+j1+"="+result)
        file.write(i1+"*"+j1+"="+result+"\n")
file.close()