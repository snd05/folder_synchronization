import sys
import shutil
import filecmp
import time


def count_arguments():
    # number of arguments
    n = len(sys.argv)
    if n != 5:
        print(
            "The number of arguments is not valid\nThe syntax is: python script.py source_folder destination_folder log_file_path sync_interval")
        sys.exit()
    print("Total arguments passed:", n)
    # name of the script
    print("\nName of the python script:", sys.argv[0])
    # arguments passed
    print("\nArguments passed:", end=" ")
    for i in range(1, n):
        print(sys.argv[i], end=" ")


# using the filecmp module
def compare_folders(src, dst):
    dcmp = filecmp.dircmp(src, dst)

    if not dcmp.diff_files and not dcmp.left_only and not dcmp.right_only:
        print("Both files have the same content")
    else:
        print("Replacing the content of the destination folder...")
        shutil.rmtree(dst)
        shutil.copytree(src, dst)


# choosing the source and destination paths
src = sys.argv[1]
dst = sys.argv[2]

# opening the log file
log_file_path = sys.argv[3]
log_file = open(log_file_path, "a")  # 'a' is for appending an existing file
# choosing the synchronization interval
sync_interval = int(sys.argv[4])
while True:
    # writing in the log file
    log_file.write("Checking the folder at the interval given...\n")
    # comparing the folders
    compare_folders(src, dst)

    log_file.flush()
    # waiting to check again
    time.sleep(sync_interval)
log_file.close()
