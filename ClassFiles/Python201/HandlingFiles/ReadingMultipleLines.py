# with open('Emails.txt', 'r') as emails:
    # print(emails.readlines())  # ['email1@gmail.com\n', 'email2@gmail.com\n', 'pgoldfarm@gmail.com\n', 'pgoldfarm@yahoo.com\n', 'email3@hotmail.com\n', 'email4@gmail.com\n']  ********This is a list.



# with open('Emails.txt', 'r') as emails:
#     emails = emails.readlines()
    
# for email in emails:
#     print("Looking for a hotmail account")
#     if "hotmail" in email:
#         print(email)  # Looking for a hotmail account
#                       # Looking for a hotmail account
#                       # Looking for a hotmail account
#                       # Looking for a hotmail account
#                       # Looking for a hotmail account
#                       # email3@hotmail.com



# with open('Emails.txt', 'r') as emails:
#     emails = emails.readlines()
    
# for email in emails:
#     if "gmail" in email:
#         print(email)  # email1@gmail.com

#                       # email2@gmail.com

#                       # pgoldfarm@gmail.com

#                       # email4@gmail.co



# Removing empty lines
with open('Emails.txt', 'r') as emails:
    emails = emails.readlines()
    
for email in emails:
    if "gmail" in email:
        print(email.rstrip())   # email1@gmail.com
                                # email2@gmail.com
                                # pgoldfarm@gmail.com
                                # email4@gmail.com
                                

