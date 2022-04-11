import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames
file_name_list = glob.glob(pattern)
print(file_name_list)
for file_name in file_name_list:
    print(file_name)
# TODO: use os.path.getsize to find each file's size
for file_name in file_name_list:
    print(os.path.getsize(file_name))

# TODO: Add a test to only display files that are not zero length
for file_name in file_name_list:
    file_size = os.path.getsize(file_name)
    if file_size !=0:
        print(file_size, file_name)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
for file_name in file_name_list:
    print(os.path.basename(file_name))

