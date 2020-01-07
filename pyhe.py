#! python3
import pyperclip
import re
# Create a regex for phone numbers
phoneRegex = re.compile(r"""
(((\d\d\d) | (\(\d\d\d\)))?    #area code optional
(\s|-)                       #first separator
\d\d\d                       #first 3 digits
-                            #Separator
\d\d\d\d                     #last 4 digits
(((ext(\.)?\s) | x)          #extensions word-part
(\d{2,5}))? )                 #extension number-part
""", re.VERBOSE)
# Create a regex for email adresses
emailRegex = re.compile(r"""
# some.-_thing@cos.com
[a-zA-Z0-0_.+]+ #name part
@               # @ symbol
[a-zA-Z0-9_.+]+ #domain name part
""", re.VERBOSE)
# Get the text off the clipboard
input("The program will now copy your clipboard. Press enter to continue...")
text = pyperclip.paste()
extractedphone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)
allphonenumbers = []
for phonenumber in extractedphone:
    allphonenumbers.append(phonenumber[0])
result = "\n".join(allphonenumbers) + "\n".join(extractedemail)

# Copy the extracted email/phone numbers
pyperclip.copy(result)
