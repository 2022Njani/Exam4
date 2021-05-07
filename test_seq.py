from seq import *
import numpy as np
from numpy.testing import assert_array_equal
import pandas as pd
# Tests the window function for the first string 
def test_window():
  seq = 'ATTTGGATT'
  actual_result = window(seq)
  expected_result = [['A', 'T', 'T', 'T', 'G', 'G', 'A', 'T', 'T'], ['AT', 'TT', 'TT', 'TG', 'GG', 'GA', 'AT', 'TT'], ['ATT', 'TTT', 'TTG', 'TGG', 'GGA', 'GAT', 'ATT'], ['ATTT', 'TTTG', 'TTGG', 'TGGA', 'GGAT', 'GATT'], ['ATTTG', 'TTTGG', 'TTGGA', 'TGGAT', 'GGATT'], ['ATTTGG', 'TTTGGA', 'TTGGAT', 'TGGATT'], ['ATTTGGA', 'TTTGGAT', 'TTGGATT'], ['ATTTGGAT', 'TTTGGATT'], ['ATTTGGATT']]
  assert actual_result == expected_result
#Tests the window function for the second string 
def test_window1():
  seq = 'ATGGA'
  actual_result = window(seq)
  expected_result = [['A', 'T', 'G', 'G', 'A'], ['AT', 'TG', 'GG', 'GA'], ['ATG', 'TGG', 'GGA'], ['ATGG', 'TGGA'], ['ATGGA']]
  assert actual_result == expected_result
# This fails the py.test because  actual_result is stored into a something other than a pandas array. I tried to find 
#the type of list it is stored in but could not find an example of the error is was running into. I know my output
# should be a pandas array since that is what is being returned but for some reason the unique_list gets a different type when the function is ran.
def test_unique():
  ary = [['A', 'T', 'G', 'G', 'A'], ['AT', 'TG', 'GG', 'GA'], ['ATG', 'TGG', 'GGA'], ['ATGG', 'TGGA'], ['ATGGA']]
  actual_result = unique(ary)
  expected_result= pd.array([['A', 'G', 'T'], ['AT', 'GA', 'GG', 'TG'], ['ATG', 'GGA', 'TGG'], ['ATGG', 'TGGA'], ['ATGGA']])
  assert actual_result == expected_result
#Tests the count_O_Kmers function for the first string  
def test_count_O_Kmers():
  unique_list = pd.array([['A', 'G', 'T'], ['AT', 'GA', 'GG', 'TG'], ['ATG', 'GGA', 'TGG'], ['ATGG', 'TGGA'], ['ATGGA']])  #[array(['A', 'G', 'T'], dtype='<U1'), array(['AT', 'GA', 'GG', 'TG'], dtype='<U2'), array(['ATG', 'GGA', 'TGG'], dtype='<U3'), array(['ATGG', 'TGGA'], dtype='<U4'), array(['ATGGA'], dtype='<U5')]
  actual_result = count_O_Kmers(unique_list)
  expected_result = [3, 4, 3, 2, 1]
  assert actual_result == expected_result
# Follows same method as first one but fails, Tried to use np and pd but still says it is not 1-d. I dont understand how this happend 
# since the form for unique list is the same as before but does not work here.
def test_count_O_Kmers1():
  unique_list = pd.array([['A' 'T' 'G'], ['AT' 'TT' 'TG' 'GG' 'GA'], ['ATT' 'TTT' 'TTG' 'TGG' 'GGA' 'GAT'], ['ATTT' 'TTTG' 'TTGG' 'TGGA' 'GGAT' 'GATT'], ['ATTTG' 'TTTGG' 'TTGGA' 'TGGAT' 'GGATT'], ['ATTTGG' 'TTTGGA' 'TTGGAT' 'TGGATT'], ['ATTTGGA' 'TTTGGAT' 'TTGGATT'], ['ATTTGGAT' 'TTTGGATT'], ['ATTTGGATT']])  
  actual_result = count_O_Kmers(unique_list)
  expected_result = [3, 5, 6, 6, 5, 4, 3, 2, 1]
  assert actual_result == expected_result
#Tests count_P_Kmers for the first string  
def test_count_P_Kmers():
  seq = "ATGGA"
  actual_result = count_P_Kmers(seq)
  expected_result = [4, 4, 3, 2, 1]
  assert actual_result == expected_result
#Tests count_P_Kmers for the second string   
def test_count_P_Kmers1():
  seq = "ATTTGGATT"
  actual_result = count_P_Kmers(seq)
  expected_result = [4, 8, 7, 6, 5, 4, 3, 2, 1]
  assert actual_result == expected_result
  


