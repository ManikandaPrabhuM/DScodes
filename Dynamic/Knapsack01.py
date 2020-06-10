def knapsack01(W, wt, val, n): 
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                continue
            elif wt[i-1] <= w: 
                table[i][w] = max(val[i-1]+table[i-1][w-wt[i-1],table[i-1][w]) 
            else: 
                table[i][w] = table[i-1][w] 
  
    return table[n][W]
n=int(input("Enter no of items\n"))
val=list(map(int,input("Enter the values\n").split())) 
wt=list(map(int,input("Enter the weights\n").split()))
W=int(input("Enter knapsack capacity\n"))
print(knapsack01(W,wt,val,n))
