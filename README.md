python main.py --model pidinet --config carv4 --sa --dil --resume --iter-size 24 -j 4 --epochs 20 --lr 0.005 --lr-type multistep --lr-steps 10-16 --wd 1e-4 --savedir checkpoints/table5_pidinet --datadir training_data/BSDS500 --dataset BSDS --gpu 0
