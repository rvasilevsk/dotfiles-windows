import sys
import pyperclip


# в винде10 не работало
# echo something | clip
# хз почему


def chomp(x):
    if x.endswith("\r\n"):
        return x[:-2]
    if x.endswith("\n") or x.endswith("\r"):
        return x[:-1]
    return x


text = ''
try:
    text = sys.stdin.read()
    text = chomp(text)
except KeyboardInterrupt:
    pass

s = 'clip << %r' % text
if text:
    print(s)
    pyperclip.copy(text)
else:
    print('usage: echo something | clip_from_stdin.py')

# spam = pyperclip.paste()
