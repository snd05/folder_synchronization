import sys
import hashlib
import shutil
import filecmp


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


def hash_check(file):
    # Arbitrary buffer size
    buf_size = 65536
    # initializing the sha256() method
    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            # reading the data = buf_size from the file and saving it in a variable
            data = f.read(buf_size)

            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

#choosing the source and destination paths
src = sys.argv[1]
dst = sys.argv[2]
# src_hash = hash_check(src)
# dst_hash = hash_check(dst)
# if src_hash == dst_hash:
#   print("Both files are the same")

# else:
#   shutil.copy(src,dst)
#using the filecmp module
dcmp = filecmp.dircmp(src, dst)

if not dcmp.diff_files and not dcmp.left_only and not dcmp.right_only:
    print("Both files have the same content")
else:
    print("Folders have different content")
