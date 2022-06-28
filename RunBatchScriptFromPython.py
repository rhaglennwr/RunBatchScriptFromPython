import time
import subprocess as sub

start_time = time.time()
print("ping google.com once")
print ("start 1")
sub.call([r'C:\Users\ibike\Paul\RunBatchFromPython\myBatchFile0.bat'])
print("finish 1")
print("--- %s seconds ---" % (time.time() - start_time))

print()

start_time = time.time()
print("ping google.com twice")
print ("start 2")
sub.call([r'C:\Users\ibike\Paul\RunBatchFromPython\myBatchFile1.bat'])
print("finish 2")
print("--- %s seconds ---" % (time.time() - start_time))

print()

start_time = time.time()
print("ping google.com thrice")
print ("start 3")
sub.call([r'C:\Users\ibike\Paul\RunBatchFromPython\myBatchFile2.bat'])
print("finish 3")
print("--- %s seconds ---" % (time.time() - start_time))
