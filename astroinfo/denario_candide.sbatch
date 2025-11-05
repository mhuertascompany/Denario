#!/bin/bash
#SBATCH --job-name=denario_desi_euclid
#SBATCH --output=/n03data/huertas/desi_euclid/denario.out
#SBATCH --error=/n03data/huertas/desi_euclid/denario.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --nodelist=n03
#SBATCH --cpus-per-task=4
#SBATCH --time=48:00:00
#SBATCH --gres=gpu:1


source ~/.bashrc
conda activate /n03data/huertas/envs/Denario_env

cd /n03data/huertas/python/Denario/astroinfo

python /n03data/huertas/python/Denario/astroinfo/denario_astropt_fastmode.py

