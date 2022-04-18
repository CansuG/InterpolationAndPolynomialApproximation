import matplotlib.pyplot as plt

x= (20, 21, 23, 24, 25, 27, 29, 30)
fx = (346, 362, 343, 339, 347, 346, 339, 394)

xp=26
yp=0

for i in range (len(x)):
    p=1
    for j in range(len(x)):
        if j!=i:
            p *= (xp - x[j]) / (x[i] -x[j])
    yp += fx[i] * p

print(f"f(26) = {yp}") 

x= (20, 21, 23, 24, 25, 26, 27, 29, 30)
fx = (346, 362, 343, 339, 347, yp, 346, 339, 394)

plt.plot(x,fx)
plt.xlabel("April")
plt.ylabel("Number of Deaths")
plt.show()





