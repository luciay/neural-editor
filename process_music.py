import math

TRAIN_SPLIT=0.7
NOTES_PER_LINE=20

# set the type of data being ingested
TYPE='mono'

SAVE_PATH='midi_split/'+TYPE+'/'
OPEN_PATH='data_input_tokens/' +TYPE+'/'
COMPOSER = ['bach', 'mozart', 'beethoven', 'brahms', 'schubert', 'haydn', 'handel', 'vivaldi']

for c in COMPOSER:

	clean = []
	with open(OPEN_PATH+c+'-train.txt') as f:
		for line in f:
			for item in line.lstrip().rsplit():
				clean.append(item)

	total_len = len(clean)
	stop_index = math.floor(total_len*TRAIN_SPLIT)

	with open(SAVE_PATH+c+'/train.txt', 'w') as f:
		count = 0
		for item in clean[:stop_index-1]:
			if count < NOTES_PER_LINE-1:
				f.write(item+' ')
				count+=1
			else:
				f.write(item+'\n')
				count = 0

	with open(SAVE_PATH+c+'/valid.txt', 'w') as f:
		count = 0
		for item in clean[stop_index:]:
			if count < NOTES_PER_LINE-1:
				f.write(item+' ')
				count+=1
			else:
				f.write(item+'\n')
				count = 0

	clean = []
	with open(OPEN_PATH+c+'-test.txt') as f:
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