import os
from sklearn.model_selection import train_test_split

conll = open('wnut17train.conll', encoding='utf-8').read().split('\n\t\n')

train, devtest = train_test_split(conll, test_size=0.3)

dev, test = train_test_split(devtest, test_size=0.5)


with open('split/train.conll.iob', 'w', encoding='utf-8') as train_f, open('split/dev.conll.iob', 'w', encoding='utf-8') as dev_f, open('split/test.conll.iob', 'w', encoding='utf-8') as test_f:
	for line in train:
		train_f.write(line + '\n\t\n')
	for line in dev:
		dev_f.write(line + '\n\t\n')
	for line in test:
		test_f.write(line + '\n\t\n')

