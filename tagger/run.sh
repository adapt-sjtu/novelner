#./train.py --train ../data/split/train.conll.iob --dev ../data/split/dev.conll.iob --test ../data/split/test.conll.iob
./train.py --train ../data/split/train.conll.iob --dev ../data/split/dev.conll.iob --test ../data/split/test.conll.iob --word_dim 25 --word_lstm_dim 25 --pre_emb /home/bill/hatespeech/embeddings/glove.twitter.27B.25d.txt
#./train.py --train ../data/split/train.conll.iob --dev ../data/split/dev.conll.iob --test ../data/split/test.conll.iob --pre_emb /home/bill/hatespeech/embeddings/glove.twitter.27B.100d.txt
