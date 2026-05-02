# TO DO: Get program working in cli, then tranlsate to GUI.
# TO DO: Implement the logic which is almost done from test.py...
'''
Write up module docstring... Explaining the entire program, serves as a preface.
'''

import tkinter as tk;
from tkinter import ttk;

# root = tk.Tk()
# root.title("Pool Revenue Simulator")


# calc total rev func, given args:
def calc_ttl_revenue(fam_pass,adult,child):
  '''
  
  '''
  try:
    with open("sales.txt","r") as sales_file:
      # to do: loop through each transaction (which is each line in sales file) & then calculate the revenue based on what user sets it to be
      fam_p = 0
      ad = 0
      ch = 0
      for transaction in sales_file:
        # we can split the line into the fam pass a, fam pass b, adult, child... because transaction always layed out in that order 
        # (Format per line: Family_A_Count,Family_B_Count,Adult_Count,Child_Count {taken from assessment description}), seperated with commas.... so we can use like a split method here...
        fam_p += (fam_pass * int(transaction[0]))
        fam_p += (fam_pass * int(transaction[1]))
        ad += (adult * int(transaction[2]))
        ch += (child * int(transaction[3]))
      return fam_p + ad + ch  
        # or maybe we treat each transaction as an array... figure out price, then move onto next array (this probably requires more computation though)
  except FileNotFoundError:
    # TO DO: handle error gracefully here:
    print("File not found")

print(f"ttl rev: ${calc_ttl_revenue(16,5,4)}")
# main loop, run until user close window or press exit:
def main():
  # to do: ask user for prices for the 3 inputs..
  pass


# root.mainloop()


# I think the core logic should follow something like this:
# sales = [[1, 0, 0, 0],[0, 0, 2, 0],[0, 1, 1, 0],[2, 0, 0, 1]]
# 
# def calc_total(fam_pass_a,fam_pass_b,adult,child):
    # fam_a=0
    # fam_b=0
    # ad=0
    # ch=0
    # for transaction in sales:
        # fam_a += (fam_pass_a * transaction[0])
        # fam_b += (fam_pass_b * transaction[1])
        # ad += (adult * transaction[2])
        # ch += (child * transaction[3])
    # return fam_a + fam_b + ad + ch
    # 
# print(f"Total rev for this transaction: ${calc_total(16,16,5,4)}")