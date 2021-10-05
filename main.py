fails=open('aste.txt', 'r',encoding='utf-8')

count=0
while True:
    count+=1
    linija=fails.readline()

    if not linija:
       break
    print('rinda{}: {}'.format(count,linija.strip()))
fails.close()