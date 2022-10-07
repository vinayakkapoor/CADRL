#!/bin/bash
python3 test.py --config=./configs/model_Sep30_p05_gamma05_cap10000_batch_1000_2.config --gpu
python3 test.py --config=./configs/model_Sep30_p07_gamma05_cap10000_batch_1000_2.config --gpu
python3 test.py --config=./configs/model_Sep30_p09_gamma05_cap10000_batch_1000_2.config --gpu