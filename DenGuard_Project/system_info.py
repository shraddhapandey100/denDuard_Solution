# importing the library
import os
import psutil
import platform
import subprocess
from pathlib import Path
from memory_profiler import profile





#-----------------------******Module Functions Start From Here******-----------------------------------

#1)------------------------Basic Informantion About System-------------------------

def basic():
	print(f"Computer network name: {platform.node()}")
	print()
	#Machine type
	print(f"Machine type: {platform.machine()}")
	print()
	#Processor type
	print(f"Processor type: {platform.processor()}")
	print()
	#Platform type
	print(f"Platform type: {platform.platform()}")
	print()
	#Operating system
	print(f"Operating system: {platform.system()}")
	print()
	#Operating system release
	print(f"Operating system release: {platform.release()}")
	print()
	#Operating system version
	print(f"Operating system version: {platform.version()}")
	print()

	#Physical cores
	print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
	print()
	#Logical cores
	print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
	print()

	#Current frequency
	print(f"Current CPU frequency: {psutil.cpu_freq().current}")
	print()
	#Min frequency
	print(f"Min CPU frequency: {psutil.cpu_freq().min}")
	print()
	#Max frequency
	print(f"Max CPU frequency: {psutil.cpu_freq().max}")
	print()

	#System-wide CPU utilization
	print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
	print()
	#System-wide per-CPU utilization
	print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}")
	print()
	#Total RAM
	print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
	#Available RAM
	print()
	print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
	#Used RAM
	print()
	print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
	#RAM usage
	print()
	print(f"RAM usage: {psutil.virtual_memory().percent}%")
	print()




#2)-------------------------------Organizing the Junk Files-----------------


DIRECTORIES = {
	"HTML": [".html5", ".html", ".htm", ".xhtml"],
	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
			".heif", ".psd"],
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			".qt", ".mpg", ".mpeg", ".3gp"],
	"DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
				"pptx"],
	"ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
				".dmg", ".rar", ".xar", ".zip"],
	"AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
	"PLAINTEXT": [".txt", ".in", ".out"],
	"PDF": [".pdf"],
	"PYTHON": [".py"],
	"XML": [".xml"],
	"EXE": [".exe"],
	"SHELL": [".sh"]

}

FILE_FORMATS = {file_format: directory
				for directory, file_formats in DIRECTORIES.items()
				for file_format in file_formats}

def organize_junk():
	for entry in os.scandir():
		if entry.is_dir():
			continue
		file_path = Path(entry)
		file_format = file_path.suffix.lower()
		if file_format in FILE_FORMATS:
			directory_path = Path(FILE_FORMATS[file_format])
			directory_path.mkdir(exist_ok=True)
			file_path.rename(directory_path.joinpath(file_path))

		for dir in os.scandir():
			try:
				os.rmdir(dir)
			except:
				pass
	print()




#3)-----------------------Get list of running processes-------------------------

# traverse the software list
def list():
	Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
	a = str(Data)
	# try block
	# arrange the string
	try:
		for i in range(len(a)):
			print(a.split("\\r\\r\\n")[i])
	except IndexError as e:
		print("All Done")






	

