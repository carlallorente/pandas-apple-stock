from matplotlib import pylab as plt
import pandas as pd
import os #For changing the working directory

os.chdir('/Users/X412/OneDrive - IE Students/Desktop')

print("Current working directory: {0}".format(os.getcwd()))

dfMBG = pd.read_csv("MBG.DE.csv")
print(dfMBG.head())
dfMBG['Date'] = pd.to_datetime(dfMBG.Date)

dfBMW = pd.read_csv("BMW.DE.csv")
print(dfBMW.head())
dfBMW['Date'] = pd.to_datetime(dfBMW.Date)


index2 = []
for date2 in dfBMW.Date:
    if dfMBG.index[dfMBG.Date == date2].values.size:
        index2.append(int(dfMBG.index[dfMBG.Date == date2].values[0]))
print(index2)


mean = dfMBG["Close"].mean()


plt.figure("Mercedes vs BMW stocks in Germany")
plt.plot(dfMBG["Date"], dfMBG["Close"], 'r-', linewidth=0.6, color='blue', label="Mercedes stock price, mean="+str(mean))
plt.plot(dfBMW["Date"], dfBMW["Close"], 'r-', ms=7, color='green', linewidth=0.6, markevery=index2, label="BMW stock price, mean="+str(mean))
plt.xlabel("Dates")
plt.ylabel("Stock price")
plt.legend(loc="lower left", prop={'size': 7})

plt.show()

#Short analysis of the graph: The stock price of BMW is higher than the one for Mercedes
# They move in a similar way. At the end of the year 2021, they have experienced a shock
#this sock impacted more on Mercedes than on BMW
