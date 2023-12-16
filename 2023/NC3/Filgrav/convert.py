import os
import glob
import binascii
i=0
mypath="./NC3/Filgrav/Export/"
for dirpath, dirs, files in os.walk(mypath):
    for filename in files:
        fname = os.path.join(dirpath,filename) 
        path = os.path.dirname(fname)
        dname = os.path.basename(path)
        if dname == 'Export':
            dname=''
        else:
            dname='/'+dname
        outdir='./NC3/Filgrav/hexout'+dname
        outfile=outdir+'/'+filename
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        with open(fname,errors='replace') as f, open(outfile, 'wb') as fout:
            stringhex=f.readline().replace('\n','')
            fout.write(
                binascii.unhexlify(stringhex)
            ) 
            fout.close()
