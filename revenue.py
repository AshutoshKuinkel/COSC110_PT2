# TO DO: implement logic
'''
TASK:
The program must assume there is a file named sales.txt in the current working directory. Each line in this file represents a single transaction (one group entering the pool) and contains four integers separated by commas.

Format per line: Family_A_Count,Family_B_Count,Adult_Count,Child_Count

Example sales.txt:

1, 0, 0, 0
0, 0, 2, 0
0, 1, 1, 0
2, 0, 0, 1
Explanation of the last line: This customer bought 2 "Type A" family passes and 1 extra child ticket.
GUI Requirements
Your window must be titled "Pool Revenue Simulator" and contain the following components:

Price Entry Fields: Three input areas where the user can set the simulation prices (which must default to the values from the previous programming task) for:
Family Pass Price (applies to both Type A and Type B)
Adult Ticket Price
Child Ticket Price
Calculate Button: A button labeled "Calculate Revenue".
Result Area: A label to display the total calculated revenue formatted as currency (e.g., $1,250.00).
Status/Messages: A way to alert the user of errors (either a status label at the bottom or a pop-up Message Box).
Functional Requirements
When the user clicks the "Calculate Revenue" button, the program must:

Validate User Input: Ensure the prices entered in the GUI are valid non-negative numbers. If not, inform the user with a helpful error message.
Read the File: Attempt to open sales.txt.
If the file does not exist, display a "File Not Found" error.
Process Data:
Read the file line by line.
Parse the four comma-separated numbers.
Calculate the cost for that transaction using the prices currently entered in the GUI.
Sum the total of all transactions.
Display Result: Update the result label with the final total.
'''

import tkinter as tk;
from tkinter import ttk;

root = tk.Tk()
root.title("Pool Revenue Simulator")

root.mainloop()
