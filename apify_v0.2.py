print("Bienvenue dans APIFY, le script de transcription en API du français standard.")
print("Le logiciel est créé et développé par Rémi Collin.")
print("Distribué sous licence Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Version actuelle 0.2")
phrase = input("Entrer la phrase à transcrire :")
mot = phrase.split()
ch=0
nb=0
C = ["r","t","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","z"] ## classe des consonnes du FR
V = ["a","e","i","o","u","y"] ## classe des voyelles du FR
Dictionnaire = {'petite':'pətit','bec':'bɛk','bel':'bɛl','chiropracteur':'kiʁopʁaktœʁ', 'asymptote':'asœ̃ptɔt>', 'techologie':'tɛknoloʒi', 'technologique':'tɛknoloʒik','techno':'tɛkno', 'année':'ane', 'femme':'fam', 'belle':'bɛl', 'ville':'vil', 'est':'ɛ', 'de':'də', 'le':'lə'}
concat = ""
def apify(mot):
    global ch
    global concat
    while ch < fin:
                        ######################### 
                        ##ANALYSE DES VOYELLES##
                        #########################
                        if mot[0:len(mot)] in Dictionnaire:
                                dic=len(mot)
                                concat+=Dictionnaire[mot]
                                ch=dic
                                continue

                        if (mot[ch]=="e"):
                                if ch==fin-1:
                                        ch+=1
                                        continue
                                elif mot[ch-1]=="j":
                                        concat+="ə"
                                        ch+=1
                                        continue

                                elif mot[ch+1]=="u":
                                        concat+="œ"
                                        ch+=2
                                        continue
                                elif mot[ch+1]=="s":
                                        concat+="ɛ"
                                        ch+=1
                                        continue
                                elif mot[ch+1]=="a" and mot[ch+2]=="u":
                                        concat+="o"
                                        ch+=3
                                        continue
                                elif mot[ch+1]=="i":
                                        if mot[ch+2]=="n":
                                                concat+="ɛ̃"
                                                ch+=3
                                                continue
                                        elif mot[ch+2]=="l":
                                                concat+="ɛj"
                                                ch+=3
                                                continue
                                elif mot[ch+1] in ["n","m"]:
                                        if mot[ch+2] in C:
                                                concat+="ɑ̃"                        
                                                ch+=2
                                                continue
                                        elif ch+1==fin:
                                                concat+="ɛ̃"
                                                ch+=2
                                                continue
                                        else:
                                                concat+="ə"
                                                ch+=1
                                                continue
                                elif mot[ch+1] in ["r","l","t","x"]:
                                        if ch+2==fin:
                                                concat+="e"
                                                ch+=2
                                                continue
                                        else:
                                                concat+="ɛ"
                                                ch+=1
                                                continue
                                elif mot[ch+1]=="s" and mot[ch+2]=="t":
                                        concat+="e"
                                        ch+=2
                                        continue
                                else:
                                        concat+="ə"
                                        ch+=1
                                        continue
                                        
                        if mot[ch] == "é":
                                concat+="e"
                                ch+=1
                                continue

                        if mot[ch]=="a":
                                if (ch == fin-1):
                                        concat+="a"
                                        ch+=1
                                        continue
                                if (mot[ch+1] in ["n","m"]):
                                        if (ch+2 == fin):
                                                concat+="ɑ̃"
                                                ch+=2
                                                continue
                                        elif mot[ch+2] in ["r","t","p","q","s","d","f","g","h","j","k","l","w","x","c","v","b","z"]:
                                                concat+="ɑ̃"
                                                ch+=2
                                                continue
                                        elif mot[ch+2] in ["n","m"]:
                                                concat+="a"
                                                ch+=2
                                                continue
                                        elif (mot[ch+2] in V):
                                                concat+="a"
                                                ch+=1
                                                continue                
                                elif (mot[ch+1]=="u"):
                                        concat+="o"
                                        ch+=2
                                        continue
                                elif (mot[ch]=="a" and mot[ch+1]=="i" and mot[ch+2] in ["l"]):
                                        concat+="aij"
                                        ch+=3
                                        continue
                                elif (mot[ch]=="a" and mot[ch+1]=="i" and mot[ch+2] not in ["n","m"]):
                                        concat+="ɛ"
                                        ch+=2
                                        continue
                                elif (mot[ch]=="a" and mot[ch+1]=="i" and mot[ch+2] in ["n","m"]):
                                        concat+="ɛ̃"
                                        ch+=3
                                        continue
                                else:
                                        concat+="a"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "i":
                                if (ch == fin-1):
                                        concat+="i"
                                        ch+=1
                                        continue

                                elif (mot[ch+1]=="o" and mot[ch+2]=='n'):
                                        concat+="j"
                                        ch+=1
                                        continue
                                elif (mot[ch+1]=="e"):
                                        if ch+2==fin:
                                                concat+="i"
                                                ch+=2
                                                continue
                                        elif mot[ch+2]=='n':
                                                concat+="jɛ̃"
                                                ch+=3
                                                continue
                                        elif mot[ch+2]=='l':
                                                concat+="jɛl"
                                                ch+=3
                                                continue
                                        elif mot[ch+1]=="e" and mot[ch+2]=='r' :
                                                concat+="j"
                                                ch+=1
                                                continue
                                        elif (ch+1==fin-1):
                                                concat+="i"
                                                ch+=3
                                                continue
                                        elif (mot[ch+1]=="e" and mot[ch+2]=='u'):
                                                concat+="j"
                                                ch+=1
                                                continue
                                elif (mot[ch+1]=="a"):
                                        concat+="j"
                                        ch+=1
                                        continue
                                elif (mot[ch+1]=="è"):
                                        concat+="j"
                                        ch+=1
                                        continue
                                elif ((mot[ch+1]=="n" or mot[ch+1]=='m') and mot[ch+2] in V):
                                        concat+="i"
                                        ch+=1
                                        continue
                                elif ((mot[ch+1]=="n" or mot[ch+1]=='m') and mot[ch+2] in C):
                                        concat+="ɛ̃"
                                        ch+=2
                                        continue
                                else:
                                        concat+="i"
                                        ch+=1
                                        continue
                                        
                        if mot[ch] == "u":
                                if (ch == fin-1):
                                        concat+="y"
                                        ch+=1
                                        continue
                                elif mot[ch-1] == "q":
                                        ch+=1
                                        continue
                                elif (mot[ch-2]=="e" and mot[ch-1]=='a'):
                                        ch+=1
                                        continue
                                elif (mot[ch+1] in ["i"]):
                                        concat+="ɥ"
                                        ch+=1
                                        continue
                                elif (mot[ch+1] in ["n","m"] and ch+1==fin-1):
                                        concat+="œ̃"
                                        ch+=2
                                        continue
                                elif (mot[ch+1] in ["n","m"] and mot[ch+2]==fin-1):
                                        concat+="œ̃"
                                        ch+=2
                                        continue
                                elif (mot[ch+1] in ["n","m"] and mot[ch+2] in C):
                                        concat+="œ̃"
                                        ch+=2
                                        continue
                                
                                elif (mot[ch+1] in ["n","m"] and ch+2==fin):
                                        concat+="œ̃"
                                        ch+=2
                                        continue
                                elif (mot[ch-1]=="a"):
                                        ch+=1
                                        continue
                                else:
                                        concat+="y"
                                        ch+=1
                                        continue

                        if mot[ch] == "y":
                                if mot[ch+1] in ["n","m"] and mot[ch+2] in C:
                                        concat+="ɛ̃"
                                        ch+=2
                                        continue
                                if mot[ch+1] in ["n","m"] and mot[ch+2] in V:
                                        concat+="i"
                                        ch+=1
                                        continue
                                else:
                                        concat+="i"
                                        ch+=1
                                        continue

                        if mot[ch] == "o":
                                if (ch == fin-1):
                                        concat+="o"
                                        ch+=1
                                        continue
                                elif (mot[ch+1] in ["r","t","p","q","s","d","f","g","h","j","k","l","w","x","c","v","b","z"] and ch+1==fin-1):
                                        concat+="ɔ"
                                        ch+=1
                                        continue
                                elif (mot[ch+1]=="ù"):
                                        concat+="u"
                                        ch+=2
                                        continue
                                elif (mot[ch+1] in ["n","m"] and ch+1 == fin-1):
                                        concat+="ɔ̃"
                                        ch+=2
                                        continue
                                elif (mot[ch+1] in ["n","m"] and mot[ch+2] in ["r","t","p","q","s","d","f","g","h","j","k","l","w","x","c","v","b","z"]):
                                        concat+="ɔ̃"
                                        ch+=2
                                        continue
                                elif mot[ch+1] =="n" and mot[ch+2] == "n":
                                        concat+="o"
                                        ch+=2
                                        continue
                                elif mot[ch+1] =="n" and mot[ch+2] in V:
                                        concat+="o"
                                        ch+=1
                                        continue
                                elif mot[ch+1] =="i":
                                        concat+="wa"
                                        ch+=2
                                        continue
                                elif mot[ch+1] =="n" and mot[ch+2]=="n":
                                        concat+="ɔ"
                                        ch+=1
                                        continue
                                elif mot[ch+1] =="u":
                                        concat+="u"
                                        ch+=2
                                        continue
                                else:
                                        concat+="o"
                                        ch+=1
                                        continue

                        if mot[ch] == "è":
                                concat+="ɛ"
                                ch+=1
                                continue
                        

                                #########################         
                                ##ANALYSE DES CONSONNES##
                                #########################        
                        
                        if mot[ch] == "s":
                                if(ch == fin-1):
                                        ch+=1
                                        continue
                                elif(ch==0 or mot[ch+1] in ["r","t","p","q","d","f","g","h","j","k","l","m","w","x","c","v","b","n","z"]):
                                        concat+="s"
                                        ch+=1
                                        continue
                                elif(mot[ch+1]=="s"):
                                        concat+="s"
                                        ch+=2
                                        continue
                                else:
                                        concat+="z"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "n":
                                if (ch == fin-1):
                                        ch+=1
                                        continue
                                elif mot[ch+1]== "n":
                                        concat+="n"                               
                                        ch+=2
                                        continue
                                else:
                                        concat+="n"
                                        ch+=1
                                        continue
                        
                        if mot[ch] == "d":
                                concat+="d"
                                ch+=1
                                continue


                        if mot[ch] == "t":
                            
                                if (ch == fin-1):
                                        ch+=1
                                        break
        ##                        if (ch == fin-2):
        ##                                ch+=1
        ##                                break
                                elif (mot[ch+1 : ch+6]=="echno"):
                                        concat+="tɛkno"
                                        ch+=6
                                        continue
                                elif (mot[ch+1 : ch+4]=="ion"):
                                        concat+="s"
                                        ch+=1
                                        continue
                                elif mot[ch+1]== "t":
                                        ch+=1
                                        continue
                                else:
                                        concat+="t"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "r":
                                if (ch == fin-1):
                                        concat+="ʁ"
                                        ch+=1
                                        break
                                if mot[ch+1]== "r":
                                        concat+="ʁ"
                                        ch+=2
                                        continue
                                else:
                                        concat+="ʁ"
                                        ch+=1
                                        continue
                        
                        if mot[ch] == "m":
                                if (ch == fin-1):
                                        concat+="m"
                                        ch+=1
                                        break
                                if mot[ch+1]== "m":
                                        concat+="m"
                                        ch+=2
                                        continue
                                else:
                                        concat+="m"
                                        ch+=1
                                        continue

                        if mot[ch] == "q":
                                if mot[ch+1] == "u":
                                        concat+="k"
                                        ch+=1
                                        continue
                        

                        if mot[ch] == "l":
                                if (ch == fin-1):
                                        concat+="l"
                                        ch+=1
                                        continue
                                if mot[ch+1]== "l":
                                        if mot[ch+2:ch+6]=="ement":
                                                concat+="l"
                                                ch+=2
                                                continue
                                        if mot[ch+2]=="o":
                                                concat+="l"
                                                ch+=2
                                                continue
                                        if mot[ch+2]=="e":
                                                concat+="j"
                                                ch+=2
                                                continue
                                elif mot[ch+1]== "l" and mot[ch+2]=="o":
                                        concat+="l"
                                        ch+=2
                                        continue
                                else:
                                        concat+="l"
                                        ch+=1
                                        continue
                                        
                                
                        if mot[ch] == "b":
                                concat+="b"
                                ch+=1
                                continue
                        
                        if mot[ch] == "x":
                                if ch==fin-1:
                                        ch+=1
                                        continue
                                elif mot[ch+1] in ["c","q","p","r","v","t"]:
                                        concat+="ks"
                                        ch+=1
                                        continue
                                elif mot[ch+1] in ["o","e","a","i"]:
                                        concat+="gz"
                                        ch+=1
                                        continue
                        
                        if mot[ch] == "w":
                                if mot[ch+1]== "w":
                                        ch+=2
                                        continue
                                else:
                                        concat+="w"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "h":
                                ch+=1
                                continue
                        
                        if mot[ch] == "z":
                                if mot[ch+1]== "z":
                                        ch+=1
                                        continue
                                else:
                                        concat+="z"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "v":
                                if mot[ch+1]== "v":
                                        ch+=1
                                        continue
                                else:
                                        concat+="v"
                                        ch+=1
                                        continue
                                
                        
                        if mot[ch] == "j":
                                if mot[ch+1]== "ʒ":
                                        ch+=1
                                        continue
                                else:
                                        concat+="ʒ"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "g":
                                if (mot[ch+1] in ["u","a","o"]):
                                        concat+="g"
                                        ch+=1
                                        continue
                                elif (mot[ch+1]=="n"):
                                        concat+="ɲ"
                                        ch+=2
                                        continue
                                else:
                                        concat+="ʒ"
                                        ch+=1
                                        continue
                                
                        if mot[ch] == "m":
                                if mot[ch+1]== "m":
                                        ch+=2
                                        continue
                                else:
                                        concat+="m"
                                        ch+=1
                                        continue

                        if mot[ch]=="c":
                                if(ch==fin-1):
                                        concat+="k"
                                        ch+=1
                                        continue
                                if(mot[ch+1] in ["o","a","u","t","r","l"]):
                                        concat+="k"
                                        ch+=1
                                        continue
                                elif(mot[ch+1] in ["i","e","y", "é"]):
                                        concat+="s"
                                        ch+=1
                                        continue    
                                elif(mot[ch+1]=="h"):
                                        if (mot[ch+2 : ch+3]=="ri"):
                                                concat+= "kʁi"
                                                ch+=4
                                                continue
                                        else:
                                                concat+= "ʃ"
                                                ch+=2
                                                continue
                                


                        if mot[ch] == "f":
                                concat+="f"
                                ch+=1
                                continue

                        if (mot[ch] == "p"):
                                if (ch == fin-1):
                                        concat+="p"
                                        ch+=1
                                        break
                                elif mot[ch+1]=="h":
                                        concat+="f"
                                        ch+=2
                                        continue
                                elif mot[ch+1]=="p":
                                        concat+="p"
                                        ch+=2
                                        continue
                                elif (ch == fin-1):
                                        concat+="p"
                                        ch+=1
                                        break
                                else:
                                        concat+="p"
                                        ch+=1
                                        continue
                        if mot[ch]=="\'":
                                concat+=""
                                ch+=1
                                continue
                        if mot[ch]==" ":
                                concat+=""
                                ch+=1
                                continue

    #print(concat)


for Item in mot:
    fin = len(mot[nb])
    apify(mot[nb])
    ch=0
    nb+=1
    del fin
print(concat)
print("Merci ! En cas de problème de transcription, merci de signaler sur le GitHub les mots mal transcrits. Merci pour votre aide !")
