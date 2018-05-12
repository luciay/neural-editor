import math
import random

# TRAIN_SPLIT=0.8
NOTES_PER_LINE=20

# set the type of data being ingested
TYPE='mono'
# TYPE='poly'

OPEN_PATH='multi-model-musical-phrase-completion/train-test/'
SAVE_PATH='luciay-neural/neural-editor/midi_split/'+TYPE+'/'
COMPOSER = ['bach', 'mozart', 'beethoven', 'brahms', 'schubert', 'haydn', 'handel', 'vivaldi']


for c in COMPOSER:

	# clean = []
	# with open(OPEN_PATH+c+'_mono_train.txt') as f:
	# 	for line in f:
	# 		for item in line.lstrip().rsplit():
	# 			clean.append(item)


	# with open(SAVE_PATH+c+'/temp.txt', 'w') as f:
	# 	count = 0
	# 	for item in clean:
	# 		if count < NOTES_PER_LINE-1:
	# 			f.write(item+' ')
	# 			count+=1
	# 		else:
	# 			f.write(item+'\n')
	# 			count = 0

	# with open(SAVE_PATH+c+'/train.txt', 'w') as t:
	# 	with open(SAVE_PATH+c+'/valid.txt', 'w') as v:
	# 		with open(SAVE_PATH+c+'/temp.txt') as f:
	# 			for line in f:
	# 				r = random.randint(0, 4)
	# 				if r == 1:
	# 					v.write(line)
	# 				else:
	# 					t.write(line)

	# with open(SAVE_PATH+c+'/train.txt', 'w') as f:
	# 	count = 0
	# 	for item in clean[:stop_index-1]:
	# 		if count < NOTES_PER_LINE-1:
	# 			f.write(item+' ')
	# 			count+=1
	# 		else:
	# 			f.write(item+'\n')
	# 			count = 0

	# with open(SAVE_PATH+c+'/valid.txt', 'w') as f:
	# 	count = 0
	# 	for item in clean[stop_index:]:
	# 		if count < NOTES_PER_LINE-1:
	# 			f.write(item+' ')
	# 			count+=1
	# 		else:
	# 			f.write(item+'\n')
	# 			count = 0

	clean = []
	with open(OPEN_PATH+c+'_'+TYPE+'_test.txt') as f:
		for line in f:
			for item in line.lstrip().rsplit():
				clean.append(item)

	with open(SAVE_PATH+c+'/test.txt', 'w') as f:
		count = 0
		for item in clean:
			if count < NOTES_PER_LINE-1:
				f.write(item+' ')
				count+=1
			else:
				f.write(item+'\n')
				count = 0