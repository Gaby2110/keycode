import matplotlib.pyplot as plt

def graph_1(li):
    plt.plot(range(0,len(li)), li)

def graph_2(li):
    plt.scatter(range(0,len(li)), li)
    
def graph_3(li):
    plt.bar(range(0,len(li)),li)