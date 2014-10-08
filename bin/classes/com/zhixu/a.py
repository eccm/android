import os
import os.path
rootdir = "./icu/"

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        nn1 = os.path.join(parent,filename)
        nn2 = os.path.join(parent,filename) + ".tmp"
        kk = "sed -e 's/com.easemob.chatuidemo/com.zhixu.icu/g' %s > %s"%(nn1, nn2)
        kk2 = "mv -f  %s  %s"%(nn2, nn1)

        os.system(kk)
        os.system(kk2)
