# -*- coding: utf-8 -*-

import hashlib
import base64
import sys
import itertools
import requests   #add this module to directly send the request
import pprint

mode = 1  
separator_char = b" "  #what we use to separate the different data
myName = "chrouzz"
myEmail = "chrouzz@gmail.com"
pp = pprint.PrettyPrinter(indent=4)
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0',
	'Content-Type': 'application/x-www-form-urlencoded',
}

s = requests.Session()

if mode == 1:

	s1 = b"KzkZxdhRGxB7eX4u1skXkfJ7VB8JfPp7Nfos3jiF7PQUNMh2SHDE" #private key 0.1BTC
	s2 = b"U2FsdGVkX19Q3I//VCH0U3cVtITZ3ckILJnUcdPX3Gs5qjdF1UjZ3mAftGivtFYDN5ZCSkBynnVqBawl4p8wKO0O8zI6D0A1+VEVCUyEvEeNoUfGcS0El9d93vsPxbg7D5avufQsScgsk3QEtq9/M4Do32OKFeq00/3NrxWOsMmh3AXmDzuuZ0qmZaI7re16FcXIrmPPiQDOHRc7wt0ng6qLiNz7VqESRTdxPOahKFRkWT8sT+Ur2y+2iZ2LEaxNM7UZqcPwYgm6FoKOVjnqdeg30R27jc6AoFPyRZ2g8+EJMp3n/pf94oSCLEWkc0osjH9DqbM6DUptu3HJbAVwXQ==" #base64 data
	s3 = b"U2FsdGVkX1+WPMJQISUVUvGRg7p4zCX4jIODIGb6b6cAreXFxv0WOxgCeSw9K+imTHiWMkRq45FsPXHs3TjYqcJz7QzQ8HeM340EwWQWXAi0fVy+r6NPmiJRgMgMqLCu4Q9o/WkNyHxvPScNgG9jf8gskggx10FiTcoyF1KE+nxjmRkEuj7uQQsPrrlRP3sjll4KXhAzrGQZi5E4sajQOBGQfaJjei5fHXXO6sxeYsFcuxzo3JdMOF3JFYQtuUDY" # unzipped base64 data

	form_data = [s1, s2, s3]

elif mode == 2:
	s1 = b"cry buyer grain save vault sign lyrics rhythm music fury horror mansion" #seed text
	s2 = b"U2FsdGVkX19Q3I//VCH0U3cVtITZ3ckILJnUcdPX3Gs5qjdF1UjZ3mAftGivtFYDN5ZCSkBynnVqBawl4p8wKO0O8zI6D0A1+VEVCUyEvEeNoUfGcS0El9d93vsPxbg7D5avufQsScgsk3QEtq9/M4Do32OKFeq00/3NrxWOsMmh3AXmDzuuZ0qmZaI7re16FcXIrmPPiQDOHRc7wt0ng6qLiNz7VqESRTdxPOahKFRkWT8sT+Ur2y+2iZ2LEaxNM7UZqcPwYgm6FoKOVjnqdeg30R27jc6AoFPyRZ2g8+EJMp3n/pf94oSCLEWkc0osjH9DqbM6DUptu3HJbAVwXQ==" #base64 data
	s3 = b"U2FsdGVkX1+WPMJQISUVUvGRg7p4zCX4jIODIGb6b6cAreXFxv0WOxgCeSw9K+imTHiWMkRq45FsPXHs3TjYqcJz7QzQ8HeM340EwWQWXAi0fVy+r6NPmiJRgMgMqLCu4Q9o/WkNyHxvPScNgG9jf8gskggx10FiTcoyF1KE+nxjmRkEuj7uQQsPrrlRP3sjll4KXhAzrGQZi5E4sajQOBGQfaJjei5fHXXO6sxeYsFcuxzo3JdMOF3JFYQtuUDY" # unzipped base64 data

	form_data = [s1, s2, s3]

elif mode == 3:
	s1 = b"KzkZxdhRGxB7eX4u1skXkfJ7VB8JfPp7Nfos3jiF7PQUNMh2SHDE" #private key 0.1BTC
	s2 = b"37fad2f9db9b74dc8fd920685925c725ba41b88c4a5e0885bbc43d75fb369f81" #shasum256 challenge.enc
	s3 = b"798ffc7b55fc1c529d9f77ec5a88dcdc8a656c42cd0866815eae2266ef84f57b" # shasum256 challengezip.enc

	form_data = [s1, s2, s3]

# create a list of permutation of elements within  the form_data list  
#ex  [[s1, s2, s3], [s1, s3, s2], [s2, s1, s3]...........]

hash_test = list(itertools.permutations(form_data))

with open("hashlist.txt","w") as f:
	#take a list of permuted elements
	for x in hash_test:
		first = True
		withSeparator = b""
		#happen elements in one line
		for y in x:
			if first:
				first = False
				withSeparator += y
			else:
				withSeparator +=  separator_char  + y
		postdata = {
			"form-name" : myName,
			"form-email" : myEmail,
			"message" : hashlib.sha256(withSeparator).hexdigest()
		}

		q = s.post('https://bitcoinchallenge.codes/register-310/', headers=headers, data=postdata)
		print(q.status_code)
		print("\n")
		print(withSeparator)
		# dont find the error message is a win!!!!
		if(q.text.find("Your SHA256 hash is unknown to me. You've got more work to do") == -1):
			print("success with the hash:" + hashlib.sha256(withSeparator).hexdigest())
			f.write(hashlib.sha256(withSeparator).hexdigest() + "\n\n")
		else:
			print("failed")

		# sys.exit()


