import sys
import os
import time
import socket
import random
import requests
#"╔══════════╗"
#"║  ║"
#"╚══════════╝"
# ═╣ ╠═
maxi = 10
memo1 = "0"
memo2 = "1"
memo3 = "2"
curso = ">"
print("\033[91m                              ______________                               ")
print("\033[91m                        ,===:'.,            `-._                           ")
print("\033[91m                             `:.`---.__         `-._                       ")
print("\033[91m                               `:.     `--.         `.                     ")
print("\033[91m                                 \.        `.         `.                   ")
print("\033[91m                         (,,(,    \.         `.   ____,-`.,                ")
print("\033[91m                      (,'     `/   \.   ,--.___`.'                         ")
print("\033[91m                  ,  ,'  ,--.  `,   \.;'         `                         ")
print("\033[91m                   `{D, {    \  :    \;                                    ")
print("\033[91m                     V,,'    /  /    //                                    ")
print("\033[91m                     j;;    /  ,' ,-//.    ,---.      ,                    ")
print("\033[91m                     \;'   /  ,' /  _  \  /  _  \   ,'/                    ")
print("\033[91m                           \   `'  / \  `'  / \  `.' /                     ")
print("\033[91m                           `.___,'   `.__,'   `.__,'  ")

print("")
time.sleep(.9)

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
print("\033[91m")

for x in range(9000):

 res = input("\033[91m"+curso+"\033[97m ")
 if res == "clear":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
 if res == "reboot":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print("\033[91m[+]\033[97m Rebooting...")
  time.sleep(.2)
  os.system("python3 lizard.py")
 if res == "sys":
  

  print('\033[97m Created By Marcus V')
  print('\033[97m LizardOS Modular Baseado em Python 3.7')
  print('\033[91m 1.9 \033[97m | \033[92mSilverSide Version')
 if res == "modules build":
   print('\033[92m#  \033[97mUse this command to create a module to lizardOS ')
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')
   mod1 = input("\033[97mModule Name\033[92m>      \033[97m")
   os.mknod(mod1 + ".module")

   my_file = open(mod1 + ".module", "w")
   text_list = ["# This is a module for LizardOS\n", "print('Hello World! i am " +mod1+ " a module to lizardOS')"] 

   my_file.writelines(text_list) 

   my_file = open(mod1 + ".module")


   content = my_file.read()


   my_file.close()
    
   print('\033[92m#  \033[97mThe module: ' + mod1 + ' is created!')
   print('\033[91m#  \033[97m Use "run" to view your module')
	 
	
	
	

 if res == "modules":
	 # ═╣ ╠═
  print("╔═════════════════ \033[92mDEVELOPER ZONE \033[97m═════════════════╗")
  print("║                                                  ║")
  print("╠══════════════════════════════════════════════════╣")
  print("║                                                  ║")
  print('║         Build , Run , Import[OFF] , \033[91mCancel\033[97m       ║')
  print("║                                                  ║")
  print("╚══════════════════════════════════════════════════╝")

  escl = input('\033[97mDev\033[92m>  	\033[97m')
  if escl == "run":
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')
   os.system("dir")
   print("")
   print('\033[92m#  \033[97mDon`t need ".module" on final of file')
   pop1 = input("\033[97mModule Name\033[92m> \033[97m")
   os.rename(str(pop1) + ".module",str(pop1) + ".py")
   os.system("python3 " + str(pop1) + ".py")
   os.rename(str(pop1) + ".py",str(pop1) + ".module")
  if escl == "build":   
   
   print('\033[92m#  \033[97mUse this command to create a module to lizardOS ')
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')
   mod1 = input("\033[97mModule Name\033[92m>      \033[97m")
   os.mknod(mod1 + ".module")

   my_file = open(mod1 + ".module", "w")
   text_list = ["# This is a module for LizardOS\n", "print('Hello World! i am " +mod1+ " a module to lizardOS')"] 

   my_file.writelines(text_list) 

   my_file = open(mod1 + ".module")


   content = my_file.read()


   my_file.close()
    
   print('\033[92m#  \033[97mThe module: ' + mod1 + ' is created!')
   print('\033[91m#  \033[97m Use "run" to view your module')

 if res == "echo":
  res = input("\033[97m ")
  
  
 if res == "modules run":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print('\033[92m#  \033[97mDon`t need ".module" on final of file')
  print('\033[91m#  \033[97mAlert you are using a fast run!')
  pop1 = input("\033[97mModule Name\033[92m> \033[97m")
  os.rename(str(pop1) + ".module",str(pop1) + ".py")
  os.system("python3 " + str(pop1) + ".py")
  os.rename(str(pop1) + ".py",str(pop1) + ".module")

 if res == "ping":
  pop1 = input("\033[97mIP\033[92m> \033[97m")
  print('\033[92m#  \033[97mUse CTRL+C to stop! ')

  os.system("ping " + str(pop1) + " -c 5")

 if res == "dir":
	 
  os.system("dir")
 if res == "admin":
  pop1 = input("@Local\033[91m> \033[97m")
  os.system(pop1)
 if res == "date":
  os.system("date")
 if res == "memorys":
	 # ═╣ ╠═
  print("╔═════════════════ \033[92mMemory  ZONE \033[97m═══════════════════╗")
  print("║                                                  ║")
  print("╠══════════════════════════════════════════════════╣")
  print("║                                                  ║")
  print('║         Edit , View , Import[OFF] , \033[91mCancel\033[97m       ║')
  print("║                                                  ║")
  print("╚══════════════════════════════════════════════════╝")

  escl = input('\033[97m?\033[92m>  	\033[97m')
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  if escl == "getter":
   os.system("python3 getter.py")
  if escl == "edit":
  
   print("╔══════════════════════\033[92m EDIT \033[97m══════════════════════╗")
   print("║                                                  ║")
   print('║       memo1, memo2, memo3, cursor, \033[91mcancel\033[97m        ║')
   print("║                                                  ║")
   print("╚══════════════════════════════════════════════════╝") 
   
   escl = input('\033[97mMemory\033[92m>  	\033[97m')
   if escl == "memo1":   
    print('\033[97m[\033[92mSelected Memory One\033[97m]')
    memo1 = input('\033[97mSet\033[92m>  	\033[97m') 
   if escl == "memo2":   
    print('\033[97m[\033[92mSelected Memory Two\033[97m]')
    memo2 = input('\033[97mSet\033[92m>  	\033[97m') 
   if escl == "memo3":   
    print('\033[97m[\033[92mSelected Memory Three\033[97m]')
    memo3 = input('\033[97mSet\033[92m>  	\033[97m') 
   if escl == "cursor":   
    print('\033[97m[\033[92mSelected Cursor(STRING)\033[97m]')
    curso = input('') 
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')
  if escl == "view":
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')	 
   print("╔══════════════════════\033[92m VIEW \033[97m══════════════════════╗")
   print("║                                                  ║")
   print('║        memo1, memo2, memo3, cursor(STRING)       ║')
   print("║                                                  ║")
   print("╚══════════════════════════════════════════════════╝")
   escl = input('\033[97mView\033[92m>  	\033[97m')
   if escl == "memo1":   
    print(memo1)
   if escl == "memo2":   
    print(memo2)
   if escl == "memo3":   
    print(memo3)
    
  
 if res == "update":
    import requests
    sites = [
        'https://raw.githubusercontent.com/0Hyd3/LizardOS/master/updates'
    ]
    for url in sites:
        r = requests.get(url)
        page_source = r.text
        page_source = page_source.split('\n')
        print("-------------\033[92mPATCH NOTES\033[97m--------------")
        print("")
       
        for row in page_source[:20]:
            print(row)
        print("")
        print("--------------------------------------")
 if res == "help":
  print("------------------------------------\033[94mHelp Me\033[97m------------------------------------")
  print("\033[97m echo \033[92m#Escreve algo no terminal ")
  print("\033[97m clear \033[92m#Limpa o terminal ")
  print("\033[97m modules \033[92m#Abre o menu de gerenciamento de modulos do sistema ")
  print("\033[97m getter \033[92m#Abre a loja de modulos (NECESSARIO ESTAR INSTALADA)")
  print("\033[97m memorys \033[92m#Abre o menu de gerenciamento de variaveis do sistema ")
  print("\033[97m ping \033[92m#Verifica sua conexao com outros servicos ")
  print("\033[97m reboot \033[92m#Reinicia o lizard (DEV-MODE) ")
  print("\033[97m sys \033[92m#Descricao da versao atual do seu sistema ")
  print("\033[97m update \033[92m#Verifica se ha uma versao mais nova")
  print("\033[97m-------------------------------------------------------------------------------")
  
  
