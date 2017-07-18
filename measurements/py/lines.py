import subprocess

def linecount(loc):
    linecount = subprocess.run(['wc', '-l', loc], stdout=subprocess.PIPE)
    linecount = linecount.stdout.decode('utf-8')
    linecount = linecount.partition(" ")[0]
    linecount = int(linecount)
    return linecount
