OMP_NUM_THREADS=30 python ./train.py --train ../data/final/train.2017.final --dev ../final_data/dev.final --test ../final_data/test.final --pre_emb /home/yuchen/useful_data/glove.twitter.27B.100d.txt --zeros 1 --cap_dim 5 --char_dim 25 --char_lstm_dim 25
# test data will not be used 
