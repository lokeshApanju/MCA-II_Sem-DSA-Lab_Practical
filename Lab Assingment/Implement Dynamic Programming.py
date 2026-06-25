# (A) Fibonacci Series using Dynamic Programming

print("(A) Fibonacci Series using Dynamic Programming")

def fibonacci(n):
   dp = [0] * (n + 1)

   dp[0] = 0
   if n > 0:
       dp[1] = 1

   for i in range(2, n + 1):
       dp[i] = dp[i - 1] + dp[i - 2]

   return dp[n]

# Driver Code
n = int(input("Enter n: "))
print("Fibonacci Number =", fibonacci(n))

print("<---------------------------------->")
# (B) 0/1 Knapsack using Dynamic Programming

print("(B) 0/1 Knapsack using Dynamic Programming")

def knapsack(W, wt, val, n):
   dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

   for i in range(n + 1):
       for w in range(W + 1):

           if i == 0 or w == 0:
               dp[i][w] = 0

           elif wt[i - 1] <= w:
               dp[i][w] = max(
                   val[i - 1] + dp[i - 1][w - wt[i - 1]],
                   dp[i - 1][w]
               )

           else:
               dp[i][w] = dp[i - 1][w]

   return dp[n][W]

# Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print("Maximum Profit =", knapsack(W, wt, val, n))
