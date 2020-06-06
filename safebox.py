from stdiomask import getpass
from os import path, system, mkdir
# Password
pwd = 'proto'

if path.exists('Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
	# Unlock
	if not getpass() == pwd:
		input('Wrong Password!')
		exit()
	system('attrib -h -s -r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
	system('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" HexBox')
	input('Unlocked!')
elif not path.exists('HexBox'):
	# Make Dir
	mkdir('HexBox')
	input('HexBox Created')
else:
	# Lock
	system('ren HexBox "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
	system('attrib +h +s +r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
	input('Locked!')