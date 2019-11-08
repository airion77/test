import os
from datetime import datetime

inputDate = datetime.strptime(str("20191105"), '%Y%m%d')

for (path, dirs, files) in os.walk(r'J:\Down', False):
    for dirname in dirs:
        print('경로 : [%s], 디렉토리 : [%s]' %(path,dirname))
    '''
    for filename in files:
        fileMtime = datetime.fromtimestamp(os.path.getmtime(path+'\\'+filename))
        if inputDate < fileMtime:
            print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
    '''