import sys
import shutil


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
src=sys.argv[1]
dst=sys.argv[2]
shutil.copytree(src,dst)