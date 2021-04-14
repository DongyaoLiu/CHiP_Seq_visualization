import os
import shutil

location = "D:/Rproject/CHiP-Seq"
folders = os.listdir(location)
print(folders)
GSMfolders = []
for GSM in folders:
    if "GSM" in GSM:
        GSMfolders.append(GSM)
print(GSMfolders)
print(len(GSMfolders))

# os.mkdir("D:/Rproject/CHiP-Seq/bw")
for GSM in GSMfolders:
    files = os.listdir(f"D:/Rproject/CHiP-Seq/{GSM}")
    for file in files:
        if ".bw" in file:
            shutil.copyfile(f"D:/Rproject/CHiP-Seq/{GSM}/{file}", f"D:/Rproject/CHiP-Seq/bw/{file}")
