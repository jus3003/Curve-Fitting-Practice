## Assignment3 ME369P/ME396P/ES122
## Name: Justin Lam
## EID : JHL2965
## Section: ME 396P

## Fill in the sections below. 
## Make sure your code runs with the tests in main
## You may use any imports, but do not use any import function for regression.


'''
PROBLEM 2

Please note the passed in file argument.

Required output:
1. problem2.gif

'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

def problem2PointGIF(filename):

    # complete the animate function
    df = pd.read_csv(filename, header = None)
    x = df[0]
    y = df[1]
    
    fig, ax = plt.subplots()
    
    def init():
        ax.clear()

    def update(i):
        label = 'timestep {0}'.format((i+1)*5)
        print(label)
        ax.set(xlim = (min(x), max(x)), ylim = (min(y),max(y)))
        ax.scatter(x[i], y[i], s = 15)
        ax.set_xlabel(label)
        return ax

    # Create an animation object from the created figure that includes
    # n frames viewed at intervals of 5 ms.          
    anim = FuncAnimation(fig, update, interval = 5, frames = len(df), init_func = init, repeat_delay = 30000, repeat = True)   
    
    # save a gif of the animation using the writing package from magick
    anim.save('problem2.gif', dpi=80, writer='pillow')

'''
PROBLEM 3

Please note the passed in file argument.

Required output:
1. problem3.gif
2. Writing section
3. Print equation output to console

'''

def problem3CurveFitting(filename):
    
    # complete the animate function 
    # Develop curve fitting and print equation output to console
    # Create an animation object from the created figure that includes
    # n frames viewed at intervals of 5 ms.
    # save a gif of the animation using the writing package from magick
    
    df_3 = pd.read_csv(filename, header = None)
    data_points = len(df_3)
    
    x_3 = df_3[0]
    y_3 = df_3[1]
    
    #Plot First Two points
    x_3_two = df_3[0][0:2]
    y_3_two = df_3[1][0:2]
    fig, ax = plt.subplots()
    
    #Do First Iteration
    x_squared = (x_3[0])**2 + (x_3[1])**2
    x_sum = x_3[0] + x_3[1]
    n = 2
    x_y = x_3[0]*y_3[0] + x_3[1]*y_3[1]  
    y_sum = y_3[0] + y_3[1]
    y_mean = y_sum/2
    
    A = np.matrix([[x_squared,x_sum],[x_sum, n]])
    B = np.matrix([[x_y], [y_sum]])
    X = np.linalg.inv(A).dot(B)
    a = float(X[0])
    b = float(X[1])
    s_t = (y_3[0]-y_mean)**2 + (y_3[1] - y_mean)**2
    s_r = (y_3[0] - a*x_3[0] - b)**2 + (y_3[1] - a*x_3[1] - b)**2
    r_squared = (s_t - s_r)/(s_t)
    
    if(b < 0):
        b_abs = abs(b)
        line_str = 'y = {}x - {} where r^2 = {}'.format(format(round(a,5), '.5f') , format(round(b_abs, 5), '.5f'), format(round(r_squared, 5), '.5f'))
    else:
        line_str = 'y = {}x + {} where r^2 = {}'.format(format(round(a,5), '.5f') , format(round(b_abs, 5), '.5f'), format(round(r_squared, 5), '.5f'))

    print(line_str)

    
    #Create List to Append a/b values
    a_b = [[0 for i in range (2)] for j in range (data_points - 1)]
    a_b[0][0] = a
    a_b[0][1] = b

    for i in range(len(x_3) - 2):
        x_squared += (x_3[i+2])**2
        x_sum += x_3[i+2]
        x_y += x_3[i+2]*y_3[i+2]
        y_sum += y_3[i+2]
        n += 1
        y_mean = y_sum/n
    
        A = np.matrix([[x_squared,x_sum],[x_sum, n]])
        B = np.matrix([[x_y], [y_sum]])
        X = np.linalg.inv(A).dot(B)
    
        a = float(X[0])
        b = float(X[1])
        a_b[i+1][0] = a
        a_b[i+1][1] = b
    
        s_t = 0 
        s_r = 0

        for r in range(0, i+3):
            s_t += (y_3[r] - y_mean)**2
            s_r += (y_3[r] - a*x_3[r] - b)**2

        r_squared = (s_t - s_r)/(s_t)
    
        if(b < 0):
            b_abs = abs(b)
            line_str = 'y = {}x - {} where r^2 = {}'.format(format(round(a,5), '.5f') , format(round(b_abs, 5), '.5f'), format(round(r_squared, 5), '.5f'))
        else:
            b_abs = abs(b)
            line_str = 'y = {}x + {} where r^2 = {}'.format(format(round(a,5), '.5f') , format(round(b_abs, 5), '.5f'), format(round(r_squared, 5), '.5f'))
        
        print(line_str)


    #Create function to update plot with each data increasing data point
    def init():
        ax.set(xlim = (min(x_3) -1, max(x_3)+ 1), ylim = (min(y_3) - 1,max(y_3)+ 1))
        ax.scatter(x_3_two, y_3_two, s = 15)
        y = 1
        line, = ax.plot(y, 'r-')


    def update(i):
        label = 'timestep {0}'.format((i+2)*250)
        ax.scatter(x_3[i+3], y_3[i+3], s = 15)
        ax.set_xlabel(label)
    
        if (i < (data_points - 3)):
            x = np.arange(min(x_3[0:(i+4)]), max(x_3[0:(i+4)]), 0.06)
            y = a_b[i+2][0]*x + a_b[i+2][1]
            line, = ax.plot(x,y, 'r-')        
        return ax, line

    anim = FuncAnimation(fig, update, interval = 250, frames = (np.arange(1,len(df_3)) - 3) , init_func = init)

    anim.save('problem3.gif', dpi=80, writer='pillow')
    

'''
PROBLEM 4

Please note the passed in file argument.

Required output:
1. problem4.gif
2. Print equation output to console

'''
def problem4WhichCurve(filename):

    # complete the animate function
    # Develop different order curve fitting and print equation output to console
    # Create an animation object from the created figure that includes
    # n # frames viewed at intervals of 5 ms.      
    # save a gif of the animation using the writing package from magick   
    
    df4 = pd.read_csv(filename, header = None)

    x4 = df4[0]
    y4 = df4[1]
    
    #Setup Hard Variables
    N = len(df4)
    n = 6
    
    #Setup Matrix A Calculations
    Xi = np.zeros((2*n+1,1))
    Xi[0] = N
    
    for i in range(1,2*n+1):
        sumx = 0 
        for r in range(0,N):
            sumx += (x4[r])**i
        Xi[i] = sumx
    
    #Setup Matrix B 
    YiXi = np.zeros((n+1, 1))
    y_sum = 0
    
    for i in range(0,N):
        y_sum += y4[i]
    
    YiXi[0] = y_sum
    
    for i in range(1,n+1):
        sumyixi = 0
        for r in range(0,N):
            sumyixi += y4[r]*(x4[r])**i
        YiXi[i] = sumyixi
    
    #Create Matrix to Store A/B Values for All Orders 
    AB  = np.zeros((n+1,n+1))
    
    #Setup Matrix Operations
    for i in range (1,n+1):
        matA = np.zeros((i+1,i+1))
        matB = np.zeros((i+1,1))
    
        #Fill in Matrix A
        for col in range(len(matA)):
            for row in range(len(matA)):
                matA[row][col] = Xi[(i*2) - col - row] 
    
        #Fill in Matrix B
        for row in range(i+1):
            matB[row][0] = YiXi[i - row]
    
        #Do Matrix Calculation
        matX = np.linalg.inv(matA).dot(matB)
    
        #Append Matrix to A/B Recorder Matrix
        for col in range(len(matX)):
            AB[i][col] = matX[(len(matX)-1) - col]
    
    #Create Matrix to hold R values
    Rsquared = np.zeros((n+1, 1))
    
    #Calculate S_t
    y_mean = y_sum/N
    S_t = 0
    
    for i in range(0,N):
        S_t += (y4[i] - y_mean)**2
    
    #Calculate S_r then calculate R then append to Matrix
    
    for r in range(1, len(Rsquared)):
        S_r = 0 
        for i in range(0,N):
            S_r += (y4[i] - AB[r][6]*((x4[i])**6) - AB[r][5]*((x4[i])**5)- AB[r][4]*((x4[i])**4)- AB[r][3]*((x4[i])**3)- AB[r][2]*((x4[i])**2)- AB[r][1]*((x4[i])**1) - AB[r][0])**2
    
        Rsquared[r][0] = ((S_t - S_r)/S_t)
    
    
    #Print Out Results
    
    #Create Matrix to Reference if Something is Positive or Negative
    sig = np.zeros((n+1,n+1), dtype = str)
    for row in range(len(sig)):
        for col in range(len(sig)):
            if AB[row][col] < 0:
                #signmatrix[row][col] = '- {}'.format(format(round(float(AB[row][col]), 5),'.5f'))
                sig[row][col] = '-'
            else:
                #signmatrix[row][col] = '+ {}'.format(format(round(float(AB[row][col]), 5),'.5f'))
                sig[row][col] = '+'
    
    #Adjust AB Numpy Matrix to Preferred Rounding, then Adjust again to Preferred Decimal Places
    AB = AB.round(decimals = 5, out = None)
    Rsquared = Rsquared.round(decimals = 5, out = None)
    
    #Print to Console
    line_str = '1: y = {}x {} {} (r^2 = {})'.format(format(AB[1][1],'.5f'), sig[1][0], format(abs(AB[1][0]),'.5f'), format(float(Rsquared[1]),'.5f'))
    print(line_str)
    line_str = '2: y = {}x^2 {} {}x {} {} (r^2 = {})'.format(format(AB[2][2],'.5f'), sig[2][1], format(abs(AB[2][1]),'.5f'), sig[2][0], format(abs(AB[2][0]),'.5f'), format(float(Rsquared[2]),'.5f'))
    print(line_str)
    line_str = '3: y = {}x^3 {} {}x^2 {} {}x {} {} (r^2 = {})'.format(format(AB[3][3],'.5f'), sig[3][2], format(abs(AB[3][2]),'.5f'), sig[3][1], format(abs(AB[3][1]),'.5f'),sig[3][0], format(abs(AB[3][0]),'.5f'), format(float(Rsquared[3]),'.5f'))
    print(line_str)
    line_str = '4: y = {}x^4 {} {}x^3 {} {}x^2 {} {}x {} {} (r^2 = {})'.format(format(AB[4][4],'.5f'), sig[4][3], format(abs(AB[4][3]),'.5f'), sig[4][2], format(abs(AB[4][2]),'.5f'),sig[4][1], format(abs(AB[4][1]),'.5f'), sig[4][0], format(abs(AB[4][0]),'.5f'), format(float(Rsquared[4]),'.5f'))
    print(line_str)
    line_str = '5: y = {}x^5 {} {}x^4 {} {}x^3 {} {}x^2 {} {}x {} {} (r^2 = {})'.format(format(AB[5][5],'.5f'), sig[5][4], format(abs(AB[5][4]),'.5f'), sig[5][3], format(abs(AB[5][3]),'.5f'),sig[5][2], format(abs(AB[5][2]),'.5f'), sig[5][1], format(abs(AB[5][1]),'.5f'), sig[5][0], format(abs(AB[5][0]),'.5f'), format(float(Rsquared[5]),'.5f'))
    print(line_str)
    line_str = '6: y = {}x^6 {} {}x^5 {} {}x^4 {} {}x^3 {} {}x^2 {} {}x {} {} (r^2 = {})'.format(format(AB[6][6],'.5f'), sig[6][5], format(abs(AB[6][5]),'.5f'), sig[6][4], format(abs(AB[6][4]),'.5f'),sig[6][3], format(abs(AB[6][3]),'.5f'), sig[6][2], format(abs(AB[6][2]),'.5f'), sig[6][1], format(abs(AB[6][1]),'.5f'), sig[6][0], format(abs(AB[6][0]),'.5f'), format(float(Rsquared[6]),'.5f'))
    print(line_str)
    
    
    #Graph Animation
    
    #Create Base Plot
    
    fig, ax = plt.subplots()
    
    def init():
        #ax.set(xlim = (min(x4) -1, max(x4)+ 1), ylim = (min(y4) - 1,max(y4)+ 1))
        #ax.set(xlim = (min(x4) -1, max(x4)+ 1), ylim = (min(y4) - 1,max(y4)+ 1))
        ax.scatter(x4, y4, s = 15)
        return ax
    
    
    #Create Update Function
    
    def update(i):
        label = 'Order {}'.format(i+1)
        ax.set_xlabel(label)
    
        x = np.arange(min(x4), max(x4), 0.2)
        y = AB[i+1][0] + AB[i+1][1]*x + AB[i+1][2]*((x)**2) + AB[i+1][3]*((x)**3) + AB[i+1][4]*((x)**4) + AB[i+1][5]*((x)**5) + AB[i+1][6]*((x)**6)
    
        line = ax.plot(x,y,'r-')
    
        return ax, line
    
    anim = FuncAnimation(fig, update, interval = 500, frames = 6, init_func = init)
    anim.save('problem4.gif', dpi = 80, writer = 'pillow')
    
 
if __name__ == '__main__':
    problem2PointGIF('data_3_2.csv')
    problem3CurveFitting('data_3_3.csv')
    problem4WhichCurve('data_3_4.csv')
