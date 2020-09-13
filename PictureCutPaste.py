import os
import string
import random
def pcp(pathToPostsFolder, pathOfDestination):	
	print("Cut Paste Started")
	os.chdir(pathToPostsFolder)
	path = pathOfDestination + str(random.choice(string.ascii_letters)) + str(random.choice(string.ascii_letters)) + str(random.choice(string.ascii_letters)) + '.jpg'
	os.rename('0.jpg', path)
	print("Cut and Pasted")

# if __name__ == "__main__":
# 	pcp()