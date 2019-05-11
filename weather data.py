import urllib.request, json
from tkinter import *
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


class Place:
    def __init__(self, gps, name):
        self.gps = gps
        self.name = name


class Window:
    def __init__(self, window):
        self.window = window
        self.subframe = tk.Frame(master=window)
        self.variable = StringVar()
        self.variable.set('temperature')
        self.check_buttons_list = {'A Basin': (Place('39.6673,-105.8649', 'A Basin'), IntVar()),
                                   'Winter Park': (Place('39.8869,-105.779', 'Winter Park', ), IntVar()),
                                   'Copper': (Place('39.47523,-106.15228', 'Copper'), IntVar())}
        Button(self.subframe, text='Graph Data', command=lambda: self.graph_data(self.check_buttons_list)).grid()
        Button(self.subframe, text='Tester', command=lambda: tester(self, self.check_buttons_list)).grid()
        Radiobutton(self.subframe, text='Temperature', variable=self.variable, value='temperature').grid()
        Radiobutton(self.subframe, text='Wind speed', variable=self.variable, value='wind').grid()
        for button in self.check_buttons_list:
            Checkbutton(self.subframe, text=button, variable=self.check_buttons_list[button][1], onvalue=1).grid()
        self.test_var = IntVar()
        Checkbutton(self.subframe, text='tester', variable=self.test_var).grid()
        self.subframe.grid()
        self.fig = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)

    def graph_data(self, checkbutton_list):
        df = pd.DataFrame()
        ax = self.fig.add_axes([.1, .2, .8, .7])
        ax.clear()
        names = list()
        for place in checkbutton_list:
            if checkbutton_list[place][1].get() == 1:
                print(checkbutton_list[place][0].gps)
                df = get_data(checkbutton_list[place][0].gps)
                print(df.info())
                df['wind'] = df['windSpeed'].str.slice(0, 2)
                plt.plot(df[self.variable.get()])
                print(place)
                names.append(place)
        try:
            plt.legend(names)
            df['datetime'] = pd.to_datetime(df['startTime'].str.slice(2, 10), yearfirst=True)
            ax.set_xticks(range(3, len(df['datetime']), 12))
            print(df['datetime'])
            ax.plot(df[self.variable.get()])
            plt.tick_params(axis='x', labelrotation=45.0)
            self.canvas.get_tk_widget().grid(column=1, row=0)
            self.canvas.draw()
        except KeyError:
            print('check a box')


def get_data(gps):
    url = 'https://api.weather.gov/points/' + gps
    data = urllib.request.urlopen(url)
    j_data = json.loads(data.read().decode())
    forecast = json.loads((urllib.request.urlopen(j_data['properties']['forecastHourly'])).read().decode())
    df = pd.DataFrame(forecast['properties']['periods'])
    return df #consider updating the app if it's left running for a long period of time


def tester(frame, check_buttons_list):
    print(check_buttons_list)
    for thing in check_buttons_list:
        print(check_buttons_list[thing][1])
        print(frame.check_buttons_list[thing][1].get())
    pass


def main():
    root = Tk()
    a = Window(root)
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()

