1. 用tagger-conll.py 代替 tagger.py，解决格式问题。
2. 下列命令用 ../data/split/test.conll.iob数据为输入，NER的结果存储在 zytest.txt 文件中。
./tagger-conll.py --model models/tag_scheme\=iob\,lower\=False\,zeros\=False\,char_dim\=25\,char_lstm_dim\=25\,char_bidirect\=True\,word_dim\=100\,word_lstm_dim\=100\,word_bidirect\=True\,pre_emb\=\,all_emb\=False\,cap_dim\=0\,crf\=True\,dropout\=0.5\,lr_method\=sgd-lr_.005/ --input ../data/split/test.conll.iob --output zytest.txt
3. 在 evaluation/ 目录下使用 conlleval 脚本对 zytest.txt 进行测评。
 ./conlleval < ../zytest.txt > testresult.txt
 
