# React-DOM

> [!TIP]
> [Passer à la version française](#version-française)

## Description
This package serves as the entry point to the DOM and server renderers for React. It is intended to be paired with the core React package. `react-dom` provides the specific methods needed to render your React components into the DOM (e.g., `createRoot`, `hydrateRoot`).

## Website / Link
- [Official Website](https://react.dev/)
- [Repository](https://github.com/facebook/react) (Monorepo includes react-dom)

## Installation
```bash
# Install React DOM
npm install react-dom
```

## Useful Commands / Tips
- `ReactDOM.createRoot(container)`: Creates a React root for the supplied container and returns the root.
- `root.render(element)`: Renders a React element into the root.

## Configuration
- Typically configured alongside React in the entry file of your application (e.g., `index.js`, `main.tsx`).

## Notes
Since React 18, `ReactDOM.render` has been replaced by `createRoot` for better performance and concurrent mode support.

---

# Version Française

## Description
Ce paquet sert de point d'entrée vers le DOM et les rendus serveur pour React. Il est destiné à être jumelé avec le paquet principal React. `react-dom` fournit les méthodes spécifiques nécessaires pour rendre vos composants React dans le DOM (par exemple, `createRoot`, `hydrateRoot`).

## Site Web / Lien
- [Site Officiel](https://react.dev/)
- [Dépôt](https://github.com/facebook/react) (Le monorepo inclut react-dom)

## Installation
```bash
# Installer React DOM
npm install react-dom
```

## Commandes Utiles / Astuces
- `ReactDOM.createRoot(container)`: Crée une racine React pour le conteneur fourni et renvoie la racine.
- `root.render(element)`: Rend un élément React dans la racine.

## Configuration
- Généralement configuré aux côtés de React dans le fichier d'entrée de votre application (par exemple, `index.js`, `main.tsx`).

## Notes
Depuis React 18, `ReactDOM.render` a été remplacé par `createRoot` pour de meilleures performances et la prise en charge du mode concurrent.
