import os
import time
import pyautogui


NbPages = 5
Décompte = 4
Captures = []

# Dimensions de la zone de rognage
gauche, haut, droite, bas = 50, 80, 50, 1366-1255  #768x1366

# Chemin du dossier pour sauvegarder le livre
dossier_sauvegarde = "C:\\Users\\CTM-010676\\Documents\\Livres-Numériques"

# S'assurer que le dossier de sauvegarde existe, sinon le créer
if not os.path.exists(dossier_sauvegarde):
    os.makedirs(dossier_sauvegarde)

for i in range(Décompte):
    print("Début dans " + str(Décompte-i) + " secondes")
    time.sleep(1)

for i in range(NbPages):

    # Prendre une capture d'écran et l'ajouter à la liste
    s = pyautogui.screenshot()
    s = s.crop((gauche, haut, s.width - droite, s.height - bas))
    Captures.append(s)

    #Changement de page avec un clic ou la flèche droite
    pyautogui.press('right')
    #pyautogui.click()
    
    time.sleep(0.7)

#Copie la première image puis la supprime de la liste (nécessaire pour la conversion)
Im1 = Captures[0]
del Captures[0]

#Convertit la liste d'image en un fichier PDF
Im1.save(os.path.join(dossier_sauvegarde, 'A-Z_Philo.pdf'), save_all=True, append_images=Captures)

print("Terminé. Fichier enregistré dans ", dossier_sauvegarde)

