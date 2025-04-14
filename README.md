Introduction:
The Medicine Management System is a Python-based console application designed to manage the inventory of medicines in a pharmacy or medical store. It is a basic implementation of  operations (add, Update, Delete) using object-oriented programming concepts.
The main goal is to allow to:
Add new medicines
Update existing ones
Delete medicines by ID
View a single medicine
View all stored medicines

Project Structure:
➤ 1. medicine class: This class defines the blueprint of a medicine object with four key attributes:
id: Unique ID for the medicine (integer)
name: Name of the medicine (string)
manufacturer: Name of the manufacturing company (string)
price: Price of the medicine (integer or float)
It also includes a str() method to display a formatted string when the object is printed.



➤ 2. medicineopration class: This class handles all the core logic using a Python dictionary to store medicines. Each medicine is stored using its ID as a key, which allows fast and easy look-up.

It includes the following methods:
add(medicine): Adds a new medicine object
update(medicine): Updates an existing medicine by ID
delete(medicineid): Removes a medicine by ID
view(medicineid): Displays details of a specific medicine
getall(): Lists all medicines in the system



➤ 3. Main Menu: This file interacts with the user through a menu in a continuous loop. The user selects an operation by entering a choice from 1 to 6.

Technical Details:
Language:Python

Concepts Used:
Object-Oriented Programming (Classes, Objects)
Dictionary for storage
User input and loops
Conditional statements


Conclusion: This project successfully demonstrates how basic object-oriented programming concepts can be applied to build a real-life application. The Medicine Management System offers an efficient and easy-to-use interface to manage medicine inventories and provides a foundation for more advanced systems.
