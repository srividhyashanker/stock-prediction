import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('outputfile.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
    	if count != 0:
    		x.append(int(row[0]))
    		y.append(float(row[1]))
    	count = count + 1

plt.plot(x,y, label='Loaded from MSE Test Output')
plt.xlabel('# of Iterations')
plt.ylabel('Error')
plt.title('Stock Prediction Loss')
plt.legend()
plt.show()
