# -*- coding: utf-8 -*-
#!/usr/bin/env python
####################################################
import os
import subprocess
import logging
#####################################################
#logging at /var/log/emailpassreset.log
#####################################################
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/log/emailpassreset.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
#########change as True to disable logging##########
logger.disabled = False
####################################################
#Check if there is root privilage
####################################################
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
####################################################
#Check if host is running a cPanelserver
####################################################
FNULL = open(os.devnull, 'w')
try:
	subprocess.check_call(["/usr/local/cpanel/cpanel", "-V"], stdout=FNULL, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError:
	exit("Server is not running cPanel.\n Exiting.")
####################################################
#Split Account Details
####################################################
def print_account():
    account, domain = EmailAccount.split("@")
    print ("Account: %s " % account)
    print ("Domain: %s " % domain)
####################################################
#Check if Email Account entered is of valid format
####################################################
def check_email_validity():
    split_build_descriptor = EmailAccount.split("@")
    if len(split_build_descriptor) == 2:
        print_account() #calling function
    else:
        print ("Email Address invalid. Try entering the complete email account. Eg: example@example.com")
        logger.error("Email Address invalid")
        exit()    
######################################################
#Check if domain, mail directory and shadow file exists
#and update the password
######################################################    
def check_domain_exists():
    import os
    import os.path
    import crypt
    import random
    import string
    account, domain = EmailAccount.split("@")
    check_userdomain = False
    userdom = os.path.join(os.sep, 'etc', 'userdomains')
    domain1 = open(userdom, "r")
    for line in domain1:
	  if line.startswith(domain):
	       check_userdomain =  line
	  else:
	       pass
    if check_userdomain:
        logger.info("Account exists in userdomains")
        username1 = check_userdomain.split (":")[1].strip()
	homedir = os.path.join(os.sep, 'etc','passwd')
	for line in open(homedir):
 		if username1 in line:
	 		homedir1 = line.split (":")[5].strip()
        maildir = os.path.join(os.sep, homedir1, 'mail', domain, account)
        if os.path.exists(maildir):
            logger.info("Mail directory exists =%s" % maildir)
            shadowpath = os.path.join(os.sep, homedir1, 'etc', domain, 'shadow')
	    showentry = False
	    for line in open(shadowpath):
 		if account in line:
	 		old_hash = line.split (":")[1].strip()
			showentry = True
		else:
			pass
            if showentry:
                passwd = raw_input("Enter new Email Password:")
                saltvalue = '$1$' + ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(8)])
                new_hash = crypt.crypt(passwd, saltvalue)
                s=open(shadowpath).read()
                if old_hash in s:
                    print"-------------------------------------------------------------------"
                    s=s.replace(old_hash, new_hash)
                    f=open(shadowpath, 'w')
                    f.write(s)
                    print "Password changed successfully to %s" % passwd
                    logger.info("Password changed successfully")
                    f.flush()
                    f.close()
                else:
                    print 'No occurances of "{old_string}" found.'.format(**locals())
                    logger.error("No occurances of shadow entry found.Try again")
                    exit()
            else:
                print "Error: Shadow entry not found"
                logger.error("Error: Shadow entry not found")
                exit()
        else:
            print "Error: Mail Directory not found"
            logger.error("Error: Mail Directory not found")
            exit()
    else:
        print 'The entered domain does not exist in this server'
        logger.error("The entered domain does not exist in this server")
        exit()
###################################################
#Script
###################################################
EmailAccount = raw_input("Enter Email Account:")
print ("EmailAccount: %s " % EmailAccount)
logger.info("Email Account to reset password: %s " %EmailAccount)
check_email_validity()
check_domain_exists()
