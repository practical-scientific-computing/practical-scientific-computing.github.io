---
title: Run Processing Pie Chart
layout: default
group: Python
type: example
---

# Run Processing Pie Chart

Let's say you have some data which you are processing, and at the end of the processing, you produce a file
RunXXXX.data. You know you have a large list of files which are being processed, and you'd like to make a
quick graph of what's done/what isn't. Let's use python/numpy to make a pie chart out of everything! Here's
the file progress.py:

```Python
#!/usr/python3
import sys,os,random#access to command line
import subprocess#run a process and get the output
"""
Make a pie chart of the progress of runs processed.
The assumption is that in some folder, you have the runs you have processed
and in the list given at the beginning of the file, these are the runs
you want to process. The code looks in the folder, determines all the files,
then makes a pie chart based on the amount done.
first, the run will cd into the folder "test", then touch a bunch of files
as an example. Next, we loop over all the files in the directory, and extract the
number from it. Then we compare to the total list.
"""


total2process = [2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2128, 2129, 2135, 2136, 2137, 2140, 2141, 2142,
                 2143, 2144, 2145, 2146, 2147, 2148, 2150, 2151, 2152, 2153, 2154, 2156, 2157, 2158, 2159, 2161, 2162, 2164, 2166,
                 2167, 2168, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2209, 2210, 2211,
                 2212, 2215, 2216, 2220, 2224, 2225, 2227, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2237, 2238, 2239, 2240, 2241,
                 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261,
                 2262, 2263, 2264, 2265, 2266, 2268, 2272, 2273, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2284, 2285, 2292, 2294,
                 2295, 2300, 2302, 2303, 2304, 2305, 2307, 2308, 2313, 2314, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324,
                 2325, 2326, 2327, 2328, 2329, 2330, 2332, 2333, 2334, 2335, 2338, 2340, 2341, 2344, 2345, 2346, 2347, 2348, 2349,
                 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2371,
                 2372, 2373, 2374, 2375, 2376, 2377, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2390, 2391, 2393, 2394,
                 2395, 2396, 2397, 2398, 2399, 2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2417, 2419,
                 2420, 2425, 2427, 2428, 2429, 2430, 2431, 2432, 2434, 2435, 2436, 2442, 2443, 2444, 2445, 2446, 2448, 2449, 2451, 2452]

runs2touch = []

#30 random runs
current_dir = os.getcwd()
for i in range(30):
    runs2touch.append(random.choice(total2process))

## don't try to overwrite a folder.
if not os.path.exists(current_dir+"/tmp"):
    print("making temp dir in current folder: %s"%(current_dir))
    os.mkdir(current_dir+"/tmp")
#make the fake dataruns.
print("touching runs %s"%runs2touch)

for run in runs2touch:
    subprocess.Popen(['touch','%s/tmp/Run%d.data'%(current_dir,run)])
                

##now look at all the files in that directory
list_done_proc = subprocess.Popen(['ls', '-1',current_dir+"/tmp/"], stdout=subprocess.PIPE)#only get the list from ls -1
list_done, err = list_done_proc.communicate()
list_of_files = list_done.strip().split('\n')
#now use collections to search for the list of files there.
processed=[]
for file in list_of_files:
    print file
    if not 'Run' in file:
        continue
    processed.append(float((file.split('Run')[1]).strip('.data')))
print(list_of_files)
print processed

import collections #use collections to take the intersection of two sets
a_multiset = collections.Counter(processed)

b_multiset = collections.Counter(total2process)
overlap = list((a_multiset & b_multiset).elements())
done_total = len(overlap)
total_total = len(total2process);
progress_total = float(done_total)/float(total_total)

vals_tot = [progress_total,1-progress_total]

#now make the numpy pie chart
from pylab import *
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])
explode=(0, 0)
labels=['Done', 'To Do']
pie(vals_tot,explode=explode,labels=labels,autopct='%1.1%%f',shadow=True,startangle=45)
title("Progress on Processing of Data",bbox={'facecolor':'0.8', 'pad':5})
show()

```

Now, copy this to the file progress.py, and simply run on the command line.

```
$ python progress.py
```
You should produce the following plot (reminder, not the same numbers).

![Progress Output](/python/media/progress_output.png "Progress Output")