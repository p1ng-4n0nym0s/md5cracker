import hashlib
import terminal_banner
import pyfiglet
ascii_banner = pyfiglet.figlet_format("MD5 Cracker !!")
print(ascii_banner)
banner_txt = "=========================================Enter your option==========================================\n1:Encode or 2:Decode\n\nThis is simple tools for encodind and decoding MD5 hashes \n\n\t\t\t\t\t\t\t\twritten by : p1ng_4n0nym0u5"
print(terminal_banner.Banner(banner_txt))
words = ""
choice  = int(input("\n"))
if (choice == 1):
    word =raw_input("Enter the message to be hashed:")
    hash = hashlib.md5(word.encode('utf-8'))
    print("MD5 hash for "+words+"is "+hash.hexdigest())
elif (choice == 2):
    flag =0
    pass_hash = raw_input("Enter your hash :")
    
    try:
    	pass_file = open('wordlist.txt', 'r')
    except:
    	print("No file found !!!")
    	exit(1)

    for word in pass_file:
    	enc_word = word.encode('utf-8')
    	digest = hashlib.md5(enc_word.strip()).hexdigest()

        print(word)
        print(digest)

    	if digest == pass_hash:
    		print("Password Found")
    		print("password is "+ word)
    		flag = 1
    		break
    if flag == 0:
    	print("Password not found in the database !!")

else:
	print("Invalid input")
