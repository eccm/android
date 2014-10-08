import os
import os.path
rootdir = "./res/"

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        a = 0;
        if filename.endswith("xml"):
            a = 1;
        
        if a == 0:
            continue
        nn1 = os.path.join(parent,filename)
        nn2 = os.path.join(parent,filename) + ".tmp"
        kk = "sed -e 's/com.easemob.chatuidemo/com.zhixu.icu/g' %s > %s"%(nn1, nn2)
        kk2 = "mv -f  %s  %s"%(nn2, nn1)

        os.system(kk)
        os.system(kk2)
