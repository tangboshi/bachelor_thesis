import subprocess

def linecount(loc):
    for i in range(1,repetitions+1):
        linecount = subprocess.run(['wc', '-l', loc], stdout=subprocess.PIPE)
        linecount = linecount.stdout.decode('utf-8')
        linecount = linecount.partition(" ")[0]
        linecount = int(linecount)
        return linecount
