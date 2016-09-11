# Email-account-password-reset-script-cPanel

At SupportSages we provide 24*7 hosting support and server monitoring.

We all know how to reset an email account password through cPanel. Yeah, navigate to cPanel >> Email Accounts and reset the password against the email account.

It is a bit time consuming, right? And what if you have only WHM Access?

Then you will have to select the account and drop into its cPanel account which adds an additional step and delay our time even more. What if we had a simple utility to reset email passwords through Command line. It would just get things done in a few seconds saving us a few minutes of our time *and the clients time ;)*.

The python script we present you here is does exactly that.  

The script can be executed as a cPanel user also to reset passwords of email accounts under his account. It is achieved through eliminating the use of cPanel API Calls, hence only a few modifications are required for the user level execution.

How To Use
-----------
  
  Run the file by using the command 
 -<br />python <filename>.py
 +<br />python filename.py
  
  A prompt to enter the email account will appear as follows 
  <br />Enter Email Account:
 
 A confirmation prompt will appear with the account detail and email address along with a new password prompt
 <br />Account: example 
 <br />Domain: example.com 
 <br />Enter new Email Password:
 
 <br />Enter the new password in the prompt.
 
 A success message will be printed in case of a successful password change.
 
 
Sample output
-------------
 
 <br />Enter Email Account:example@example.com
 <br />EmailAccount: example@example.com 
 <br />Account: example 
 <br />Domain: example.com 
 <br />Enter new Email Password:redred
 <br />-------------------------------------------------------------------
 <br />Password changed successfully to redred
