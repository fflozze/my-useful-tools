# FileZilla

> [!TIP]
> [Passer à la version française](#version-française)

## Description
FileZilla is a free and open-source FTP, FTPS, and SFTP client. It is one of the most popular tools for transferring files between a local computer and a remote server. It offers an intuitive graphical interface with drag-and-drop support, allowing easy management of downloads and uploads.

## Website / Link
- [Official Website](https://filezilla-project.org/)
- [Documentation](https://wiki.filezilla-project.org/Documentation)

## Installation
Download the client installer from the official website:
- [Download](https://filezilla-project.org/download.php?type=client)

The installation is standard (Next, Next...) but **be careful** with optional offers (adware) sometimes proposed in the free installer; be sure to decline them.

## Useful Commands / Tips
- **Site Manager** (`CTRL + S` or `CMD + S`): Save your connection profiles (Host, User, Port, Protocol) to reconnect quickly.
- **Drag and Drop**: Transfer files simply by dragging them from the local window to the remote window (and vice versa).
- **Edit on the fly**: Right-click on a remote file > `View/Edit`. FileZilla downloads the file, opens it in your editor, and offers to re-upload it as soon as you save changes.
- **Filters**: Use filename filters (Funnel icon) to hide or exclude files (e.g., `.DS_Store`, `Thumbs.db`, `.git/`) from transfers.

## Configuration
- **Default Editor**: `Edit` > `Settings` > `File editing`. Associate it with your favorite IDE (VS Code, Sublime Text, Notepad++, etc.) to edit files directly.
- **Concurrent Connections**: In Site Manager, `Transfer Settings` tab, you can limit the number of simultaneous connections to avoid being banned by strict FTP servers.

## Notes
- There is a **FileZilla Pro** version (paid) that adds support for cloud protocols like Amazon S3, Google Cloud Storage, Microsoft Azure, WebDAV, etc.
- **Security**: If you save your passwords in the Site Manager, it is strongly recommended to set a master password in FileZilla to encrypt these locally stored credentials.

---

# Version Française

## Description
FileZilla est un client FTP, FTPS et SFTP gratuit et open-source. C'est l'un des outils les plus populaires pour transférer des fichiers entre un ordinateur local et un serveur distant. Il propose une interface graphique intuitive avec support du glisser-déposer, permettant de gérer facilement les téléchargements et les téléversements.

## Site Web / Lien
- [Site Officiel](https://filezilla-project.org/)
- [Documentation](https://wiki.filezilla-project.org/Documentation)

## Installation
Télécharger l'installateur client depuis le site officiel :
- [Download](https://filezilla-project.org/download.php?type=client)

L'installation est standard (Suivant, Suivant...) mais **attention** aux offres optionnelles (adware) parfois proposées dans l'installateur gratuit ; pensez à les refuser.

## Commandes Utiles / Astuces
- **Gestionnaire de Sites (Site Manager)** : `CTRL + S` (ou `CMD + S`). Permet de sauvegarder vos profils de connexion (Hôte, User, Port, Protocole) pour s'y reconnecter rapidement.
- **Glisser-Déposer** : Transférez des fichiers simplement en les faisant glisser de la fenêtre locale vers la fenêtre distante (et inversement).
- **Édition à la volée** : Clic droit sur un fichier distant > `Afficher/Éditer`. FileZilla télécharge le fichier, l'ouvre dans votre éditeur, et propose de le ré-uploader dès que vous sauvegardez les modifications.
- **Filtres** : Utilisez les filtres de noms de fichiers (Icône entonnoir) pour masquer ou exclure des fichiers (ex: `.DS_Store`, `Thumbs.db`, `.git/`) des transferts.

## Configuration
- **Éditeur par défaut** : `Édition` > `Paramètres` > `Édition des fichiers`. Associez-le à votre IDE favori (VS Code, Sublime Text, Notepad++, etc.) pour modifier les fichiers directement.
- **Connexions simultanées** : Dans le Gestionnaire de sites, onglet `Paramètres de transfert`, vous pouvez limiter le nombre de connexions simultanées pour éviter d'être banni par certains serveurs FTP stricts.

## Notes
- Il existe une version **FileZilla Pro** (payante) qui ajoute le support de protocoles cloud comme Amazon S3, Google Cloud Storage, Microsoft Azure, WebDAV, etc.
- **Sécurité** : Si vous enregistrez vos mots de passe dans le gestionnaire de sites, il est fortement recommandé de définir un mot de passe maître dans FileZilla pour chiffrer ces identifiants stockés localement.
