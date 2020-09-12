import os
import pyperclip


cwd = os.getcwd()
text = 'cd /d "%s"' % cwd
s = "clipboard << " + text
pyperclip.copy(text)
print(s)
