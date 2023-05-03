import os

tree_depth = [3, 5, 7, 9, 11]

for depth in tree_depth:
    os.system(
        f'python3 main.py --workingDir=epochs_{depth} --random_mutation --invert_mutation --decay=0.7 --tree_depth={depth}'
    )
