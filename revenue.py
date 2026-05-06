'''
revenue.py : CodeTown Public Pool GUI sales-review program.

The purpose of this program is to receive an input for the prices of the family pass tickets, 
adult tickets and child tickets and calculate the revenue based on those prices and the ticket
amounts based on the sales.txt file.

The approach taken to solve this problem was to first present the re-sizable GUI to the user,
prompting them to enter the respective prices. Once the prices were validated (if no input,
default to values in assingment 1) the program opens the sales.txt file, if the file doesn't
exist in the directory, a FileNotFound error message was displayed to the user using tkinter's
messagebox module. So once confirming the sales.txt file existed within the directory the program
then we process each line of the sales.txt file, and form a list of lists. Finally, we then
iterate over our lists of lists to multiply the amount of all ticket groups (adult,child,fam pass)
by the user's price inputs and return the total revenue.

Run revenue.py to experience the GUI system and calculate the total revenue based on transactions
and input prices.
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Helper to process sales:
def process_sales() -> list[list]:
  '''
  Outputs all trasnactions listed within sales.txt file cleanly into a list of lists.
  
  Args:
    (None): No explicit Args, instead function relies on existence of sales.txt file
  
  Returns:
    list[list]: One list containing all transactions which are also stored in a list
                i.e. sales = [[1,0,0,1],[0,0,2,1]].
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
    # pop up message, this is handled using messagebox module rather than alerting user with label
    # on screen:
    messagebox.showerror("FileNotFoundError",'''Error: sales.txt not found. Please ensure the
                         file is in the same directory.''')
  
# Helper to calculate total revenue:
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
  # call our processed sales i.e. list of lists, to iterate over:
  sales = process_sales()
  
  # the only way we hit this is condition is if we go to the except statement,
  # in process_sales(), which only occurs when the file sales.txt hasn't been found.
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

# Initialising our GUI setup:
root = tk.Tk()

root.title("Pool Revenue Simulator")

# Elements in window should expand, as window expands,
# key aspect of resizeability:
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# Don't want default window size to be too big or small,
# this 600x350 resolution seems to work well across all
# devices/platforms as a default:
root.geometry("600x350")

frame = ttk.Frame(root, padding=10)
frame.grid(column = 0, row = 0,sticky="NSEW")

# We don't want the label to expand as page expands, only the entry fields (on column1)
# should expand 3x more than column 0:
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

default_values_label = ttk.Label(frame,
                         text='''Default Values: Family pass: $16.00, Adult: $5.00, Child: $4.00''',
                         foreground="grey",
                         font=("Arial",10))

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
                foreground="green",
                anchor="center"
                )

def on_submit() -> None:
  '''
  Called when user clicks calculate button in GUI. Receives input entered in entry fields & calls
  calc_total() function provided input is valid.
  
  Args:
    (None) : No arguments passed explicitly to the function.
    
  Returns:
    (None) : Only updates result_var label with the updated total revenue based on
             user's input prices.
  '''
  try:
    # either checking user has entered appropriate values else using default values from AT1, as
    # outlined in assingment description:
    fam_pass_price = float(fam_pass_entry.get() or 16.00)
    adult_price = float(adult_entry.get() or 5.00)
    child_price = float(child_entry.get() or 4.00)
    
    # Enforce non-negative price rules, in accordance with AT2 task description:
    bad_entry = False
    if (fam_pass_price < 0 or adult_price < 0 or child_price < 0):
      bad_entry = True
      messagebox.showerror("Input Error:","Error: All prices must be non-negative.")
      
    # output message:
    if(not bad_entry):
      total = calc_total(fam_pass_price,adult_price,child_price)
      
      # Prevent calculation in the event of missing file:
      if total is None:
        bad_entry = True
      else:
        result_var.set(f"Total Revenue: ${total:.2f}")
  except ValueError:
    messagebox.showerror("ValueError:","Error: Prices must be numeric.")

# button widget placed seperately to all other widgets, as python requires
# on_submit function to be defined before trying to call it.
button = ttk.Button(frame,text="Calculate Revenue",command=on_submit)

# placing all widgets with grid (without placing the labels, it'll
# have an address in memory but won't be able to be seen):    
label.grid(column = 0, row = 0,columnspan=2,sticky="nsew")
prompt_label.grid(column=0,row=1,columnspan=2,pady=7)
default_values_label.grid(column=0,row=2,columnspan=2)
fam_pass_label.grid(column=0, row=3, sticky="e", padx=5)
fam_pass_entry.grid(column=1, row=3, sticky="ew", padx=5,pady=5)
adult_label.grid(column=0, row=4, sticky="e", padx=5)
adult_entry.grid(column=1, row=4, sticky="ew", padx=5,pady=5)
child_label.grid(column=0, row=5, sticky="e", padx=5)
child_entry.grid(column=1, row=5, sticky="ew", padx=5,pady=5)
button.grid(pady=15,column=0,row=6,columnspan=2)
result_label.grid(column=0, row=7, columnspan=2,sticky="ew")


root.mainloop()
