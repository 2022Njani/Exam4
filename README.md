My program when run using the command line, outputs the linguistic complexity of
each sequence in a file of sequences and a dataframe for that sequence. To run my program just type in the name of my 
python script. I did not utilize the parser argument functions because I was not inputting anything on the command line 
with my script. I see now that K was suppose to be an arugment on the command line but my code still works so that it gets
all possiblities. 

window function : # Function takes in the sequence, initializes an empty list c and 2 variables k and y. 
k represents the length of the kmer and y represents the offset value so that when splicing the string we do not go out of
 range. Everytime we increase k we must increase y so that the loop does not go out of range. I do len(seq)+ 1 because we
 want to loop through all positions in the string  d is a created list within the loop that stores all kmer possibilities
 fo that instance in the loop. I append that list d to list c to creat a list of lists that contain all splices of the
 string for every value of k.


unique function: This function takes in the list of lists created in the first function. I initialize
 a list called unique_list because I will store all the lists unique values for each instance of k.
 I intialize i because of the loop. the variable x gets the list of lists from the first function 
 but now it is a pandas array. This allows me to use a function of pandas .unique to parse out any copies.
 I loop through each list within x and run the .unique function on it. It returns a list of lists
 that all have unique substrings.


count_O_Kmers function:  This function takes in the unique list of lists that contain all the substrings for all values 
of k. I intialize a count list that will contain the lengths of each list in the list of lists unique_list.
I run a loop that pops out each list within the unique_list and set a variable named counter to the length
 of the list that is being popped out. Lastly in the loop I append the counter to the count list so that at the end of
 the function I can return a list of integers that represent observed kmers.


count_P_Kmers function: This function takes in the sequence as its argument and intializes a list c anf variables k=1
 n and y. The list c will be a list of the possible kmers, k represents the kmer value, n and y are intialzied
 so that they can become the two formulas fo Pkmer in the loop. x is given the length of the sequence
 In the loop n gets the first formula and y gets the second formula. I then have a string of
 conditionals that decifer which value (n or y) is smaller so that it can be appended to the list c.
 at the end of the loop I reintialize n and y to 0 so that I do not over add any values. k+=1 iterates
the loop. returns a list of integers that represent the possible kmers for that string

creat_df function: This function takes in the sequence, the observed kmers list, and the possible kmers list. k_index
 is intialized as an empty list so that it be the column that represents the value of k. The loop
 creates a list of integers that go up to the length of the sequence. I then create a dataframe with
 columns being the k_index list, the observed kmers list, and  possible kmers list. Then I create 
 2 new locations at the bottom of the dataframe using df.at. I create a new row total using 
 df.at called total and the two postions that are being filled are where the row total and where the cols
 observed kmers and possible kmers intersect. There we assign gthe sum of each column to their respective
 locations in the row total. Return df.

main function: # this function is responsible for opening my text file and looping through it to run all the functions on it.
# It is also responsible  for finding the lc and wrting the file out. I run a loop in my main function
# so that it performs all the functions on every string in the file. lc is found by taking the sum of
#observed kmers and dividing it by possible kmers sum. I write out to 2 files, one csv and one txt.
#I close both files and run main().
