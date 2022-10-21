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
def list_participants():
    work_dir = "/projects/b1108/data/Georgia/foundations/"
    for partic in os.listdir(work_dir):
        #checks to make sure it's a participant
        if(partic[0:5] == "sub-f"):
            try:
                wd = work_dir + "/" + partic + "/ses-1/"
                dest = "/projects/b1108/studies/foundations/data/raw/neuroimaging/bids/" + partic + "/ses-1/"
                shutil.copytree(wd, dest) 
            except:
                print("Unable to copy " + partic)


def main():   
    list_participants()


if __name__ == "__main__":
    main()