import math

TRAIN_SPLIT=0.7
NOTES_PER_LINE=20

clean = []
with open('bach-train-original.txt') as f:
	for line in f:
		for item in line.lstrip().rsplit():
			clean.append(item)

total_len = len(clean)
stop_index = math.floor(total_len*TRAIN_SPLIT)

with open('bach-train.txt', 'w') as f:
	count = 0
	for item in clean[:stop_index-1]:
		if count < NOTES_PER_LINE-1:
			f.write(item+' ')
			count+=1
		else:
			f.write(item+'\n')
			count = 0
			

with open('bach-valid.txt', 'w') as f:
	count = 0
	for item in clean[stop_index:]:
		if count < NOTES_PER_LINE-1:
			f.write(item+' ')
			count+=1
		else:
			f.write(item+'\n')
			count = 0

clean = []
with open('bach-test-original.txt') as f:
	for line in f:
		for item in line.lstrip().rsplit():
			clean.append(item)

with open('bach-test.txt', 'w') as f:
	count = 0
	for item in clean:
		if count < NOTES_PER_LINE-1:
			f.write(item+' ')
			count+=1
		else:
			f.write(item+'\n')
			count = 0