import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

myData= pd.read_csv('accidentData.csv')


fatality=np.array(myData['Fatality'])
severeInjury=np.array(myData['Severe injury'])
minorInjury=np.array(myData['Minor injury'])
personsAffected=fatality+severeInjury+minorInjury
myData['Persons_Affected']=personsAffected
myData.to_csv('6932321.csv',index=True) 

fig,ax1=plt.subplots(figsize=(8.5,7))
ax1.plot('Year','Fatality','b',data=myData)
plt.title('Accident Data Graph',color='g')
ax1.set_ylabel('Fatality',color='m')
ax2=ax1.twinx()
ax2.plot('Year','Persons_Affected','r',data=myData)
ax2.set_ylabel('Persons_Affected',color='c')
plt.savefig('6932321.png')
plt.show()
