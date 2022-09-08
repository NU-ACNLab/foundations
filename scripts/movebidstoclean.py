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
	dest_dir_behav ="/projects/b1108/studies/foundations/data/raw/neuroimaging/behavioral"

	#iterates through subject folders to grab the right files
	for subject in os.listdir(directory):
		#make directory in dest_dir for the new subject
		dest_sub_dir = dest_dir + "/" + subject
		os.mkdir(dest_sub_dir)
		sub_dir = source_dir + "/" + subject + "/ses-1" #define dest sub directory to iterate through files there
		print(sub_dir)

		for data_type in os.listdir(sub_dir):
			for file in os.listdir(sub_dir + "/" + data_type):
				#try except keeps script from erroring out
				try:
					#shutil.copyfile(file, dest_dir) #copies files from source to destination
					'''
					if(data_type == "func"):
						shutil.copyfile(file, dest_dir + "/" + subject + "/ses-1/" + "func") #copies files from source to destination
					elif(data_type == "anat"):
						shutil.copyfile(file, dest_dir + "/" + subject + "/ses-1/" + "func") 
					elif(data_type == "beh"):
						shutil.copyfile(file, dest_dir_behav + "/" + subject + "/ses-1/" + "func")

					'''
					print(file + " copy successful.\n") 
				except:
					print(file + " failed to copy.\n")



def mini_bid_mover(subject):
	#here we define where files are coming from and moving to 
	source_dir = "/projects/b1108/data/Georgia/foundations" 
	dest_dir = "/projects/b1108/studies/foundations/data/raw/neuroimaging/bids"
	dest_dir_behav ="/projects/b1108/studies/foundations/data/raw/neuroimaging/behavioral"


	#make directory in dest_dir for the new subject
	dest_sub_dir = dest_dir + "/" + subject
	os.mkdir(dest_sub_dir)
	sub_dir = source_dir + "/" + subject + "/ses-1" #define dest sub directory to iterate through files there
	print(sub_dir)

	for data_type in os.listdir(sub_dir):
		for file in os.listdir(sub_dir + "/" + data_type):
			#try except keeps script from erroring out
			try:
				#shutil.copyfile(file, dest_dir) #copies files from source to destination
				'''
				if(data_type == "func"):
					shutil.copyfile(file, dest_dir + "/" + subject + "/ses-1/" + "func") #copies files from source to destination
				elif(data_type == "anat"):
					shutil.copyfile(file, dest_dir + "/" + subject + "/ses-1/" + "func") 
				elif(data_type == "beh"):
					shutil.copyfile(file, dest_dir_behav + "/" + subject + "/ses-1/" + "func")

				'''
				print(file + " copy successful.\n") 
			except:
				print(file + " failed to copy.\n")	




def main():
	#bid_mover()
	mini_bid_mover("sub-f11202")



if __name__ == "__main__":
    main()

