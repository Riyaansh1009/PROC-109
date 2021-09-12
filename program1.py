import statistics 
import csv
import pandas as pd
import plotly.figure_factory as ff 
import plotly.graph_objects as go



df = pd.read_csv("data.csv")
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)

mean = statistics.mean(new_data)
mode = statistics.mode(new_data)
median = statistics.median(new_data)
stDev = statistics.stDev(new_data)


firstStDevStart,  firstStDevEnd = mean-stDev, mean+stDev
listOfDataWithin1stDev = [result for result in new_data if result>firstStDevStart and result<firstStDevEnd]

secondStDevStart, secondStDevEnd = mean-2*stDev, mean+2*stDev
listOfDataWithin2stDev = [result for result in new_data if result>secondStDevStart and result<secondStDevEnd]

thirdStDevStart, thirdStDevEnd = mean-3*stDev, mean+3*stDev
listOfDataWithin3stDev = [result for result in new_data if result>thirdStDevStart and result<thirdStDevEnd]

graph = ff.create_distplot([new_data],["result"], show_hist=False)
graph.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17], mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[thirdStDevStart,thirdStDevStart],y=[0,0.17], mode="lines", name="stDev3"))
graph.add_trace(go.Scatter(x=[secondStDevStart,secondStDevStart],y=[0,0.17], mode="lines", name="stDev2"))
graph.add_trace(go.Scatter(x=[firstStDevStart,firstStDevStart],y=[0,0.17], mode="lines", name="stDev1"))
graph.add_trace(go.Scatter(x=[thirdStDevEnd,thirdStDevEnd],y=[0,0.17], mode="lines", name="stDevEnd3"))
graph.add_trace(go.Scatter(x=[secondStDevEnd,secondStDevEnd],y=[0,0.17], mode="lines", name="stDevEnd2"))
graph.add_trace(go.Scatter(x=[firstStDevEnd,firstStDevEnd],y=[0,0.17], mode="lines", name="stDevEnd3"))


graph.show()