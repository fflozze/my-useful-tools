# Firefox

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Firefox is a free and open-source web browser developed by the Mozilla Foundation. It uses the Gecko rendering engine to display web pages, which implements current and anticipated web standards. Firefox is known for its extensive customizability, strong privacy features, and commitment to an open web.

## Website / Link
- [Official Website](https://www.mozilla.org/en-US/firefox/new/)
- [Mozilla Developer Network (MDN)](https://developer.mozilla.org/)

## Installation
```bash
# Windows (via Winget)
winget install -e --id Mozilla.Firefox

# macOS (via Homebrew)
brew install --cask firefox

# Linux (Ubuntu/Debian)
sudo apt install firefox

# Direct Download
# Visit https://www.mozilla.org/en-US/firefox/new/
```

## Useful Commands / Tips
- `Address Bar Shortcuts`:
    - `*` + Space: Search Bookmarks
    - `%` + Space: Search Open Tabs
    - `^` + Space: Search History
- `Ctrl + Shift + P`: Open Private Window
- `Ctrl + Shift + M`: Toggle Responsive Design Mode (for developers)
- `Shift + F5` or `Ctrl + Shift + R`: Hard Reload (clear cache for page)
- `about:config`: Access advanced configuration settings (use with caution).
- `about:profiles`: Manage Firefox profiles.

## Configuration
- **Settings**: Accessible via `about:preferences` or the hamburger menu.
- **Extensions**: Manage add-ons via `about:addons` (`Ctrl + Shift + A`).
- **user.js**: A configuration file that can be used to harden Firefox privacy settings (e.g., [Arkenfox](https://github.com/arkenfox/user.js)).
- **Sync**: Use a Firefox Account to sync bookmarks, history, passwords, and open tabs across devices.

## Notes
- Firefox is one of the few major browsers not based on Chromium, helping to maintain diversity in the browser engine market.
- It has excellent DevTools, especially for CSS Grid and Flexbox debugging.
- Privacy features like Enhanced Tracking Protection are enabled by default.

---

# Version Française

## Description
Firefox est un navigateur web libre et open-source développé par la Mozilla Foundation. Il utilise le moteur de rendu Gecko pour afficher les pages web, qui implémente les standards web actuels et anticipés. Firefox est connu pour sa grande personnalisation, ses fonctionnalités de confidentialité robustes et son engagement envers un web ouvert.

## Site Web / Lien
- [Site Officiel](https://www.mozilla.org/fr/firefox/new/)
- [Mozilla Developer Network (MDN)](https://developer.mozilla.org/fr/)

## Installation
```bash
# Windows (via Winget)
winget install -e --id Mozilla.Firefox

# macOS (via Homebrew)
brew install --cask firefox

# Linux (Ubuntu/Debian)
sudo apt install firefox

# Téléchargement Direct
# Visitez https://www.mozilla.org/fr/firefox/new/
```

## Commandes Utiles / Astuces
- `Raccourcis de la Barre d'Adresse` :
    - `*` + Espace : Rechercher dans les Marque-pages
    - `%` + Espace : Rechercher dans les Onglets Ouverts
    - `^` + Espace : Rechercher dans l'Historique
- `Ctrl + Maj + P` : Ouvrir une Fenêtre Privée
- `Ctrl + Maj + M` : Basculer le Mode Vue Adaptative (pour les développeurs)
- `Maj + F5` ou `Ctrl + Maj + R` : Rechargement Forcé (vider le cache de la page)
- `about:config` : Accéder aux paramètres de configuration avancés (à utiliser avec prudence).
- `about:profiles` : Gérer les profils Firefox.

## Configuration
- **Paramètres** : Accessible via `about:preferences` ou le menu hamburger.
- **Extensions** : Gérer les modules complémentaires via `about:addons` (`Ctrl + Maj + A`).
- **user.js** : Un fichier de configuration qui peut être utilisé pour renforcer les paramètres de confidentialité de Firefox (par exemple, [Arkenfox](https://github.com/arkenfox/user.js)).
- **Sync** : Utilisez un Compte Firefox pour synchroniser vos marque-pages, historique, mots de passe et onglets ouverts entre vos appareils.

## Notes
- Firefox est l'un des rares navigateurs majeurs non basé sur Chromium, contribuant à maintenir la diversité sur le marché des moteurs de navigateur.
- Il dispose d'excellents outils de développement (DevTools), en particulier pour le débogage de CSS Grid et Flexbox.
- Les fonctionnalités de confidentialité comme la Protection Renforcée contre le Pistage sont activées par défaut.
