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

for i in range(3,21):
    print("------------------------")
    for j in range(1,11):
        r=i*j
        # print("%d*%d=%d" %(i,j,r))
        print(f"{i}*{j}={r}")