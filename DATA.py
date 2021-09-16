import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random 
import pandas as pd 
import csv 
df = pd.read_csv("studentMarks.csv") 
data = df["Math_score"].tolist() 

#plotting the graph 
fig = ff.create_distplot([data],["Math Scores"], show_hist= False) 
fig.show()

#finding mean and standard deviation
#mean = statistics.mean(data)
#std = statistics.stdev(data)
#print(mean,std)

#Sampling the data
def random_set_of_mean(counter):
  dataset = []
  for i in range(0,counter):
    random_index = random.randint(1,len(data)-1)
    value = data[random_index]
    dataset.append(value)
  mean = statistics.mean(dataset)
  return mean

mean_list= []
for i in range(0,1000):
  set_of_means = random_set_of_mean(100)
  mean_list.append(set_of_means)
  
std2 = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print(mean)

fig = ff.create_distplot([mean_list],["studentmarks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,20],mode = "lines",name = "NAME"))
fig.show()