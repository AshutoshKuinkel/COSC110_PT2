def process_sales() -> list[list]:
  '''
  Write up docstring
  '''
  arr = []
  with open("sales.txt","r") as file:
    for transaction in file:
      # process each transaction:
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
  
def calc_total(fam_pass_a,fam_pass_b,adult,child):
  '''
  Write up docstring
  '''
  
  sales = process_sales()
  fam_a=0
  fam_b=0
  ad=0
  ch=0
  for transaction in sales:
    fam_a += (fam_pass_a * transaction[0])
    fam_b += (fam_pass_b * transaction[1])
    ad += (adult * transaction[2])
    ch += (child * transaction[3])
  return fam_a + fam_b + ad + ch
    
print(f"Total rev for this transaction: ${calc_total(16,16,5,4)}")

'''
Everything done step by step... not the best implementation in terms of time and space complexity, this will suffer hard under scale,
but built from logical principles started with this in online python interpreter. This serves basis of entire prorgam:

sales = [[1, 0, 0, 0],[0, 0, 2, 0],[0, 1, 1, 0],[2, 0, 0, 1]] {This is the entire purpose of process_sales functions to get our sales file data looking nice like this}

def calc_total(fam_pass_a,fam_pass_b,adult,child):
    fam_a=0
    fam_b=0
    ad=0
    ch=0
    for transaction in sales:
        fam_a += (fam_pass_a * transaction[0])
        fam_b += (fam_pass_b * transaction[1])
        ad += (adult * transaction[2])
        ch += (child * transaction[3])
    return fam_a + fam_b + ad + ch
    
print(f"Total rev for this transaction: ${calc_total(16,16,5,4)}")
'''

