import subprocess
import re

def create_file(filename):
	subprocess.run(['touch', filename])

def give_permissions(filename):
	subprocess.run(['chmod', '777', 'ciao'])

def check_internet_connection():
	# can we connect to the internet?
	return subprocess.run(['ping', '-c', '2', 'google.com'])

def get_ip_info():
	# get network information with "ifconfig" command and save them in a file
	# net-tools lib should be installed with atp for using ifconfig
	lan_info = subprocess.check_output(['ifconfig']).decode('utf-8')
	inet = re.findall(r'inet [0-9].*', lan_info)
	print(inet)

def find_network_ip():
	# 1. calculate network address starting from our ip and netmask
	# 2. how many devices can be connected to the network?
	#file_text = subprocess.check_output(['cat', '...'])
	#...
	return

def hops_to_site(site):
	# write in a file how many hops to go to the given site
	file_text = subprocess.check_output(['traceroute', site]).decode('utf-8')
	print(file_text)
	
	#channels = re.findall(r'Channel [0-9]*', output)

def main():
	create_file('ciao')
	give_permissions('filename')
	if (check_internet_connection()):
		print('I can connect to the internet! :D')
	else:
		print('I can\'t connect to the internet! :(')
	get_ip_info()
	find_network_ip()
	hops_to_site('google.it')

if __name__ == '__main__':
	main()
