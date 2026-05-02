# TO DO: Get program working in cli, then tranlsate to GUI.
'''
Write up module docstring... Explaining the entire program, serves as a preface.
'''

import tkinter as tk;
from tkinter import ttk;

root = tk.Tk()
root.title("Pool Revenue Simulator")


# calc total rev func, given args:
def calc_ttl_revenue(*prices_user_set):
  '''
  
  '''
  try:
    with open("sales.txt","r") as sales_file:
      # to do: loop through each transaction (which is each line in sales file) & then calculate the revenue based on what user sets it to be
      for transaction in sales_file:
        # we can split the line into the fam pass a, fam pass b, adult, child... because transaction always layed out in that order, seperated with commas.... so we can use like a split method here...
        
        pass
  except FileNotFoundError:
    pass
  
# main loop, run until user close window or press exit:
def main():
  # to do: ask user for prices for the 3 inputs..
  pass


root.mainloop()
