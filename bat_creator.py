# в винде10 не работало
# echo something | clip
# хз почему
# поэтому сделал clip_from_stdin.py


cmd_lines = '''
wh = where %*

gist git status
giaa git add --all %*
gicm git commit -m %*
gidi git diff %*
gip git push

cdd cd /d %*
cd1 cd ..
cd2 cd ../..
cd3 cd ../../..

mdcd mkdir "%*" & cd /d "%*"


cc echo %* | clip_from_stdin.py

py27 c:\\bin\\python27-32\\python.exe %*
py33 c:\\bin\\python33-64\\python.exe %*
py37 c:\\bin\\python37-32\\python.exe %*
py38 c:\\bin\\python38-32\\python.exe %*
py3864 c:\\bin\\python38-64\\python.exe %*

pipupip python -m pip install --upgrade pip
pipf python -m pip freeze
pipi python -m pip install %*
pipu python -m pip install --upgrade %*
pipun python -m pip uninstall %*
act .\\venv\\Scripts\\activate.bat
deact .\\venv\\Scripts\\deactivate.bat
new_venv python3 -m venv venv
fl8 flake8

ll ls -l %*

ff far .

scls scoop list
scs scoop search %*
scinf scoop info %*
sci scoop install %*
scu scoop update *
sccl scoop cleanup *

all scoop update * & scoop cleanup * & rustup update

ytdl youtube-dl %*

st "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
stt "C:\\Program Files\\Sublime Text 3\\sublime_text.exe" .

ddd @python3 -c "import datetime; s = datetime.datetime.now().strftime('%%Y-%%m-%%d'); print(s)"
mmm @python3 -c "import datetime; s = datetime.datetime.now().strftime('%%H:%%M:%%S'); print(s)"
cddd ddd | clip_from_stdin.py
cmmm mmm | clip_from_stdin.py
'''


dir_lines = '''
SyncD d:\\documents-beh\\0-beh-lora-android-d-versioning
BehPy d:\\documents-beh\\0-beh-lora-android-d-versioning\\dev\\behpy
DotFilesWindows d:\\documents-beh\\0-beh-lora-android-d-versioning\\dotfiles-windows
'''


def text_to_lines(text):
    r"""
    :param text: str
    :return: abc.Generator[str]
    >>> text = ''' some \n text \n # comment\ntext2'''
    >>> list(text_to_lines(text))
    ['some', 'text', 'text2']
    """
    seq = (ln.strip() for ln in text.strip().splitlines())
    seq = (ln for ln in seq if ln and ln[0] != '#')
    return seq


def write_cmd_file(name, content):
    name = 'cmd\\'+name+'.cmd'
    print(name, '<<', repr(content), end='...')
    try:
        with open(name, 'w', encoding='utf8') as f:
            f.write(content)
        print('ok')
    except Exception as e:
        print(e)


def main_cmd():
    for ln in text_to_lines(cmd_lines):
        name, content = ln.split(' ', 1)
        write_cmd_file(name, content)


def main_dirs():
    for ln in text_to_lines(dir_lines):
        name, content = ln.split(' ', 1)
        name = 'cd'+name
        content = r'@cd /d "%s"' % content
        write_cmd_file(name, content)


if __name__ == '__main__':
    main_cmd()
    print()
    main_dirs()
