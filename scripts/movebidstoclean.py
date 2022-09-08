"""filemover.py: Copies bids files. Is called by slurm script"""

__author__      = "Katharina Seitz"
__date__   = "9/8/22"

import os
import shutil


'''
    Iterates through the study folder to create a list of participants

            Parameters:
                    None. 

            Returns:
                    a: a list of participants
'''
def subj_iterator():
	#intiliaze list of participants 
	participants = []
	source_dir = "/projects/b1108/data/Georgia/foundations" 
	#iterates through subject folders to grab the particpants
	for subject in os.listdir(source_dir):
		#make directory in dest_dir for the new subject
		participants.append(subject)
	return(participants)
		


'''
    Copies a single particpant's bids files from old Georgia directories to new 
    /studies/foundations data format. Behavioural data goes into behavioral folder, rather than
    bids

            Parameters:
                    a: subject

            Returns:
                    none
'''
def subj_mover(subject):
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
					shutil.copyfile(file, dest_dir + "/" + subject + "/ses-1/" + "anat") 
				elif(data_type == "beh"):
					shutil.copyfile(file, dest_dir_behav + "/" + subject + "/ses-1/" + "behavioral")

				'''
				print(file + " copy successful.\n") 
			except:
				print(file + " failed to copy.\n")	




def main():
	partic_list = subj_iterator()
	for partic in partic_list:
		subj_mover(partic)
		print(partic)



if __name__ == "__main__":
    main()

