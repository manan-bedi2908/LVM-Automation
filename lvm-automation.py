import os
import getpass

os.system("tput bold")
os.system("tput setaf 1")
print("\t\t\tLogical Volume Management")
os.system("tput setaf 7")

print("\t\t\t------------------------")

passwd = getpass.getpass("Enter the password: ")
apass = "mb"

if passwd != apass:
	print("Access Denied")
	exit()

print("Where you would like to perform your job(local/remote)?",end=' ')
location = input()
print(location)

if location == "remote":
	remoteIP = input("Enter the IP Address: ")

def lvm_automate():
	os.system("tput setaf 2")
	print("Displaying the Available Disks")
	os.system("fdisk -l")
	num = int(input("How many disks you want to combine into a single Volume Group:"))
	disks = []

	for i in range(num):
		disk = input(f"Enter the {i+1} disk name of which you would like to create a Physical Volume: ")
		disks.append(disk)
		try:
			os.system(f"pvcreate {disk}")
		except:
			print("Error Occured!! Could not create a Physical Volume!!")
		else:
			os.system("tput setaf 3")
			print("Successfully created The Physical Volume!!")

		os.system(f"pvdisplay {disk}")
	
	length = len(disks)
	print("Number of disks: ", length)

	vg_name = input("Enter the name of the Volume Group: ")
	try:
		os.system(f"vgcreate {vg_name} {disks[0]} {disks[1]}")
	except:
		print("Error Occurred!!")
	else:
		print("Successfully created Volume Group")

	lv_name = input("Enter the name of the Logical Volume: ")
	size = int(input("Enter the size of the Logical Volume: "))
	try:
		os.system(f"lvcreate --size {size} --name {lv_name} {vgname}")
	except:
		print("Error occurred!!")
	else:
		print("Successfully created the Logical Volume!!")
	
	os.system("tput setaf 2")
	print("Displaying the details of the Logical Volume")
	os.system(f"lvdisplay {vg_name}/{lv_name}")
	
	os.system("tput setaf 3")
	print("Formatting the  Logical Volume...")
	os.system(f"mkfs.ext4 /dev/{vg_name}/{lv_name}")
	
	dir_loc = input("Enter the Directory location which you want to mount with the Logical Volume: ")
	try:
		os.system(f"mount /dev/{vg_name}/{lv_name} {dir_loc}")
	except:
		print("Error occurred!!")
	else:
		os.system("tput setaf 2")
		print("Successfully mounted the Directory")

	print("Displaying information about the Disks...")
	os.system("df -h")

def lvm_extend():
	vg_name = input("Enter the name of the Volume Group: ")
	lv_name = input("Enter the name of the Logical Volume: ")
	size = int(input("Enter the size of the Logical Volume: "))
	try:
		os.system(f"lvextend --size {size} /dev/{vg_name}/{lv_name}")
	except:
		print("Error occurred!!")
	else:
		print("Size of Logical Volume Changed!!")
	
	print("Formatting the remaining portion of the Logical Memory...")
	try:
		os.system(f"resize2fs /dev/{vg_name}/{lv_name}")
	except:
		print("Error Occurred!!")
	else:
		print("Successfully formatted the remaining portion!!")

while True:
	
	print("1. Logical Volume Management")
	print("2. Extend Logical Volume")
	print("Enter Your Choice: ",end=' ')
	ch = input()

	if int(ch) == 1:
		lvm_automate()
	elif int(ch) == 2:
		lvm_extend()

	input("Enter to continue...")	
	os.system("clear")



