#!/bin/bash
python3 train.py --config=./configs/model_Sep27_switchPos_gamma03_cap100_1.config  --gpu
python3 test.py --config=./configs/model_Sep27_switchPos_gamma03_cap100_1.config  --gpu
