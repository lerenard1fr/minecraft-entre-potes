# Minecraft Entre Potes — Site web

Site statique pour expliquer comment rejoindre le serveur Minecraft Entre Potes.

## Adresse du serveur

```
play.laconfreriefr.com
```

- **Java Edition** : `play.laconfreriefr.com` (port 25565)
- **Bedrock Edition** : `play.laconfreriefr.com` (port 25566)
- Comptes crackés acceptés ✅

## Hébergement sur GitHub Pages

1. Crée un nouveau dépôt sur GitHub.
2. Pousse ces fichiers sur la branche `main`.
3. Va dans **Settings → Pages**.
4. Source : **Deploy from a branch** → sélectionne `main` et dossier `/ (root)`.
5. Le site sera disponible sur `https://ton-pseudo.github.io/ton-repo/`.

## Fichiers

- `index.html` : page principale
- `infos.html` : page infos (statut, plugins, sauvegardes)
- `style.css` : mise en forme
- `images/` : logos en plusieurs tailles (64, 128, 256, 512)
- `server-icon.png` : logo source (à placer à la racine)
- `generate_logos.py` : script pour regénérer les tailles de logos
- `README.md` : ce fichier

## Logo

Place ton `server-icon.png` à la racine, puis lance :

```bash
python generate_logos.py
```

Cela génère les logos en plusieurs tailles dans `images/`.
