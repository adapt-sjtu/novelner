./tagger-conll.py --model models/all_5055_adam --input ../final_data/dev.final.featured.new --output transfertest.txt > /tmp/asd
python ../data/wnuteval.py < transfertest.txt > ./evaluation/transfertestresult.txt
cat ./evaluation/transfertestresult.txt
