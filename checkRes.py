print("Loading results for cache hierarchy from Sniper\n")
f = open("/mnt/B/sniper/test/gapbs/xywqr.log")

allTuples = []
for line in f:
	q=""
	for w in line:
		q=q+w
		if w == ')':
			allTuples.append(q)
			q=""

# print(len(allTuples))
dictMap={}
for t in allTuples:
	t = t[1:]
	t = t[:-1]
	t=t.split(',')
	tag=t[0]
	tag=tag[1:]
	tag=tag[:-1]
	t[0]=tag
	dictMap[tag]=t[2]
# print(dictMap)

metric = ["loads", "stores", "load-misses", "store-misses", "load-overlapping-misses",
"store-overlapping-misses", "loads-prefetch", "stores-prefetch", 
"hits-prefetch", "evict-prefetch", "invalidate-prefetch", "hits-warmup", "evict-warmup", "invalidate-warmup",
"prefetches", "coherency-downgrades", "coherency-upgrades", "coherency-invalidates", "coherency-writebacks"]

a_metric = ["loads","stores","load-misses",
	"stores-misses","stores-where","evict","backinval"]
a_tag = ["I","S","M","E","O","u","e","c"]

levels = ["L1-I", "L1-D", "L2", "L3"]
collect = []
allCollect = []

f = open("/mnt/B/sniper/test/gapbs/check.log", 'w')

mydict = {}

for i in range(len(metric)):
	line = metric[i]
	mydict[line]=" "

for i in range(len(a_metric)):
	for a in a_tag:
		line = a_metric[i] + "-" + a
		mydict[line]=" "



#cache levels
for i in range(len(levels)):
	level=levels[i]

	for m in metric:
		key = level+"."+m

		if key in dictMap:
			collect.append(dictMap[key])
			mydict[m]=mydict[m]+str(dictMap[key])+","
		else:
			mydict[m]="0,"
	
	for m in a_metric:
		key1 = level+"."+m

		for t in a_tag:
			key = key1 + "-" + t
			key2 = m+'-'+t

			if key in dictMap:
				collect.append(dictMap[key])
				mydict[key2]=mydict[key2]+str(dictMap[key])+","
			else:
				mydict[key2]="0,"

			key=key1

	allCollect.append(collect)
	collect = []

f = open("/mnt/B/sniper/test/gapbs/check.log", "w")

for k in mydict:
	f.write(k +","+ mydict[k] + '\n')