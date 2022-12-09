from subprocess import run, PIPE, CalledProcessError
import shlex

cmd = "netstat -n"

cmd_words = shlex.split(cmd)

try:
    process = run(cmd_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
else:
    stdout = process.stdout.decode()
    stderr = process.stderr.decode()

    lines = stdout.splitlines()
    for line in lines:
        if 'ESTABLISHED' in line:
            proto, recq, sendq, local, remote, status = line.split()
            if proto == 'tcp4':
                print(local, remote)

