from __future__ import print_function
import csv
import mmap
import plotly.plotly as py
from plotly.graph_objs import *
from datetime import datetime
import plotly.tools as tls


dataFile = open('/home/pi/plotly/data.csv', 'a+')
doneFile = open('/home/pi/plotly/done.log', 'a+')

m = mmap.mmap(doneFile.fileno(), 0, access=mmap.ACCESS_READ)

dataR = csv.DictReader(dataFile)

tInList = []
tdList = []
for row in dataR:

    if m.find(str(row)) != -1:
        n = 1
    else:
        inInt = int(row['in'])
        outInt = int(row['out'])
        monthInt = int(row['month'])
        dateInt = int(row['date'])
        hourInt = int(row['hour'])
        minuteInt = int(row['minute'])
        secondInt = int(row['second'])
        td = datetime(year=2015, month=monthInt, day=dateInt, hour=hourInt, minute=minuteInt, second=secondInt)
        tInList.append(inInt)
        tdList.append(td)
        print("New Plot")
        #Plotting the Total In Count *1
        inStream = py.Stream('vts52yaho1')
        inStream.open()
        inStream.write(dict(x=td, y=inInt))
        inStream.close()
        #End of *1
        #Plotting the Total Out Count
#        outStream = py.Stream('nhzfl55ut2')
#        outStream.open()
#        outStream.write(dict(x=td, y=outInt))
#        outStream.close()
        print(row, file = doneFile)
      
#stream = Stream(
#    token='9bfuux3mfq',
#    maxpoints=50
#)
#TotalIn = Scatter(
#x=tdList,
#y=tInList,
#x=[],
#y=[],
#mode="lines+markers",
#stream=stream
#)
#data = Data([TotalIn])
#layout = Layout(title='Stream In Test 2')
#fig = Figure(data=data, layout=layout)
#unique_url = py.plot(fig, filename='Stream In Test 2')
