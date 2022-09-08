"""filemover.py: Copies bids files. Is called by slurm script"""

__author__      = "Katharina Seitz"
__date__   = "9/8/22"

import os
import shutil


'''
    Copies bids files from old Georgia directories to new /studies/foundations data format

            Parameters:
                    a: file_path, allows us to use the same code to move anat, dwi, and func data over. 

            Returns:
                    none
'''
def bid_mover():
	#here we define where files are coming from and moving to 
	source_dir = "/projects/b1108/data/Georgia/foundations" 
	dest_dir = "/projects/b1108/studies/foundations/data/raw/neuroimaging/bids"

	#iterates through subject folders to grab the right files
	for subject in os.listdir(directory):
		#make directory in dest_dir for the new subject
		dest_sub_dir = "/projects/b1108/studies/foundations/data/raw/neuroimaging/bids" + 
				"/" + "subject"
		os.mkdir(dest_sub_dir)
		sub_dir = source_dir + "/" + subject #define dest sub directory to iterate through files there
		print(sub_dir)

		for file in os.listdir(sub_dir):
			#try except keeps script from erroring out
			try:
				#shutil.copyfile(file, dest_dir) #copies files from source to destination
				print(file + " copy successful.\n") 
			except:
				print(file + " failed to copy.\n")


def main():
	bid_mover()



if __name__ == "__main__":
    main()

