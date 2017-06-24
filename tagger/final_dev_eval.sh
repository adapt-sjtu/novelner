./tagger-conll.py --model models/tag_scheme=iob,lower=False,zeros=True,char_dim=25,char_lstm_dim=25,char_bidirect=True,word_dim=100,word_lstm_dim=100,word_bidirect=True,pre_emb=glove.twitter.27B.100d.txt,all_emb=False,cap_dim=5,crf=True,dropout=0.5,lr_method=sgd-lr_.005/ --input ../final_data/dev.final --output transfertest.txt > /tmp/asd
python ../data/wnuteval.py < transfertest.txt > ./evaluation/transfertestresult.txt
cat ./evaluation/transfertestresult.txt
