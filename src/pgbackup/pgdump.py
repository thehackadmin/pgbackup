import subprocess
from sys import exit

def dump(dburl):
    try:
        return subprocess.Popen(['pg_dump', dburl], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"ERROR:  {err}")
        exit(1)
def dump_filename(dburl, timestamp=None):
    dbname = dburl.split("/")[-1]
    dbname = dbname.split("?")[0]
    if timestamp:
        return f"{dbname}-{timestamp}.sql"
    else:
        return f"{dbname}.sql"
