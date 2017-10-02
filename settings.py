import hashlib

# LTM server url
url = "https://ltm-admin.fundacja-medyczna.pl/P1"

# LTM user
user = "tomek"

# password (plain text)
passwd = "password" # put your password instead

# hashing
digest=hashlib.md5()
digest.update(passwd)

# md5 hash of the password
password=str(digest.hexdigest())
