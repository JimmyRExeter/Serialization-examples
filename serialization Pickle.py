from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import pickle
from channel import TranChannel


#Create the channel Object
chan = TranChannel("98_7707.001")
# Plot it
chan.plotit()
# create afile to Pickel up the Channel
channelfile = open("pickledchan.dat","wb")
#Pickle it into the file
pickle.dump(chan,channelfile)
pickle.dump(chan.timelist,channelfile)
pickle.dump(chan.datalist,channelfile)
channelfile.close
print('pickled')






   