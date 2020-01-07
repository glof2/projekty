#! python3
# Libraries
import re
import pyperclip
import datetime
# Searching phrase
passemailRegex = re.compile(r".+@.+\..{1,3}:.+")
# Take text from clipboard
text = pyperclip.paste()
# Extract
result = passemailRegex.findall(text)
# Save Data
result = "".join(result)
currenttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
with open(currenttime + ".txt", "a") as f:
    f.write(result)
    print(f"Saved in {currenttime}.txt")
