n=int(input()) #input integer
nlist1=list(str(n))#turns integer  into a list of string numbers
if len(nlist1) % 2 ==0: #checks to see if list has an even number of items
    midnumidx= int((len(nlist1)/2)-1)   #gets the index value of middle number
elif len(nlist1) % 2 !=0:   #condition if there is odd number of items in list
    midnumidx= int((len(nlist1)/2)-(1/2))
nlist2=[int(i) for i in nlist1] #turns string list of numbers into a list of integers
fhalfsum= sum(nlist2[0:midnumidx+1]) #finds the sum of the first half of the list of integers
shalfsum= sum(nlist2[midnumidx+1:]) #finds the sum of the second half of the list
if fhalfsum==shalfsum: #if the sum of the first half of the list is equal to the sum of 
    return True        #the second half of the list, returns True
elif fhalfsum!=shalfsum:  #if the sum of the first half of the list is not equal to the sum of
    return False          #the second half of the list, returns False
 
