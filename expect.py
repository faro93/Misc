#!/usr/bin/python3
#code utf-8

import sys
import pexpect
import time
import re
import passepass

# cnx = 'ssh -l <user> <ip>'
ip = '10.5.3.245'
user = 'murdesconfs'
password = passepass.getpass(user, '172.19.28.26')
cmdes = [
    'ssh -l <user> <ip>',
    'show registration sipd by-realm * extended to-file <file>',
    'show directory /opt'
]
promptShell = r'.*\# '
prmoptPasswd = r'^.*password:\s+$'

cmde = cmdes[0]
if '<user>' in cmde:
    cmde = cmde.replace('<user>', user)
if '<ip>' in cmde:
    cmde = cmde.replace('<ip>', ip)

child = pexpect.spawn(cmde, timeout=5)
child.expect(prmoptPasswd)
child.sendline(password)
child.expect(promptShell)

myDate = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
hostname = "PVTST062"

for cmde in cmdes[1:]:
    if '<file>' in cmde:
        cmde = cmde.replace('<file>', f'{hostname}.{myDate}.REG.by.realm.ext.txt')
   
    child.sendline(cmde)
    child.expect(promptShell)

    for line in enumerate(child.after.decode("ISO-8859-1", "strict").split('\r\n')):
        if line[0] == len(child.after.decode("ISO-8859-1", "strict").split('\r\n'))-1:
            print(f'{line[1]}', end='')
        else:
            print(f'{line[1]}')

child.close()
