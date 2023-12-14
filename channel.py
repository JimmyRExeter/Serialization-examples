from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import struct

'''Class to Hold Channel Data '''
class TranChannel:
    NameOfChannel : str
    Filename : str
    unit : str
    TOF : float # time of the first sample
    NOS : int   # number of samples
    SamplingInterval : float ## sampling rate
    datalist = []
    timelist = []
    headerlist = []
    def __repr__(self):
        return (self.NameOfChannel)
    '''Extract Useful info from the header
     Time of First Sample
     Sample Interval
     Name of the channel
     Mechanical Unit'''
    def __ProcessHeader(self):
        for i in self.headerlist:
            tempstring = i[0]
            temp2 = i[1]
            tempstring = tempstring.strip()
            if tempstring == "Time of first sample":
                self.TOF = float(temp2)
            if tempstring == "Sampling interval":
                self.SamplingInterval = float(temp2)    
            if tempstring == "Name of the channel":
                self.NameOfChannel = temp2 
            if tempstring == "Unit":
                self.unit = temp2   
        print(f"Time of First Sample is {self.TOF}")            
        print(f"Sample Interval is {self.SamplingInterval}") 

    '''Load the channel data from the File'''
    def __LoadChannel(self):
        ## checkiffileexists
        
        infile = open(self.Filename)
        rawcontents = infile.readlines()
        #print(rawcontents)
        infile.close()
        dcount = 0
        for i in rawcontents:
          split = i.split(':',1)
          if len(split) <= 1:
              self.datalist.append(float(split[0]))
              self.timelist.append(float(dcount))
              dcount +=1
          else:
            self.headerlist.append(split)   
       # print(self.headerlist)

        self.__ProcessHeader()

        for i in range(0,len(self.timelist)):
            self.timelist[i] = self.TOF + (i * self.SamplingInterval )
       # print(self.datalist)      


    def __init__(self,filename):
        self.Filename = filename
        res = self.__LoadChannel()

    def saveit(self):

        TD = np.array(self.timelist)
        PD = np.array(self.datalist)
        TD.tobytes()
        PD.tobytes()

        # binarychan.jer is the filename to save into
        f= open("binarychan.jer","wb")
        temp = float(1.01) ## create aVERSION NUMBER
        byteout = struct.pack("d",temp) 
        written = f.write(byteout)
        print(f"File Bytes Written Version = {written}")  



        temp = self.NameOfChannel
        while len(temp) < 255 : temp +=' '
        
        arr2 = bytes(temp, 'ascii')
        stringsize = ("255s")
        byteout = struct.pack(stringsize,arr2)
        bsize = len(arr2)
        print(bsize)
        written = f.write(byteout)
        print(f"File Bytes Written Nameofchan = {written}")

        temp = float(self.TOF)
        byteout = struct.pack("d",temp) 
        written = f.write(byteout)
        print(f"File Bytes Written TimeOfFirst = {written}")   
        
        temp = self.SamplingInterval
        byteout = struct.pack("d",temp) 
        written = f.write(byteout)
        print(f"File Bytes Written SI = {written}") 

        datalen = int(len(self.datalist))
        print(f" datalen = {datalen}") 
        bytesout = struct.pack("q",datalen)
        written = f.write(bytesout) 

        print(f"File Bytes Written datacount = {written}") 


        datasize = ("d") 

        for i in range(datalen):       
          bytesout = struct.pack(datasize,self.datalist[i])
          written = f.write(bytesout)
        print(f"File Bytes Written Data = {written* datalen}") 

        f.close


    '''Plot the channel '''
    def plotit(self):
        TD = np.array(self.timelist)
        PD = np.array(self.datalist)
        plt.title(self.NameOfChannel)
        plt.ylabel(self.unit)
        plt.xlabel("time (s)")
        plt.plot(TD, PD)
        plt.show()
