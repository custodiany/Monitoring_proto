import paramiko
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect('10.14.61.1', port=22, username='root', password='cua001')

print("<Cpu_avg>")
stdin, stdout, stderr = cli.exec_command("sar -u 1 1 | awk '/Average/ { cpu = 100 - $8 } END {print cpu }'")
lines = stdout.readlines()
print(''.join(lines))

print("<Mem_avg>")
stdin, stdout, stderr = cli.exec_command("free -m | awk '/Mem/ { used_mem = $3 }; /Mem/ { cached_mem = $7 }; /Mem/ { total_mem = $2 }; /Mem/ { buffers_mem = $6 }; END { print (used_mem - cached_mem - buffers_mem)/total_mem * 100}'")
lines = stdout.readlines()
print(''.join(lines))

print("<File_system>")
stdin, stdout, stderr = cli.exec_command("df -h")
lines = stdout.readlines()
print(''.join(lines))

cli.close()
