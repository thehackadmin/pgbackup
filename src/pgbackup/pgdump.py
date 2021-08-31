import subprocess
from sys import exit

def dump(dburl):
    try:
        return subprocess.Popen(['pg_dump', dburl], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"ERROR:  {err}")
        exit(1)

