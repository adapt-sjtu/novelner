OMP_NUM_THREADS=30 python ./train.py --model_path ./models/all5532 --train ../final_data/train.final.featured --dev ../final_data/dev.final.featured --test ../final_data/test.final --pre_emb /home/yuchen/useful_data/glove.twitter.27B.100d.txt --zeros 1 --pos_dim 5 --dep_dim 5 --ind_dim 3 --head_dim 3 --lr_method adam
# test data will not be used 
