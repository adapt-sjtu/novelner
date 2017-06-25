THEANO_FLAGS='floatX=float32' python sequence_labeling.py --num_epochs 200 --batch_size 10 --num_units 200 --num_filters 30 \
 --learning_rate 0.01 --decay_rate 0.1 --schedule 50 100 150 --grad_clipping 5 --regular none --dropout recurrent --delta 1.0 \
 --train "../final_data/train.final.featured" --dev "../final_data/dev.final.featured" --test "../final_data/test.final" 
