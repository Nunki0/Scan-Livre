from PIL import Image
import os

#Liste des inmages à convertir
Liste_Image = []

# Chemin du dossier contenant les images à rogner
dossier_images = "C:\\Users\\CTM-010676\\Documents\\Livres"

# Dimensions de la zone de rognage
gauche, haut, droite, bas = 480, 35, 480, 768-716

# Liste des extensions d'images que vous souhaitez traiter
extensions_images = ['.png']

# Parcourir le dossier
for fichier in os.listdir(dossier_images):
    chemin_fichier = os.path.join(dossier_images, fichier)

    # Vérifier si le fichier est une image avec l'extension souhaitée
    if os.path.isfile(chemin_fichier) and any(chemin_fichier.lower().endswith(ext) for ext in extensions_images):

        # Ouvrir l'image
        image = Image.open(chemin_fichier)

        # Rogner l'image
        image_rognée = image.crop((gauche, haut, image.width - droite, image.height - bas))

        #Ajoute l'image rognée à la liste d'images à convertir
        Liste_Image.append(image_rognée.convert('RGB'))

print("Images rognées.")

#Copie la première image puis la supprime de la liste (nécessaire pour la conversion)
Im1 = Liste_Image[0]
del Liste_Image[0]

#Convertit la liste d'image en un fichier PDF
Im1.save(os.path.join(dossier_images, 'Livre.pdf'), save_all=True, append_images=Liste_Image)

print("Fichier PDF créé.")


