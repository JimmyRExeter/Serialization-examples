import io
import struct
import matplotlib.pyplot as plt
import numpy as np

infile= open("binarychan.jer","rb")

bytein = infile.read(8) # 8 bytes for a double
fileVersion = struct.unpack("d",bytein)[0]
print(fileVersion)

bytein = infile.read(255)
cn = struct.unpack("255s",bytein)[0]
cn = str(cn,'ascii')
ab = cn.strip(' ')
print(ab)

bytein = infile.read(8) # 8 bytes for a double
tof = struct.unpack("d",bytein)[0]
print(tof)

bytein = infile.read(8) # 8 bytes for a double
SI = struct.unpack("d",bytein)[0]
print(SI)

bytein = infile.read(8) # 8 bytes for a unsignedlonglong
DataCount = struct.unpack("q",bytein)[0]
print(DataCount)

datalist = []
timelist = []


for i in range(DataCount):
  bytein = infile.read(8) # 8 bytes for a dluble
  Datapoint = struct.unpack("d",bytein)[0]  
  datalist.append(Datapoint)
  time = tof + (i * SI)
  timelist.append(time)


TD = np.array(timelist)
PD = np.array(datalist)
plt.title(ab)
plt.ylabel('g')
plt.xlabel("time (s)")
plt.plot(TD, PD)
plt.show()



