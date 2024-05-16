#!/usr/bin/python3

import yt_dlp
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	clear()

	userSelectedOutputType = ''
	links = ''
	ytdlpArguments = {
		'outtmpl': '%(title)s.%(ext)s'
	}

	print("\nWhat type of output do you want?\n")
	print("1) Audio only")
	print("2) Video only")
	print("3) Video and audio")
	try:
		userSelectedOutputType = int(input("\nMake a selection: "))
		if userSelectedOutputType not in (1, 2, 3):
			raise ValueError	
	except ValueError:
		print('\nThe input you provided was invalid, please ensure that you supply\nonly one of the valid numbers listed above\n')
		input('Press [ENTER] to continue: ')
		main()


	if userSelectedOutputType == "1":
		ytdlpArguments += {
			'format': 'bestaudio',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
			}]
		}

	elif userSelectedOutputType == "2":
		ytdlpArguments += {
			'format': 'bestvideo'
		}

	elif userSelectedOutputType == "3":
		ytdlpArguments += {
			'format': 'bv+ba/b'
		}
		

	clear()

	if len(links) == 0:
		links = input("\n[Input all links seperating each with a space]\n==============================================\n").split()

	clear()

	print("\n[Queued For Download]\n=====================\n")
	for link in links:
		print(link)

	userContinueResponse = input("\nDo you want to continue? (Y/n): ") or "Y"

	while True:
		match userContinueResponse.lower():
			case "n":
				exit()
			case "y":
				os.chdir(os.path.expanduser("~") + "/Downloads")
				try:
					os.mkdir("YT-DLP Output")
				except:
					pass
				os.chdir("YT-DLP Output")
				clear()
				with yt_dlp.YoutubeDL(ytdlpArguments) as ytdlp:
					ytdlp.download(links)
					clear()
					print(f"\nDownload finished. You can find them here: {os.path.expanduser("~") + "/Downloads/YT-DLP Output"}")
					break
			case _:
				print('\nThe input you provided was invalid, please ensure that you supply\nonly "Y" or "N"\n')
				input('Press [ENTER] to continue: ')

if __name__ == '__main__':
    main()
