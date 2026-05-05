<h1 style="text-align: center;">Name: Ash Kuinkel</h1>

## Purpose/Summary : 
The purpose of this assingment is to solve the client's problem, i.e. Codetown Public Pool requires a GUI application that reads
a log of daily ticket sales from a file and calculates the total revenue based on prices entered by the user in the window which
helps them in acheiveing their goal of being able to review their sales performance.

## How to Run:
Let's dive into how this program can be run. 

The program has been packaged in the form of a tarball, preserving all the current files, directories including structures, file permissions etc.
This was done using the command:

```bash
tar -zc revenue.py sales.txt readme.md > pt2.tgz
```

where z - puts archive through gzip & c - creates archive

To load the archived directory, files etc., run the command:

```bash
tar -zxf pt2.tgz 
```
where z - puts archive through gzip, x - extracts from archive (into current directory) & f - refers to name of archive i.e. pt2.tgz


## How Proposed solution adheres to marking criteria/client requirements:
The marking criteria/client requirements of this problem specifically require us to acheive the GUI & Functional Requirements.

## GUI Requirements:
  - Price Entry Fields: Three input areas where the user can set the simulation prices (which must default to the values from the previous programming task) for:
      - Family Pass Price (applies to both Type A and Type B)
      - Adult Ticket Price
      - Child Ticket Price
    
  These requirements are most definitely met. The GUI produced, features the title "Pool Revenue Simulator" as required and does indeed feature 3 tkinter entry
  fields prompting the user to enter the price of the family pass, adult price and child price to their liking. In the event, the user does not set these prices,
  they default to the values from the previous assessment task, i.e. {Family Pass Price : $16.00, Adult Ticket Price : $5.00, Child Ticket Price : $4.00}

  - Calculate Button: A button labeled "Calculate Revenue".

  Indeed a button labeled exactly as required, "Calculate Revenue" is featured within the GUI. Tkinter features a button widget, which was simply implented and 
  placed under the input fields.

  - Result Area: A label to display the total calculated revenue formatted as currency (e.g., $1,250.00).

  The result area is implemented by using tkinter's label widget. In particular, we used a StringVar to dynamically update the result text after every successfull
  calculation. Note that an alternative way we could implement this was considered, i.e. we could create a new label every time we output the result text. However,
  this approach was not taken, because we would essientially be stacking the layers of labels on top of each other, worsening performance and doing extra unecessary
  work when we could infact we dynamically updating one label widget.

  - Status/Messages: A way to alert the user of errors (either a status label at the bottom or a pop-up Message Box).

  All errors within this programming task were displayed to the user in the form of a pop-up message box. This was done using the messagebox module within tkinter.

## Functional Requirements:
  - Validate User Input: Ensure the prices entered in the GUI are valid non-negative numbers. If not, inform the user with a helpful error message.

  This is met, we ensure that the prices that the user has entered in the GUI are valid non-negative numbers, if they are not, we use the messagebox module and raise
  an error to the user. Furthermore, we also ensure that we are only performing calculations for the total revenue when the given input is valid. This is implemented
  through the use of a boolean variable which in the event of an error gets set to true and the calculation is guarded by an if condition to only run when the boolean
  variable is set to false. Furthermore, if user inputs non-numeric values a ValueError is raised in the message box and the boolean value is also set to True, preventing
  the calculations from running.

  - Read the File: Attempt to open sales.txt.
      - If the file does not exist, display a "File Not Found" error.

  This requirement is followed perfectly. We must read the sales.txt file for the program to output any results. Hence in the event that the file does not exist we
  simply use tkinter's messagebox module and implement it inside a FileNotFoundError inside a try, except statement. This ensures that if the sales.txt file is not
  present, we return an error and do not perform any further calculations.

  - Process Data:
    - Read the file line by line.
    - Parse the four comma-separated numbers.
    - Calculate the cost for that transaction using the prices currently entered in the GUI.
    - Sum the total of all transactions.

  This process outlined is indeed followed by my solution to the problem.


Let's dive through how each of the following requirements listed have been accomplished through my proposed solution. 


## References:
- https://www.w3schools.com/python/python_args_kwargs.asp
- https://www.w3schools.com/python/ref_string_split.asp
- https://www.geeksforgeeks.org/python/break-list-chunks-size-n-python/
- https://www.geeksforgeeks.org/python/ternary-operator-in-python/
- 
...
