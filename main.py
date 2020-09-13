from selenium import webdriver
import time
import Renamer
import PictureCutPaste as pcp
import os
import winsound

recipient = "Sarim" # Change this name to the name you want to send message.

botDirectory = "D:\\WebWhatsAppBot"
chromedriver = os.path.join(botDirectory, 'chromedriver.exe')
linkToPost = 'D:\\Posts\\0.jpg'
person = f'//*[@title="{recipient}"]'
pathToPostsFolder = 'D:\\Posts'
pathOfDestination = 'D:\\DonePosts\\'


options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=" + botDirectory)
navigator = webdriver.Chrome(executable_path=chromedriver, options=options)

def playsound():
	winsound.PlaySound("1.wav", winsound.SND_ASYNC)
	time.sleep(5)

def upload():
	
	print("Getting the web page")	
	navigator.get("https://web.whatsapp.com/")
	time.sleep(10)
	print("Got it...!!!")
	
	per = True

	while per:
		
		try:
			
			group = navigator.find_element_by_xpath(person).click()
		except Exception as e:
			print(e)
			print("Connect your phone to Internet..")
			playsound()
			
			navigator.refresh()
			time.sleep(15)
		else:
			print("Posting to", recipient)
			time.sleep(1)
			clip_button = navigator.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div').click()
			# //*[@id="main"]/footer/div[1]/div[1]/div[2]/div
			# time.sleep(5)
			photo_icon = navigator.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/span/div/div/ul/li[1]/button/input')
			# //*[@id="main"]/footer/div[1]/div[1]/div[2]/span/div/div/ul/li[1]/button
			# //*[@id="main"]/footer/div[1]/div[1]/div[2]/span/div/div/ul/li[1]/button/span
			# input Xpath: //*[@id="main"]/footer/div[1]/div[1]/div[2]/span/div/div/ul/li[1]/button/input
			time.sleep(2)
			photo_icon.send_keys(linkToPost)

			time.sleep(11)

			submit_button = navigator.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()

			time.sleep(20)
			print('Posted...')

			navigator.close()
			navigator.quit()
			pcp.pcp(pathToPostsFolder, pathOfDestination)
			time.sleep(2)
			Renamer.Rename(pathToPostsFolder)
			time.sleep(1)
			per = False
			
if __name__ == '__main__':
	upload()
