# -*- coding: utf-8 -*-
import os
import shutil

'''
    Copies foundations participants from /data/Georgia to /studies
            Parameters:
                    none
            Returns:
                    none
'''
def mover():
    work_dir = "/projects/b1108/data/Georgia/foundations/"
    for partic in os.listdir(work_dir):
        if(partic[0:5] == "sub-f"):
            wd = work_dir + "/" + partic + "/ses-1/"
            for folder in os.listdir(wd): 
             #checks to make sure it's a participant
                try:
                    source = wd + folder
                    if(folder == "beh"):
                        dest = "/projects/b1108/studies/foundations/data/raw/neuroimaging/behavioral/"\
                            + partic + "/ses-1/" + folder
                        shutil.copytree(source, dest) 
                        print("Copied " + partic + " " + folder)
                    else:
                        dest = "/projects/b1108/studies/foundations/data/raw/neuroimaging/bids/"\
                             + partic + "/ses-1/" + folder
                        shutil.copytree(source, dest) 
                        print("Copied " + partic + " " + folder)
                except:
                    print("Unable to copy " + partic)


def main():   
    mover()


if __name__ == "__main__":
    main()