from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import pickle


channelfile2 = open("pickledchan.dat","rb")
chan2 = pickle.load(channelfile2)
chan2.timelist = pickle.load(channelfile2)
chan2.datalist = pickle.load(channelfile2)
channelfile2.close


print(chan2)
chan2.plotit()







   