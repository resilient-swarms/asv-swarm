# Data processing
import numpy as np 
import subprocess
import os
import sys

# This file should be run as:
# python3 simulate wave_height wave_heading rand_seed

# Extract the command line args
wave_ht = sys.argv[1]
wave_heading = sys.argv[2]
rand = sys.argv[3]

# build directory
build_dir = "./build"
build_dir_threading_disabled = build_dir + "/threading_disabled"
build_dir_threading_with_sync = build_dir + "/threading_with_sync"
build_dir_threading_without_sync = build_dir + "/threading_without_sync"

# simulator app
app_threading_disabled = build_dir_threading_disabled + "/asv_simulator"
app_threading_with_sync = build_dir_threading_with_sync + "/asv_simulator"
app_threading_without_sync = build_dir_threading_without_sync + "/asv_simulator"

# input file
input_file = "../asv"

# Create the output dir
out_dir = "./asv_out"
os.mkdir(out_dir)

# number of trials
trials = range(10)

# simulate each trial one after the other.
time_file_name = out_dir + "/time_threading_disabled"
time_file = open(time_file_name, "w")
print("threading_disabled")
for trial in trials:
	print("trial - " + str(trial))
	#out_file = out_dir + "/asv_out_" + str(trial)
	out_file = "/dev/null"
	ps = subprocess.run([app_threading_disabled, input_file, out_file, str(wave_ht), str(wave_heading), str(rand)], stdout=time_file)

time_file_name = out_dir + "/time_threading_with_sync"
time_file = open(time_file_name, "w")
print("threading_with_sync")
for trial in trials:
	print("trial - " + str(trial))
	#out_file = out_dir + "/asv_out_" + str(trial)
	out_file = "/dev/null"
	ps = subprocess.run([app_threading_with_sync, input_file, out_file, str(wave_ht), str(wave_heading), str(rand)], stdout=time_file)

time_file_name = out_dir + "/time_threading_without_sync"
time_file = open(time_file_name, "w")
print("threading_without_sync")
for trial in trials:
	print("trial - " + str(trial))
	#out_file = out_dir + "/asv_out_" + str(trial)
	out_file = "/dev/null"
	ps = subprocess.run([app_threading_without_sync, input_file, out_file, str(wave_ht), str(wave_heading), str(rand)], stdout=time_file)

