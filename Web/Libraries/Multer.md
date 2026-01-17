# Multer

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Multer is a node.js middleware for handling `multipart/form-data`, which is primarily used for uploading files. It is written on top of busboy for maximum efficiency.

## Website / Link
- [Repository](https://github.com/expressjs/multer)
- [NPM](https://www.npmjs.com/package/multer)

## Installation
```bash
# Install multer
npm install multer
```

## Useful Commands / Tips
- `upload = multer({ dest: 'uploads/' })`: Basic configuration to save files to a folder.
- `app.post('/profile', upload.single('avatar'), ...)`: Middleware to handle a single file upload.

## Configuration
- Can be configured with disk storage (where to store files) or memory storage (keep files in memory as buffers).
  ```javascript
  const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, '/tmp/my-uploads')
    },
    filename: function (req, file, cb) {
      cb(null, file.fieldname + '-' + Date.now())
    }
  })
  ```

## Notes
Do not verify `multipart/form-data` bodies with body-parser; use Multer for that.

---

# Version Française

## Description
Multer est un middleware node.js pour gérer le `multipart/form-data`, qui est principalement utilisé pour le téléchargement de fichiers. Il est écrit au-dessus de busboy pour une efficacité maximale.

## Site Web / Lien
- [Dépôt](https://github.com/expressjs/multer)
- [NPM](https://www.npmjs.com/package/multer)

## Installation
```bash
# Installer multer
npm install multer
```

## Commandes Utiles / Astuces
- `upload = multer({ dest: 'uploads/' })`: Configuration de base pour enregistrer les fichiers dans un dossier.
- `app.post('/profile', upload.single('avatar'), ...)`: Middleware pour gérer un téléchargement de fichier unique.

## Configuration
- Peut être configuré avec un stockage sur disque (où stocker les fichiers) ou un stockage en mémoire (garder les fichiers en mémoire sous forme de tampons).
  ```javascript
  const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, '/tmp/my-uploads')
    },
    filename: function (req, file, cb) {
      cb(null, file.fieldname + '-' + Date.now())
    }
  })
  ```

## Notes
Ne vérifiez pas les corps `multipart/form-data` avec body-parser ; utilisez Multer pour cela.
