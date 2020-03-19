import sys
import subprocess


def dump(url):
    try:
        return subprocess.Popen(['pgdump', url], stdout=subprocess.PIPE)
    except OSError as error:
        print(f'Error: {error}')
        sys.exit(1)
