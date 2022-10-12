# -*- coding: utf-8 -*-
import os 


directory = "/projects/b1108/data/Georgia/foundations/sub-f10792_TESTKAT/ses-1"
participant = "f10792"

def rename_partic(): 
    files = glob.glob(participant + "--FMAP1--GR--?_ph*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_phase1." + parts[1]
        os.rename(file, new_name) 

    #rename t1000--FMAP2--GR--6_ph sub-t1000_ses-1_phase2 *
    files = glob.glob(participant + "--FMAP2--GR--?_ph*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_phase2." + parts[1]
        os.rename(file, new_name) 
      
    #rename t1000--FMAP1--GR--5 sub-t1000_ses-1_magnitude1 * 
    files = glob.glob(participant + "--FMAP1--GR--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_magnitude1" + parts[1]
        os.rename(file, new_name)

    #rename t1000—-FMAP2--GR--6 sub-t1000_ses-1_magnitude2 *  
    files = glob.glob(participant + "--FMAP2--GR--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_magnitude2" + parts[1]
        os.rename(file, new_name)

    #rename t1000--MID1--EP_RM--9 sub-t1000_ses-1_task-mid_run-01_bold *  
    files = glob.glob(participant + "--MID1--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-mid_run-01_bold" + parts[1]
        os.rename(file, new_name)

    #rename t1000--MID2--EP_RM--10 sub-t1000_ses-1_task-mid_run-02_bold *
    files = glob.glob(participant + "--MID2--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-mid_run-02_bold" + parts[1]
        os.rename(file, new_name)
      
    #rename t1000--REST1--EP_RM--7 sub-t1000_ses-1_task-rest_run-01_bold *
    files = glob.glob(participant + "REST1--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-rest_run-01_bold" + parts[1]
        os.rename(file, new_name)
          
    #rename t1000--REST2--EP_RM--8 sub-t1000_ses-1_task-rest_run-02_bold *
    files = glob.glob(participant + "--REST2--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-rest_run-02_bold" + parts[1]
        os.rename(file, new_name)
          
    #rename t1000--REST3--EP_RM--11 sub-t1000_ses-1_task-rest_run-03_bold * 
    files = glob.glob(participant + "--REST3--EP_RM--11*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "__ses-1_task-rest_run-03_bold" + parts[1]
        os.rename(file, new_name)

    #rename t1000--REST4--EP_RM--12 sub-t1000_ses-1_task-rest_run-04_bold * 
    files = glob.glob(participant + "--REST4--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-rest_run-04_bold" + parts[1]
        os.rename(file, new_name)


    #rename t1000--T1w--GR--4 sub-t1000_ses-1_T1w *  
    files = glob.glob(participant + "--T1w--GR--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_T1w" + parts[1]
        os.rename(file, new_name)


def main():
   try:
       rename_partic()
    except:
        print(participant + " FAILED and I AM MAD >:-(")

if __name__ == "__main__":
    main()

 







