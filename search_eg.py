import numpy as np

search_list=np.loadtxt('gistfile1.txt',dtype=str)
i=0

q=str(input("Word to search for?"))

key=-1
while i<np.size(search_list):
	print(i)
	if(search_list[i]==q):
		key=i
	i+=1
	
if (key!=-1):
	print('Found '+q+' at index='+str(key))
else:
	print('String not found')