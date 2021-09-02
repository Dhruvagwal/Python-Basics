# in machine there is algorithm which is linear regression
# y = mx + c

def linear_regression(y,x):
    m = 0.0 # slope
    c = 0.0 # bias

    # nested loop
    lr = 0.001
    if len(y) != len(x):
        print("You've entered wrong dimension")
        return None
    global_loss = 0
    for index in range(0,len(y)):
        y_pred = m*x[index] + c
        loss = y[index] - y_pred

        m = m-0.1
        c = c - 0.1
        global_loss = loss

    return m,c
            
    
    

y = [4,8,6,6,8]
x = [1,6,4,8,9]

# y = 2x

# y = mx+c
# (y-c)/x = m

m,c = linear_regression(y,x)

func = m*3 + c
print(func)