'''
Write up module docstring... Explaining the entire program, serves as a preface.
'''

import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox

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
    messagebox.showerror("File Error","Error: sales.txt not found. Please ensure the file is in the same directory.")
  
# Helper to calculate total revenue:
# TO DO: SET DEFAULT VALUES OF THESE TO WHAT THEY WERE IN AT1:
def calc_total(fam_pass:float,adult:float,child:float)-> float | None :
  '''
  Outputs total revenue by adding all revenue of all individual transactions.
  
  Args:
    fam_pass (float): User set price of family pass.
    adult (float): User set price of adult ticket.
    child (float): User set price of child ticket.
  
  Returns:
    (float | None): Total revenue for all transactions, (None if transaction file missing).
  '''
  
  sales = process_sales()
  if not sales:
    return None
  fam_p=0
  ad=0
  ch=0
  for transaction in sales:
    fam_p += (fam_pass * transaction[0])
    fam_p += (fam_pass * transaction[1])
    ad += (adult * transaction[2])
    ch += (child * transaction[3])
  return float(fam_p + ad + ch)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Pool Revenue Simulator")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.geometry("600x330")

frame = ttk.Frame(root, padding=10)
frame.grid(column = 0, row = 0,sticky="NSEW")
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=3)

# Creating all widgets required:
label = tk.Label(frame,
                  text="Welcome to CodeTown Public Pool\n Revenue Calculator!",
                  justify='center',
                  anchor='center',
                  font=("Arial",24,"bold"),
                  foreground="white",
                  background="blue")

prompt_label = ttk.Label(frame,
                         text='''Enter simulation values & press calculate:''',
                         font=("Arial",16))

fam_pass_label = ttk.Label(frame,text="Family Pass Price:")

fam_pass_entry = ttk.Entry(frame)

adult_label = ttk.Label(frame,text="Adult Ticket Price:")

adult_entry = ttk.Entry(frame)

child_label = ttk.Label(frame,text="Child Ticket Price:")

child_entry = ttk.Entry(frame)

result_var = tk.StringVar()

result_label = ttk.Label(frame,
                textvariable=result_var,
                font=("Arial",18),
                foreground="green"
                )

def on_submit() -> None:
  '''
  Write up docstring..
  '''
  try:
    # either checking user has entered appropriate values else using default values from AT1, as outlined in assingment description:
    fam_pass_price = float(fam_pass_entry.get() or 16.00)
    adult_price = float(adult_entry.get() or 5.00)
    child_price = float(child_entry.get() or 4.00)
    
    # Enforce non-negative price rules, in accordance with AT2 task description:
    bad_entry = False
    if (fam_pass_price < 0 or adult_price < 0 or child_price < 0):
      bad_entry = True
      messagebox.showerror("Input Error:","Error: All prices must be non-negative.")
    
    # Prevent calculation in the event of missing file:
    total = calc_total(fam_pass_price,adult_price,child_price)
    if total is None:
      bad_entry = True
      
    # output message:
    if(not bad_entry):
      result_var.set(f"Total Revenue: ${total:.2f}")
  except ValueError:
    messagebox.showerror("ValueError:","Error: Prices must be numeric.")

button = ttk.Button(frame,text="Calculate Revenue",command=on_submit)

# placing all widgets with grid:    
label.grid(column = 0, row = 0,columnspan=2,sticky="nsew")
prompt_label.grid(column=0,row=1,columnspan=2,pady=7)
fam_pass_label.grid(column=0, row=2, sticky="e", padx=5)
fam_pass_entry.grid(column=1, row=2, sticky="ew", padx=5,pady=5)
adult_label.grid(column=0, row=3, sticky="e", padx=5)
adult_entry.grid(column=1, row=3, sticky="ew", padx=5,pady=5)
child_label.grid(column=0, row=4, sticky="e", padx=5)
child_entry.grid(column=1, row=4, sticky="ew", padx=5,pady=5)
button.grid(pady=15,column=0,row=5,columnspan=2)
result_label.grid(column=0, row=6, columnspan=2)



# main loop, run until user close window or press exit:
def main():
  # to do: ask user for prices for the 3 inputs..
  pass


root.mainloop()

if __name__ == "__main__":
  main()


'''
Everything done step by step... not the best implementation in terms of time and space complexity, this will suffer hard under scale,
but built from logical principles started with this in online python interpreter. This small peice serves basis of entire prorgam:

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
