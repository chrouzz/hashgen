import hashlib
import base64
import itertools

mode = 2  

if mode == 1:

	s1 = b"KzkZxdhRGxB7eX4u1skXkfJ7VB8JfPp7Nfos3jiF7PQUNMh2SHDE" #private key 0.1BTC
	s2 = b"U2FsdGVkX19Q3I//VCH0U3cVtITZ3ckILJnUcdPX3Gs5qjdF1UjZ3mAftGivtFYDN5ZCSkBynnVqBawl4p8wKO0O8zI6D0A1+VEVCUyEvEeNoUfGcS0El9d93vsPxbg7D5avufQsScgsk3QEtq9/M4Do32OKFeq00/3NrxWOsMmh3AXmDzuuZ0qmZaI7re16FcXIrmPPiQDOHRc7wt0ng6qLiNz7VqESRTdxPOahKFRkWT8sT+Ur2y+2iZ2LEaxNM7UZqcPwYgm6FoKOVjnqdeg30R27jc6AoFPyRZ2g8+EJMp3n/pf94oSCLEWkc0osjH9DqbM6DUptu3HJbAVwXQ==" #base64 data
	s3 = b"U2FsdGVkX1+WPMJQISUVUvGRg7p4zCX4jIODIGb6b6cAreXFxv0WOxgCeSw9K+imTHiWMkRq45FsPXHs3TjYqcJz7QzQ8HeM340EwWQWXAi0fVy+r6NPmiJRgMgMqLCu4Q9o/WkNyHxvPScNgG9jf8gskggx10FiTcoyF1KE+nxjmRkEuj7uQQsPrrlRP3sjll4KXhAzrGQZi5E4sajQOBGQfaJjei5fHXXO6sxeYsFcuxzo3JdMOF3JFYQtuUDY==" # unzipped base64 data

	form_data = [s1, s2, s3]

	hash_test = list(itertools.permutations(form_data))
elif mode == 2:
	s1 = b"cry buyer grain save vault sign lyrics rhythm music fury horror mansion" #seed text
	s2 = b"U2FsdGVkX19Q3I//VCH0U3cVtITZ3ckILJnUcdPX3Gs5qjdF1UjZ3mAftGivtFYDN5ZCSkBynnVqBawl4p8wKO0O8zI6D0A1+VEVCUyEvEeNoUfGcS0El9d93vsPxbg7D5avufQsScgsk3QEtq9/M4Do32OKFeq00/3NrxWOsMmh3AXmDzuuZ0qmZaI7re16FcXIrmPPiQDOHRc7wt0ng6qLiNz7VqESRTdxPOahKFRkWT8sT+Ur2y+2iZ2LEaxNM7UZqcPwYgm6FoKOVjnqdeg30R27jc6AoFPyRZ2g8+EJMp3n/pf94oSCLEWkc0osjH9DqbM6DUptu3HJbAVwXQ==" #base64 data
	s3 = b"U2FsdGVkX1+WPMJQISUVUvGRg7p4zCX4jIODIGb6b6cAreXFxv0WOxgCeSw9K+imTHiWMkRq45FsPXHs3TjYqcJz7QzQ8HeM340EwWQWXAi0fVy+r6NPmiJRgMgMqLCu4Q9o/WkNyHxvPScNgG9jf8gskggx10FiTcoyF1KE+nxjmRkEuj7uQQsPrrlRP3sjll4KXhAzrGQZi5E4sajQOBGQfaJjei5fHXXO6sxeYsFcuxzo3JdMOF3JFYQtuUDY==" # unzipped base64 data

	form_data = [s1, s2, s3]

	hash_test = list(itertools.permutations(form_data))


with open("hashlist.txt","w") as f:
	for x in hash_test:
		first = True
		withoutSpace = b""
		withSpace = b""
		for y in x:
			if first:
				first = False
				withoutSpace += y
				withSpace += y
			else:
				withoutSpace += y
				withSpace +=  b" "  + y
		print(withoutSpace)
		print("\n")
		print(withSpace)
		print("\n\n")
		f.write("without space\n")
		f.write(hashlib.sha256(withoutSpace).hexdigest() + "\n")
		f.write("with space\n")
		f.write(hashlib.sha256(withSpace).hexdigest() + "\n\n")


