import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Set to true to use KDE over histogram
use_kde = False

def analysis(file) :
    # Read file and remove first 10 rows
    data = pd.read_csv(file) 
    data = data.iloc[10:]

    print("Analysis of " + file)

    # Create collumn frame time and fps
    data['frame_time'] = data[' Time (ms)'] - data[' Time (ms)'].shift(1)
    data['fps'] = data['frame_time'].apply(lambda x: 1000/x)

    frame_time_avg = data['frame_time'].mean()
    frame_time_std_dev = data['frame_time'].std()
    fps_avg = data['fps'].mean()
    fps_std_dev = data['fps'].std()

    print("Frame Time Average", frame_time_avg)
    print("Frame Time Standard Deviation", frame_time_std_dev)
    print("Frames Per Second Average", fps_avg)
    print("Frames Per Second Standard Deviation", fps_std_dev)  
    print("FPS Percentiles:")  
    print("01:", data['fps'].quantile(q=0.01), "10:", data['fps'].quantile(q=0.1))  
    print("99:", data['fps'].quantile(q=0.99), "90:", data['fps'].quantile(q=0.9))  
    print("")  

    fig = plt.figure(num=file)
    fig.suptitle(file[0:file.find("frametimes.csv")], fontsize=16)

    plt.title('Frame Analysis')


    plt.subplot(2, 1, 1)
    plt.plot(data["Frame"], data["frame_time"])
    plt.xlabel('Frame Index')
    plt.ylabel('Frame Time (ms)')

    plt.subplot(2, 2, 3)
    plt.hist(data['fps'], bins = 300) if not use_kde else data['fps'].plot.kde()
    plt.xlabel('FPS')
    plt.ylabel('Occurrences')

    plt.subplot(2, 2, 4)
    data.boxplot(column='frame_time', vert = False)
    plt.xlabel('Frame Time')


    plt.show()

# Get file names which contain frame times
fileNames= [f for f in os.listdir('.') if os.path.isfile(f) and re.search(".*frametimes\.csv", f)]

if not len(fileNames) :
    exit();

plt.close("all")
for file in fileNames :
    analysis(file)