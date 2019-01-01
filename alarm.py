


dari  waktu  impor  strftime  sebagai  tm
from time import sleep
from os import system as sis
import sys
import subprocess as sp
lg = '\033[92m'
lr = '\033[91m'
x = '\033[0m'
# Proyek alarm hehe
# Alarm ini bisa bikin butlup
# 
# masi dalam pengembangan
# buat ngancurin satelit NASA, hek pesbuk dan hek wipi
# hehehe

def anu():
      try:
            while True:
                  waktu=tm('%I:%M:%S %p')
                  if waktu == alarm:
                        lup = True
                        sis('clear')
                        print('\tALARMNYA BUNYI GAYN !!\n')
                        print('kang heker berkata: '+lr+pesan+lg)
                        print ('\n\n\n\n\nteken ctrl+c biar stop mendadak')
                        sp.call('mpv .nada',shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)
                        
                        break
                  else:
                        print('\rSekarang jam ',waktu,end=''),;sys.stdout.flush();sleep(0.5)
                        set=str(waktu)
      except KeyboardInterrupt:
            print('\nhehe'+x)      
      
if __name__=='__main__':
      sis('clear')
      print (lg+'\tINI ALARM GAYN !!\n')
      j=input('jam (jj) > ')
      m=input('menit (mm) > ')
      d=input('detik (dd) > ')
      print(lr+'\n jam 12 malem - 12 siang = am (pagi)\n jam 12 siang - 12 malem = pm (siang)\n')
      ap = input(lg+'pagi(am) apa siang(pm) ?: ').upper()
      pesan =input('Masukan pesan : ')
      alarm = j+':'+m+':'+d+' '+ap
      
      print('oke. alarm sudah di atur !')
      sleep(1)
      sis('clear')
      print ('\tALARM HEHE !')
      print('\nalarm diatur jam: '+j+':'+m+' '+ap)
      anu()
      
      
