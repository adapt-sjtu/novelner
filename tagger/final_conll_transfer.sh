OMP_NUM_THREADS=10 python ./train.py --model_path ./models/conll_5055_adam --train ../final_data/train.final.featured.all --test ../final_data/test.final --dev ../final_data/dev.final.featured.new --pre_emb /home/yuchen/useful_data/glove.twitter.27B.100d.txt --zeros 1 --pos_dim 5 --dep_dim 0 --ind_dim 5 --head_dim 5 --lr_method adam
# test data will not be used 
