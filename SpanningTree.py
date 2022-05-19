import telnetlib
import time

print('MES2428P-SFP-ONU')

ip_address = b'172.17.255.105'
login = b'admin\n'
password = b'admin\n'
sw_glob = b'MES2428P-SFP-ONU#'

#Login process:
telnet = telnetlib.Telnet(ip_address, 23, 5)
telnet.read_until(b'MES2428P-SFP-ONU login:')
telnet.write(login)
telnet.read_until(b'Password:')
telnet.write(password)
telnet.read_until(sw_glob)

try:
	print(' 1: Отключить Spanning-Tree\n 2: Включить Spanning-Tree\n 3: Выход')
	test_number = int(input())
	if test_number == 1:
		telnet.write(b'conf t\n')
		telnet.read_until(b'(config)#')
		telnet.write(b'interface range gig0/1-2\n')
		telnet.read_until(b'#')
		telnet.write(b'spanning-tree bpdufilter enable\n')
		telnet.read_until(b'#')
		telnet.write(b'exit\n')
		telnet.read_until(b'#')
		telnet.write(b'exit\n')
		telnet.read_until(b'#')
	elif test_number == 2:
		telnet.write(b'conf t\n')
		telnet.read_until(b'(config)#')
		telnet.write(b'interface range gig0/1-2\n')
		telnet.read_until(b'#')
		telnet.write(b'spanning-tree bpdufilter disable\n')
		telnet.read_until(b'#')
		telnet.write(b'exit\n')
		telnet.read_until(b'#')
		telnet.write(b'exit\n')
		telnet.read_until(b'#')
	elif test_number == 3:
		print('Bye')
	else:
		print('Такого значения в списке нет:')
except ValueError:
	print('Введенное значение не является числом')
finally:
	#telnet.write(b'clear line vty all\n')
	time.sleep(1)
	telnet.write(b'exit\n')
	time.sleep(1)
	telnet.close()
	print('Finish')
input()

