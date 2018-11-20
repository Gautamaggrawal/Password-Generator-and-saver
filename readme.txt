This is PASSWORD GENERATOR and SAVER version 1.0.0
===================================================
This software helps in saving passwords in encrypted form(Md5) in database and help
in saving saved passwords.This software also comprises of Password generator which 
will generate passwords randomly based on your choices you choose.
Basically this software is a computer directiory for storing passwords for the ease 
of users in  a encrypted form.
In this software there are certain categories to save password example 
Computer passwords,e-banking,social account-Fb and many more.
This software require a master password to continue in your account.
If users doesnot have it he can create his username and password.

Documentation
-------------
The main i.e 'password generator and saver'screen has 3 buttons and 2 entries ie 'USERNAME' & 'PASSWORD'
Buttons on mains screen:
1)LOGIN
2)ABOUT
3)CREATE ACCOUNT
----------------
1.lOGIN bUTTON:After adding registered username and password it will take user to its main account
2.ABOUT bUTTON:It shows the message box displaying the information about the software.
3.cREATEaCCOUNT bUTTON:This button will take you to other tk() window.Its helps in user registration.Any field can't be empty.If empty it willshow a warning message box.It has only 1 button i.e CREATE
If user is already registered and tring to register it will show a error box

Second Tk() window:WELCOME
--------------------------
It has 4 buttons i.e 
1)Categories
2)My Account
3)Show Saved
4)Password Generator
---------------------
1.Categories bUTTON:It will take you to next tk() window, before displaying the next window it will popup a                      dialog box that will ask your username for verification. 
                    After username verification it will open categories window which will have 7 radio buttons.
                    every radio button will popup next window for saving different categories passwords and                     usernames.

2.MyAccount bUTTON:It will ask the user to reset the saved data.It will MyAccount window which will have only                    one button that will ask user to RESET his saved passwords.

3.Showsaved bUTTON:It will view all the saved passwords and username of different categories(if any).it will                       popup a dialog box that will ask your username for verification.After username verification                     it will open categories window which will have 7 radio buttons.every radio button will popup                    next window that will show your saved  passwords and usernames.


4.PasswordGenerator bUTTON:
---------------------------
It will take you to next window for generating random passwords based on your choice.
Password generator window:
It will have 3 buttons:
1.back:-to go back to previous window

2.Generate password:-To generate passwords based on the password length user has given and differnt selected check boxes.If any entry is kept empty it will show warning message box.

3.Create:-it will pop the message box(if all entries are filled)'password successfully created'   



Default Libriaries used:
Tkinter
uuid
hashlib
shelve
random
string
subprocess


   