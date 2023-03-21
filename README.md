# MY FINAL PROJECT
My project is a simple to do list that let's users add to do lists and add days and time in their to do item. 

- What does it do?  
  It tells the user how many days are remaining for their item that they've added, when the item is due, and if the item is overdue.

- What is the "new feature" which you have implemented that we haven't seen before?  
 It uses datetime module that let's the user add their date and time. 

## Prerequisites
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)? 
List those here (if any).

## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - Module name: Datetime Module
- [x] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name: to-do-list.py
  - Line number(s): from line 6 to 29
  - Name of two properties: description, due_date
  - Name of two methods: list_name(self,name) and list_due_date(self)
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to a file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: to-do-list.py
  - Line number(s): Line 23  (if time_delta.days > 0:)
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name: to-do-list.py
  - Line number(s): Line 62 (for list in lists:)
- [x] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.