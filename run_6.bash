#!/bin/bash
python3 train.py --config=./configs/model_Sep27_switchPos_gamma04_cap100_2.config  --gpu
python3 test.py --config=./configs/model_Sep27_switchPos_gamma04_cap100_2.config  --gpu
