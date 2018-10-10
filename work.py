# base64 string from line 310 alpha channel which decodes to openssl salted data
# donations to: 1Fnv5AjLoZiCQCypVwPFjW2pimS9TgZ5xZ

import base64



with open("challengezip.enc","wb") as f:
	f.write(base64.b64decode("U2FsdGVkX1+WPMJQISUVUvGRg7p4zCX4jIODIGb6b6cAreXFxv0WOxgCeSw9K+imTHiWMkRq45FsPXHs3TjYqcJz7QzQ8HeM340EwWQWXAi0fVy+r6NPmiJRgMgMqLCu4Q9o/WkNyHxvPScNgG9jf8gskggx10FiTcoyF1KE+nxjmRkEuj7uQQsPrrlRP3sjll4KXhAzrGQZi5E4sajQOBGQfaJjei5fHXXO6sxeYsFcuxzo3JdMOF3JFYQtuUDY=="))
