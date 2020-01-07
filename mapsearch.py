import webbrowser
import sys
import pyperclip

sys.argv

if len(sys.argv) > 1:
    searchquery = " ".join(sys.argv[1:])
else:
    searchquery = pyperclip.paste
webbrowser.open("https://www.google.com/maps/place/" + searchquery)
