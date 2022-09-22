#!python
# -*- coding: utf-8 -*-
from ldap3 import Server, Connection, ALL

# server = Server('192.168.6.12')
# conn = Connection(server)
# conn.bind()
# print(conn)

loginuser = 'wachira'
loginpass = 'p1234'

# host = '192.168.6.12'
host = '172.16.1.3'
cnn = 'uid=' + loginuser + ',ou=people,dc=inno,dc=local'

try:
	# server = Server(host, get_info=ALL)
	server = Server(host, port = 636, use_ssl = True)
	conn = Connection(server, cnn, 'Innovisor123', auto_bind=True)
	# conn.search('ou=people,dc=inno,dc=local', '(uid=wachira)')
	conn.search('ou=people,dc=inno,dc=local', '(ou=people)')
	x = conn.entries
	print(x)
except:
	print("Invalid login")


