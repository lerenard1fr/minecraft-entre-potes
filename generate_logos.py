from PIL import Image
import os

# Créer le dossier images s'il n'existe pas
os.makedirs('images', exist_ok=True)

# Ouvrir l'image source
source = Image.open('server-icon.png')

# Tailles à générer
sizes = [64, 128, 256, 512]

for size in sizes:
    # Redimensionner avec une bonne qualité
    img = source.resize((size, size), Image.LANCZOS)
    
    # Sauvegarder en PNG
    png_path = f'images/logo-{size}.png'
    img.save(png_path, 'PNG', optimize=True)
    
    # Sauvegarder en WebP
    webp_path = f'images/logo-{size}.webp'
    img.save(webp_path, 'WEBP', quality=90, method=6)
    
    print(f'{size}x{size}: PNG={os.path.getsize(png_path)/1024:.1f} Ko, WebP={os.path.getsize(webp_path)/1024:.1f} Ko')

print('Logos générés avec succès !')
