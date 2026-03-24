import subprocess

# shell=False, the command is executed directly without using the shell, which is safer and more efficient. When shell=False, the command should be a list of arguments rather than a string.
command = ["ls", "-l"]

sp = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

rt = sp.wait() # wait for the process to finish and return the exit code, succeed with exit code 0, fail with non-zero exit code

out, err = sp.communicate() # read the output and error streams of the process, and wait for it to finish if it hasn't already

print(out)
print(err)


# shell = True, the command is executed through the shell, which allows you to use shell features like environment variables, pipes, etc. However, it can be a security hazard if you're using untrusted input in the command string, as it can lead to shell injection vulnerabilities. When shell=True, the command should be a string rather than a list.
command_ = "echo $SHELL"
sp = subprocess.Popen(command_, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)