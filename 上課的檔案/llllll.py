import matplotlib.pyplot as plt
import numpy as np
import cv2

def show_map(row, col):
    global lines
    if lines == []:
        for i in range(row):
            line = plt.plot(map[i*col:(i+1)*col,0], map[i*col:(i+1)*col,1], linewidth=3, c='k')
            lines.append(line)
        for j in range(col):
            line = plt.plot(map[j:row*col:col,0], map[j:row*col:col,1], linewidth=3, c='k')
            lines.append(line)
    else :
        for i in range(row):
            lines[i][0].set_xdata(map[i*col:(i+1)*col,0])
            lines[i][0].set_ydata(map[i*col:(i+1)*col,1])
        for j in range(col):
            lines[j+row][0].set_xdata(map[j:row*col:col,0])
            lines[j+row][0].set_ydata(map[j:row*col:col,1])
    fig.canvas.draw()
    fig.canvas.flush_events()

row, col = 5, 5

map = np.random.rand(row*col, 2)
data = []
for i in range(row):
    for j in range(col):
        data.append([j, i])
data = np.array(data)
data = data / np.max(np.abs(data), axis=0)


lines = []
plt.ion()
fig = plt.figure(figsize=(12, 8))
plt.scatter(data[:,0], data[:,1], s=3, c='g')
#print(map[0:5,0])
show_map(row, col)

sigma0, T1, T2, learnRate0 = 3, 100, 1000, 3
t = 0
dataSize = data.shape[0]
while True:
    learnRate = learnRate0 * np.exp(-t/T2)
    sigma = sigma0 * np.exp(-t/T1)
    
    for index in range(dataSize):
        x = data[index,:]
        dists = np.linalg.norm(map-x, axis=-1)    
        minindex = np.argmin(dists, axis=-1)
        min_row = minindex // col
        min_col = minindex % col

        for i in range(row):
            for j in range(col):
                update = learnRate * np.exp((-np.abs(i-min_row)-np.abs(j-min_col)) / 2 / sigma**2) * (x - map[i*col+j,:])
                map[i*col+j,:] += update
    
    show_map(row, col)

    t += 1
plt.show()
