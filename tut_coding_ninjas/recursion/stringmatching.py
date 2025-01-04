s1 = "smd"
s2 = "skdmk"

dp = [[2] * (len(s2) + 1) for i in range(len(s1) + 1)]

print(dp)
print(len(dp))
print(len(dp[0]))

for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        print(dp[i][j], end=' ')
    print()
