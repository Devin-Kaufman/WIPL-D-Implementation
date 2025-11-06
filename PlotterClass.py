import matplotlib.pyplot as plt
import numpy as np
import csv

class DataPlotter:

    #Initializing the class, just using the filename as a pass so that we can parse it later
    def __init__(self, fileName, title="Data Plot", x_label="X-axis", y_label="Y-axis"):
        self.fileName = fileName
        self.title = title
        self.x_label = x_label
        self.y_label = y_label


    #Reading the CSV and more properly storing it, each row is a gen with each column being a separate design
    def readCSV(self):
        self.x_data = []
        self.y_data = []
        counter = 1

        with open(self.fileName, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.x_data.append(float(row[0]))
                self.y_data.append(counter)
                counter += 1


    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.x_data, self.y_data, marker='o', linestyle='-', color='b')
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.grid(True)
        plt.show()

    def convergencePlot(self):
        #nothing here for now
        pass