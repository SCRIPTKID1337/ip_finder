import socket as s
host = input ("type the name of website :- ")
print (f'ip of {host} is {s.gethostbyname(host)}')
input ()
