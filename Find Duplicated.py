## My First Program
# remove Duplicated ptf Files

import os
import hashlib
import send2trash

# def get_hash():
# compare it
# and send duplicated files to trash

direct = os.walk(r'D:\Software\msayd')
lists = []


def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


for folders, subfolders, filenames in direct:
    for filename in filenames:
        if filename.endswith('.ptf'):

            file = os.path.join(folders, filename)
            filehash = hashfile(file)
            if filehash not in lists:
                lists.append(filehash)
            else:
                send2trash.send2trash(file)
                # os.remove(file)

                ## Done