import plotly.figure_factory as ff
import pandas as pd
import csv 
import random 
import statistics
import plotly.graph_objects as go

df = pd.read_csv("class 111.csv")
data = df["Math_score"].tolist()

def random_test_subjects():
    data_set=[]
    for i in range(1,100):
        random_index=random.randint(0, len(data)-1)
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)
    return mean
mean_list=[]
for i in range(0,1000):
    set_of_mean=random_test_subjects()
    mean_list.append(set_of_mean)
    

fig = ff.create_distplot([data],["Math Scores"],show_hist = False)
"""fig.show()"""



mean=statistics.mean(mean_list)
print(mean)
stdv=statistics.stdev(mean_list)
print(stdv)

first_std_deviation_start, first_std_deviation_end = mean-stdv, mean+stdv
second_std_deviation_start, second_std_deviation_end = mean-(2*stdv), mean+(2*stdv)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdv), mean+(3*stdv)


fig = ff.create_distplot([mean_list],["Math Scores"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))


z_score = (mean - mean_of_sample2)/stdv
print("The z score is = ",z_score)fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
