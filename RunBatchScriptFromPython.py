import time
import subprocess as sub

start_time = time.time()
print("ping google.com once in myBatchFile0.bat")
print ("start 1")
sub.call([r'C:\Users\ibike\Paul\RunBatchFromPython\myBatchFile0.bat'])
print("finish 1")
print("--- %s seconds ---" % (time.time() - start_time))

print()

start_time = time.time()
print("ping google.com twice in myBatchFile1.bat")
print ("start 2")
sub.call([r'C:\Users\ibike\Paul\RunBatchFromPython\myBatchFile1.bat'])
print("finish 2")
print("--- %s seconds ---" % (time.time() - start_time))

print()

start_time = time.time()
print("ping google.com thrice in myBatchFile2.bat")
print ("start 3")
sub.call([r'C:\Users\ibike\Paul\RunBatchFromPython\myBatchFile2.bat'])
print("finish 3")
print("--- %s seconds ---" % (time.time() - start_time))
