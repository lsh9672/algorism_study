#백준 2193번(디피, 실버3)
import sys

n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(91)]

dp[0] = 0
dp[1] = 1


for i in range(2,n+1):

    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])