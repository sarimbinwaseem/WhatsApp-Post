import os
	
def Rename(pathToPostsFolder):
	print("Renaming....")
	
	os.chdir(pathToPostsFolder)
	files = os.listdir()
	# print(files)

	name = "0.jpg"

	if name in files:
		pass
	else:
		print(files[-1])
		os.rename(files[-1], name)
	print("Done")
# if __name__ == "__main__":
# 	Rename()

