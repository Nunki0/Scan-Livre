import os
import time
import pyautogui
import pngconverter

def Scan():
    NbPages = 546-164
    Décompte = 4

    for i in range(Décompte):
        print("Début dans " + str(Décompte-i) + " secondes")
        time.sleep(1)



    # Chemin du dossier pour sauvegarder les captures d'écran
    dossier_sauvegarde = "C:\\Users\\CTM-010676\\Documents\\Livres"

    # S'assurer que le dossier de sauvegarde existe, sinon le créer
    if not os.path.exists(dossier_sauvegarde):
        os.makedirs(dossier_sauvegarde)

    for i in range(NbPages):
        # Prendre une capture d'écran
        screenshot = pyautogui.screenshot()

        # Chemin complet pour sauvegarder la capture dans le dossier spécifié
        chemin_capture = os.path.join(dossier_sauvegarde, f"capture_{i}.png")
        screenshot.save(chemin_capture)

        #Changement de page avec un clic ou la flèche droite
        pyautogui.press('right')
        #pyautogui.click()
        
        time.sleep(0.7)

    print("Terminé. Captures d'écran enregistrées dans", dossier_sauvegarde)

Scan()
pngconverter.Convert()
