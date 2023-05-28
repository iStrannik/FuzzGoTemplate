#!/bin/bash

./simple_go_web/simple_go_web &

python3 main.py --workingDir=epochs --random_mutation --invert_mutation --decay=0.7 --generation=11 &

wait
