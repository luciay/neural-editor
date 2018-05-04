import math

TRAIN_SPLIT=0.7
NOTES_PER_LINE=20
COMPOSER = 'vivaldi'

clean = []
with open('data_input_composer/'+COMPOSER+'-train.txt') as f:
	for line in f:
		for item in line.lstrip().rsplit():
			clean.append(item)

total_len = len(clean)
stop_index = math.floor(total_len*TRAIN_SPLIT)

with open('midi_split/'+COMPOSER+'/train.txt', 'w') as f:
	count = 0
	for item in clean[:stop_index-1]:
		if count < NOTES_PER_LINE-1:
			f.write(item+' ')
			count+=1
		else:
			f.write(item+'\n')
			count = 0
			

with open('midi_split/'+COMPOSER+'/valid.txt', 'w') as f:
	count = 0
	for item in clean[stop_index:]:
		if count < NOTES_PER_LINE-1:
			f.write(item+' ')
			count+=1
		else:
			f.write(item+'\n')
			count = 0

clean = []
with open('data_input_composer/'+COMPOSER+'-test.txt') as f:
	for line in f:
		for item in line.lstrip().rsplit():
			clean.append(item)

with open('midi_split/'+COMPOSER+'/test.txt', 'w') as f:
	count = 0
	for item in clean:
		if count < NOTES_PER_LINE-1:
			f.write(item+' ')
			count+=1
		else:
			f.write(item+'\n')
			count = 0