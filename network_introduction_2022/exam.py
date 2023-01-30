import subprocess

def create_file(filename):
	subprocess.run(['touch', filename])

def give_read_permissions():
	subprocess.run(['sudo', 'chmod', '666', '/path/to/file'])

def check_internet_connection():
	# can we connect to the internet?
	return subprocess.run(['ping', '-c', '2', 'google.com'])

def get_ip_info():
	# get network information with "ifconfig" command and save them in a file
	# net-tools lib should be installed with atp for using ifconfig
	subprocess.run(['ifconfig', '...'])

def find_network_ip():
	# 1. calculate network address starting from our ip and netmask
	# 2. how many devices can be connected to the network?
	file_text = subprocess.check_output(['cat', '...'])
	...

def main():
	create_file('')
	give_read_permissions('filename')
	if (check_internet_connection()):
		print('I can connect to the internet! :D')
	else:
		print('I can\'t connect to the internet! :(')
	get_ip_info()
	find_network_ip()

if __name__ == '__main__':
	main()
