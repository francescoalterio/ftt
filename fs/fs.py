import sys

from fs.actions.create_file import create_file
from fs.actions.create_dir import create_dir
from fs.actions.delete_dir import delete_dir
from fs.actions.delete_file import delete_file
from fs.actions.rename import rename
from fs.actions.delete_all_dir import delete_all_dir

def fs():
    action = sys.argv[2]
    name = sys.argv[3]

    if action == 'cf': create_file(name)
    elif action == 'cd': create_dir(name)
    elif action == 'dd': delete_dir(name)
    elif action == 'df': delete_file(name)
    elif action == 'rn': rename(name, sys.argv[4])
    elif action == 'dad': delete_all_dir(name)
    