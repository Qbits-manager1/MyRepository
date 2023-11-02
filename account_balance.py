import csv
"""function to return the available balance in the account """
def get_balance(acc_no):
  # open the file in read mode
  filename = open('balance.csv', 'r')
  # create dictreader object to read the data from file
  file = csv.DictReader(filename) 
  # iterate over each row and append values to empty list
  for col in file:       
    if col['Account number'] == acc_no:
      return float(col['Balance'])
  return False 
