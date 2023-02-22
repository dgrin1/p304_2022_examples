import numpy as np #import librraries

search_list=np.loadtxt('gistfile1.txt',dtype=str)    #gistfile1.txt read bunch of text into an array
i=0 # start near 0

q=str(input("Word to search for?"))   #ask user what they are interested in

success=[]

key=-1      #assume we haven't found it yet
while i<np.size(search_list):    #try every element in the list
	print(i,search_list[i])   #print where I am in the list
	if(search_list[i]==q):   #if equal to string of interest, change key to be the location in the list of target text
		key=i
		success.append[i]
	i+=1 #increment yourself
	
if (key!=-1): #found it
	print('Found '+q+' at index='+str(key))
else:
	print('String not found')