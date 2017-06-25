OMP_NUM_THREADS=8 python ./train.py --model_path ./models/all505055 --train ../final_data/train.final.featured --dev ../final_data/dev.final.featured --test ../final_data/test.final --pre_emb /home/yuchen/useful_data/glove.twitter.27B.50d.txt --word_dim 50 --word_lstmn_dim 50 --zeros 1 --pos_dim 5 --dep_dim 0 --ind_dim 5 --head_dim 5 --lr_method adam
# test data will not be used 
