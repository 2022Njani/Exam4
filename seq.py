import numpy as np
import pandas as pd



# Function takes in the sequence, initializes an empty list c and 2 variables k and y. 
#k represents the length of the kmer and y represents the offset value so that when splicing the string
# we do not go out of range. Everytime we increase k we must increase y so that the loop does not go
#out of range. I do len(seq)+ 1 because we want to loop through all positions in the string
# d is a created list within the loop that stores all kmer possibilities fo that instance in the loop.
# I append that list d to list c to creat a list of lists that contain all splices of the string for
#every value of k.
def window(seq):
    c = []
    k= 0
    y = 0
    while k < len(seq) +1:
        d = [seq[i:i+k] for i in range(len(seq)-y+1)]
        c.append(d)
        k+=1
        y+=1
    c.pop(0)
    return c
   
 
#ary = window(a)
#ary.pop(0)
#print(ary)

# This function takes in the list of lists created in the first function. I initialize
# a list called unique_list because I will store all the lists unique values for each instance of k.
# I intialize i because of the loop. the variable x gets the list of lists from the first function 
# but now it is a pandas array. This allows me to use a function of pandas .unique to parse out any copies.
# I loop through each list within x and run the .unique function on it. It returns a list of lists
# that all have unique substrings.
def unique(ary):
    unique_list = []
    i=0
    x= pd.array(ary)
    print(x)
    for i in range(len(x[i])):
        unique_list.append(pd.unique(x[i]))
    
      
      
       
    print(unique_list)
    return unique_list
   



# This function takes in the unique list of lists that contain all the substrings for all values of k.
#I intialize a count list that will contain the lengths of each list in the list of lists unique_list.
#I run a loop that pops out each list within the unique_list and set a variable named counter to the length
# of the list that is being popped out. Lastly in the loop I append the counter to the count list so that at the end of
# the function I can return a list of integers that represent observed kmers.
def count_O_Kmers(unique_list):
    count_list = []
    for x_list in unique_list:
        print(x_list)
        counter = len(x_list)
        count_list.append(counter)
    print(count_list)
    return count_list
   
#count_list = count_O_Kmers(unique_list)
#print(count_list)


# This function takes in the sequence as its argument and intializes a list c anf variables k=1 n and y.
# The list c will be a list of the possible kmers, k represents the kmer value, n and y are intialzied
# so that they can become the two formulas fo Pkmer in the loop. x is given the length of the sequence
# In the loop n gets the first formula and y gets the second formula. I then have a string of
# conditionals that decifer which value (n or y) is smaller so that it can be appended to the list c.
# at the end of the loop I reintialize n and y to 0 so that I do not over add any values. k+=1 iterates
#the loop. returns a list of integers that represent the possible kmers for that string
def count_P_Kmers(seq):
    c= []
    k=1
    n=0
    y=0
    x = len(seq)
    while k < x+1:
        n= x - k +1
        y= 4**k
        if n < y:
            c.append(n)
        elif n==y:
            c.append(n)
        else:
            c.append(y)
        n=0
        y=0
        k+=1
    print(c)
    return c
       
#P_kmers = count_P_Kmers(a)
#print(P_kmers)

# This function takes in the sequence, the observed kmers list, and the possible kmers list. k_index
# is intialized as an empty list so that it be the column that represents the value of k. The loop
# creates a list of integers that go up to the length of the sequence. I then create a dataframe with
# columns being the k_index list, the observed kmers list, and  possible kmers list. Then I create 
# 2 new locations at the bottom of the dataframe using df.at. I create a new row total using 
#df.at called total and the two postions that are being filled are where the row total and where the cols
# observed kmers and possible kmers intersect. There we assign gthe sum of each column to their respective
# locations in the row total. Return df.
def create_df(seq,count_list,P_kmers):
    k_index = []
    for i in range(1,len(seq)+1):
        k_index.append(i)
    df = pd.DataFrame(list(zip(k_index,count_list,P_kmers)), columns = ['k','observed kmers', 'possible kmers'])
    df.at['total','observed kmers'] = df['observed kmers'].sum()
    df.at['total','possible kmers'] = df['possible kmers'].sum()
    return df

#df = create_df(a,count_list,P_kmers)
#df


#lc = df['observed kmers'].sum()/df['possible kmers'].sum()

#lc
# this function is responsible for opening my text file and looping through it to run all the functions on it.
#
def main():
  fn = open("test.txt","r+")
  file = [line.strip() for line in fn]
  for line in file:
    ary = window(line)
    
    unique_list =unique(ary)
    count_list = count_O_Kmers(unique_list)
    P_kmers = count_P_Kmers(line)
    df = create_df(line,count_list,P_kmers)
    lc = df['observed kmers'].sum()/df['possible kmers'].sum()
    print(df)
    print(lc)
    df.to_csv('test_0.csv',index=False, sep =' ', mode ='a')
    f= open("test_0.txt",'a')
    f.write(line +' ')
    f.write(str(lc)+ ' ')
    f.close()
  fn.close()
main()
   



  
    
  
