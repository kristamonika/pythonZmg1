import os
if os.path.exists('aste.txt'):
    os.remove('aste.txt')
else:
    print('Fails neeksistē!')
os.rmdir('bildes')