
# Helper to process sales:
def process_sales() -> list[list]:
  '''
  Outputs all trasnactions listed within sales.txt file cleanly into a list of lists.
  
  Args:
    No explicit Args, instead function relies on existence of sales.txt file
  
  Returns:
    list[list]: One list containing all transactions which are also stored in a list i.e. sales = [[1,0,0,1],[0,0,2,1]].
  '''
  arr = []
  try:
    with open("sales.txt","r") as file:
      for transaction in file:
        # process each transaction (i.e. each line):
        x = transaction.split(",")
    
        for y in x:
          y = y.strip() #helps to remove \n character from final value in each transaction list
          y = int(y) 
          arr.append(y) # append all numbers from sales file into arr..
        
      n = 4
      res=[]
      # break arr into chunks of 4, to get list of lists:
      for i in range(0,len(arr),n):
        res.append(arr[i:i+n])
      
      return res
  except FileNotFoundError:
    # TO DO: HANDLE FILE NOT FOUND ERROR PROPERLY
    print("File not found Error...")
  
# Helper to calculate total revenue:
# TO DO: SET DEFAULT VALUES OF THESE TO WHAT THEY WERE IN AT1:
def calc_total(fam_pass:float,adult:float,child:float)-> float:
  '''
  Outputs total revenue by adding all revenue of all individual transactions.
  
  Args:
    fam_pass (float): User set price of family pass.
    adult (float): User set price of adult ticket.
    child (float): User set price of child ticket.
  
  Returns:
    (float): Total revenue for all transactions.  
  '''
  
  sales = process_sales()
  fam_p=0
  ad=0
  ch=0
  for transaction in sales:
    fam_p += (fam_pass * transaction[0])
    fam_p += (fam_pass * transaction[1])
    ad += (adult * transaction[2])
    ch += (child * transaction[3])
  return fam_p + ad + ch
    
print(f"Total rev for this transaction: ${calc_total(18.5,6,4.5)}")

