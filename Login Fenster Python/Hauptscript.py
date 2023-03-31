#WICHTIG!!!!
#die datei muss in eine exe umgewandelt werden, weil ansonsten andere die Benutzer und passwörter sehen können. einfach im internet google`n` (python datei in exe umwandeln)
#oder ihr verschlüsselt die .py datei 


import random        #dinge die ihr als voraussetzung braucht(einfach mit cmd (admin) : pip install (vorrausetzung)  (installieren) )
import time

#INFO:
#Die Login seite ist von mir selber erstellt worden. Ich werde versuchen das Script zu verbessern bis es Fertig ist.
#ich habe überall texte hingeschrieben wo ihr dinge ändern könnt oder wo ihr was hinzufügen könnt.
print("Version 0.2")
print("Do you want to Login  1 YES/2 NO?")  #Text kann übersetzt werden oder komplett geändert werden.
number = input(">>")         #das symbol (>>) was hinzeigt wo das passwort eingegeben wird. Kann geändert werden.
print("")
text1 = input("Type your Username >")   #kann geändert werden.
t = text1.lower()
print("")         #einfach nur dafür das eine Zeile platz zwischen dem Usernamen eingeben und Passwort eingeben ist


#das ist der wichtige part vom script 
#hier sind alle Benutzernamen und passwörter gespeichert.
#um mehr benutzer und passwörter zu adden einfach benutzername 1 und passwort 1 kopieren und daten ändern/anpassen

if text1 == "test1":     #Benutzername 1 ("test1")
        text2 = input("Type your Password >")  #kann übersetzt oder geändert werden      
        t = text2.lower()

if text2 == "test2":    #passwort für den Benutzernamen 1 ("test2")
        print("")
        print("hello test")  #das ist der text der am ende für den benutzer sichbar ist (z.b. Links für discord oder mega etc.)
       

#das ist der part wenn ein benutzername oder passwort falsch eingegeben wird
else:
    print("Your Username or Password is Wrong!")    #änderbar   
    print("Try Again")                              #änderbar

time.sleep(10);      #zeit bis sich das fenster schließt nach eingabe vom falschem passwort. zum ändern einfach (10) zu (zahl) ändern



