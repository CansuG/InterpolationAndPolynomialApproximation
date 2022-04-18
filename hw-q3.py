import matplotlib.pyplot as plt

def proterm(i, value, x): 
    pro = 1 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro 
  
def dividedDiffTable(x, y, n):
  
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]))
    return y
  

def applyFormula(value, x, y, n):
    sum = y[0][0] 
  
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]) 
      
    return sum 
  
def printDiffTable(y, n): 
  
    for i in range(n): 
        for j in range(n - i): 
            print(y[i][j] , "\t", end = " ")
        print("") 

n=8
x= (20, 21, 23, 24, 25, 27, 29, 30)
y = [[0 for i in range(8)] 
        for j in range(8)]

y[0][0] = 346
y[1][0] = 362
y[2][0] = 343
y[3][0] = 339
y[4][0] = 347
y[5][0] = 346
y[6][0] = 339
y[7][0] = 394

y=dividedDiffTable(x, y, n); 
  
printDiffTable(y, n); 
  
value = 26;
fx = applyFormula(value, x, y, n) 
print (f"f(26) : {fx}")

x= (20, 21, 23, 24, 25, value, 27, 29, 30)
fx = (346, 362, 343, 339, 347, fx, 346, 339, 394)

plt.plot(x,fx)
plt.xlabel("April")
plt.ylabel("Number of Deaths")
plt.show()

