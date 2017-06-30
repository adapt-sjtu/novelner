OMP_NUM_THREADS=10 python ./train.py --model_path ./models/conll0000 --train ~/datasets/conll2003/eng.train --dev ~/datasets/conll2003/eng.testa --test ~/datasets/conll2003/eng.testb --pre_emb /home/yuchen/useful_data/glove.twitter.27B.100d.txt --zeros 1 --pos_dim 0 --dep_dim 0 --ind_dim 0 --head_dim 0 --lr_method adam
# test data will not be used 
