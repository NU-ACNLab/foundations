#!/usr/bin/bash
#
#SBATCH -A p31833
#SBATCH -p short
#SBATCH -t 04:00:00
#SBATCH --mem=20G
#SBATCH -J mriqc-hf
#SBATCH	--mail-type=END,FAIL
#SBATCH	--mail-user=katharina.seitz@northwestern.edu

module purge
module load singularity/latest
echo "modules loaded"
cd /projects/b1108

singularity run --cleanenv -B /projects/b1108:/projects/b1108/ /projects/b1108/software/singularity_images/mriqc-latest.simg -v /projects/b1108/studies/foundations/data/raw/neuroimaging/bids/derivatives -v /projects/b1108/studies/foundations/data/processed/neuroimaging/mriqc participant --participant-label ${1}
# change above to --clean-workdir so that the work directory is cleared and you save space
