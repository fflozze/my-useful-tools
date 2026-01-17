# react-i18next

> [!TIP]
> [Passer à la version française](#version-française)

## Description
react-i18next is a powerful internationalization (i18n) framework for React and React Native which is based on i18next. It provides a complete solution for translating your application, handling pluralization, formatting dates/numbers, and switching languages dynamically. It is designed to be flexible and easy to use with hooks and components.

## Website / Link
- [Official Website](https://react.i18next.com/)
- [Repository](https://github.com/i18next/react-i18next)
- [i18next Documentation](https://www.i18next.com/)

## Installation
```bash
# Install react-i18next and i18next (core library)
npm install react-i18next i18next --save

# If you need to load translations from backend/files
npm install i18next-http-backend
# If you want to detect user language
npm install i18next-browser-languagedetector
```

## Useful Commands / Tips
- `useTranslation Hook`: The most common way to translate content working with functional components.
  ```javascript
  const { t, i18n } = useTranslation();
  // ...
  <h1>{t('Welcome to React')}</h1>
  ```
- `Trans Component`: Useful for robust interpolation and integrated react components.
- `i18n.changeLanguage('fr')`: Function to switch the active language dynamically.
- `Interpolation`: `t('key', { variable: 'value' })` allows passing dynamic values to translations.

## Configuration
Typical configuration in an `i18n.js` file:
```javascript
import i18n from "i18next";
import { initReactI18next } from "react-i18next";

i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    resources: {
      en: { translation: { "Welcome": "Welcome to React" } },
      fr: { translation: { "Welcome": "Bienvenue à React" } }
    },
    lng: "en", 
    fallbackLng: "en",
    interpolation: { escapeValue: false }
  });

export default i18n;
```

## Notes
- It's highly recommended to separate translation files (e.g., JSON files) for better maintainability.
- `i18next` ecosystem is huge, check for plugins if you have specific needs (like localstorage caching).

---

# Version Française

## Description
react-i18next est un framework d'internationalisation (i18n) puissant pour React et React Native, basé sur i18next. Il fournit une solution complète pour traduire votre application, gérer la pluralisation, le formatage des dates/nombres, et changer de langue dynamiquement. Il est conçu pour être flexible et facile à utiliser avec des hooks et des composants.

## Site Web / Lien
- [Site Officiel](https://react.i18next.com/)
- [Dépôt](https://github.com/i18next/react-i18next)
- [Documentation i18next](https://www.i18next.com/)

## Installation
```bash
# Installer react-i18next et i18next (bibliothèque principale)
npm install react-i18next i18next --save

# Pour charger les traductions depuis un backend/fichiers
npm install i18next-http-backend
# Pour détecter la langue de l'utilisateur
npm install i18next-browser-languagedetector
```

## Commandes Utiles / Astuces
- `Hook useTranslation`: La méthode la plus courante pour traduire du contenu avec des composants fonctionnels.
  ```javascript
  const { t, i18n } = useTranslation();
  // ...
  <h1>{t('Welcome to React')}</h1>
  ```
- `Composant Trans`: Utile pour une interpolation robuste et l'intégration de composants React.
- `i18n.changeLanguage('fr')`: Fonction pour changer la langue active dynamiquement.
- `Interpolation`: `t('cle', { variable: 'valeur' })` permet de passer des valeurs dynamiques aux traductions.

## Configuration
Configuration typique dans un fichier `i18n.js`:
```javascript
import i18n from "i18next";
import { initReactI18next } from "react-i18next";

i18n
  .use(initReactI18next) // passe i18n à react-i18next
  .init({
    resources: {
      en: { translation: { "Welcome": "Welcome to React" } },
      fr: { translation: { "Welcome": "Bienvenue à React" } }
    },
    lng: "en", 
    fallbackLng: "en",
    interpolation: { escapeValue: false }
  });

export default i18n;
```

## Notes
- Il est fortement recommandé de séparer les fichiers de traduction (ex: fichiers JSON) pour une meilleure maintenabilité.
- L'écosystème `i18next` est vaste, vérifiez les plugins si vous avez des besoins spécifiques (comme la mise en cache localstorage).
