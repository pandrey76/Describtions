# 1. Checking file exist, can be run from terminal.
$ [ -f db1.sqlite3 ] && echo "FILE exist." || echo "FILE does not exist."

# 2. Kill all python Django runserver process
$ ps -ef | grep '.*python3.*manage.py.*runserver.*' | grep -v grep | awk '{print $2}' | xargs -r kill -9
