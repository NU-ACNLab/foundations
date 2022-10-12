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
    files = glob.glob(participant + "--FMAP2--GR--?_ph*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_phase2." + parts[1]
        os.rename(file, new_name) 
    files = glob.glob(participant + "--FMAP1--GR--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_magnitude1" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "--FMAP2--GR--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_magnitude2" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "--MID1--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-mid_run-01_bold" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "--MID2--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-mid_run-02_bold" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "REST1--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-rest_run-01_bold" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "--REST2--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-rest_run-02_bold" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "--REST3--EP_RM--11*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "__ses-1_task-rest_run-03_bold" + parts[1]
        os.rename(file, new_name)
    files = glob.glob(participant + "--REST4--EP_RM--*")
    for file in files:
        parts = file.split(".")
        new_name = participant + "_ses-1_task-rest_run-04_bold" + parts[1]
        os.rename(file, new_name)
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

 







