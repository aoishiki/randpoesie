# coding=utf-8
import random
import sys

args = sys.argv
if len(args) < 2 :
	print("put number")
else :
	samplenum = int(args[1])
	for line in open('word.txt', 'r') :
		wordList = line[:-1].split(',')
	listlen = len(wordList)

	if samplenum > listlen :
		print("引数は",listlen,"以下にしてください")
	else :
		sampleWords = random.sample(wordList,samplenum)
		for word in sampleWords :
			print(word)