import subprocess
import re

def create_file(filename):
	subprocess.run(['touch', filename])

def give_permissions(filename):
	subprocess.run(['chmod', '777', filename])

def check_internet_connection():
	# can we connect to the internet?
	return subprocess.run(['ping', '-c', '2', 'google.com'])

def get_ip_info():
	# get network information with "ifconfig" command and save them in a file
	# net-tools lib should be installed with atp for using ifconfig
	ifconfig_out = subprocess.check_output(['ifconfig']).decode('utf-8')
	info = re.findall(r'inet [0-9].+', ifconfig_out)
	splitted_info = re.split(r'[\W]+', info[0])
	print('info:', splitted_info)
	return splitted_info

def write_ip_info(info):
	ip = info[1] + '.' + info[2] + '.' + info[3] + '.' + info[4]
	write_ip = 'echo "ip: ' + ip + '" > lan_info.txt'
	subprocess.run(write_ip, shell=True)
	netmask = info[6] + '.' + info[7] + '.' + info[8] + '.' + info[9]
	write_netmask = 'echo "netmask: ' + netmask + '" >> lan_info.txt'
	subprocess.run(write_netmask, shell=True)
	return [info[1], info[2], info[3], info[4], info[6], info[7], info[8], info[9]]

def bin_to_dec(binary):
	decimal = 0
	i = 0
	while binary != 0:
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary // 10
		i += 1
	return(decimal)

def dec_to_bin(decimal):
	binary = 0
	mult = 1
	while decimal > 0:
		binary += (decimal % 2) * mult
		mult *= 10
		decimal = decimal // 2
	return(binary)

def size_of(n):
	i = 0
	while n > 0:
		i += 1
		n = n // 10
	return i

def write_network_ip(info):
	# 1. calculate network address starting from our ip and netmask
	# 2. how many devices can be connected to the network?
	#file_text = subprocess.check_output(['cat', '...'])
	
	ip_bin = ''
	for count in range(1, 4):
		n_bin = dec_to_bin(int(info[count]))
		print('size_of:')
		print(size_of(n_bin))
		if size_of(n_bin) < 8:
			print('size_of:')
			print(size_of(n_bin))
			
			ip_bin += dec_to_bin(int(info[count]))
			ip_bin += dec_to_bin(int(info[count]))

	'''netmask_bin = ''
	for  count in range(6, 9):
		netmask_bin[i] = dec_to_bin(int(info[count + 5]))

	network_dec = []
	for count in range(0, 3):
		network_dec = bin_to_dec(network_bin[count])

	network = str(network_dec[0]) + '.' + str(network_dec[1]) + '.' + str(network_dec[2]) + '.' + str(network_dec[3])
	write_netmask = 'echo "network: ' + network + '" >> lan_info.txt'
	subprocess.run(write_netmask, shell=True)'''

def hops_to_site(site):
	# write in a file how many hops to go to the given site
	file_text = subprocess.check_output(['traceroute', site]).decode('utf-8')
	print(file_text)

def main():
	create_file('lan_info.txt')
	give_permissions('lan_info.txt')
	if (check_internet_connection()):
		print('I can connect to the internet! :D')
	else:
		print('I can\'t connect to the internet! :(')
	info = get_ip_info()
	write_ip_info(info)
	write_network_ip(info)
	#hops_to_site('google.it')

if __name__ == '__main__':
	main()
