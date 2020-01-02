#!/bin/bash

mkdir -p /mnt/test

mount -t ntfs family.ntfs /mnt/test

getfattr --only-values -n user.FILE0 /mnt/test/Users/Family/Documents/credentials.txt > cred.png

umount /mnt/test

rm -rf /mnt/test
