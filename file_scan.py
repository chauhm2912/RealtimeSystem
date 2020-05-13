import time

start_time = time.time()

file = open('pg100.txt', "r")
wordcount = {}
for word in file.read().split():
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

for key in wordcount.keys():
	print(key, '', wordcount[key])

end_time = time.time()

print()
print((end_time - start_time)*1000, "ms")

file.close()
