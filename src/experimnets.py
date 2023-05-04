import os

os.system(
    f'python3 main.py --workingDir=epochs_no_mut --decay=0.7'
)
os.system(
    f'python3 main.py --workingDir=epochs_random --random_mutation --decay=0.7'
)
os.system(
    f'python3 main.py --workingDir=epochs_invert --invert_mutation --decay=0.7'
)
os.system(
    f'python3 main.py --workingDir=epochs_both --random_mutation --invert_mutation --decay=0.7'
)

decays = [1.0]


for decay in decays:
    os.system(
        f'python3 main.py --workingDir=epochs_{str(int(decay * 100))} --random_mutation --invert_mutation --decay={decay}'
    )
