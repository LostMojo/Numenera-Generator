#! python3
# ability_formatter.py - formats ability description from clipboard into python dictionary pastable text
# breaks either at : or before the () and removes the : afterward,
# copies it all back into the clipboard, strips /r/n for windows
# helpful for Numenera Data Entry

import pyperclip

text = pyperclip.paste()
text = text.replace('\r\n', ' ')

text = '"' + '": \n"'.join(text.split(': ')) + '"'

print(text)
pyperclip.copy(text)
