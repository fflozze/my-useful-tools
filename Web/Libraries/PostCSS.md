# PostCSS

> [!TIP]
> [Passer à la version française](#version-française)

## Description
PostCSS is a tool for transforming CSS with JavaScript plugins. It provides a parser, a plugin system, and a stringifier. It allows you to use modern CSS features today, lint your CSS, and more. Common plugins include Tailwind CSS and Autoprefixer.

## Website / Link
- [Official Website](https://postcss.org/)
- [Repository](https://github.com/postcss/postcss)

## Installation
```bash
# Install PostCSS
npm install postcss
```

## Useful Commands / Tips
- PostCSS is rarely run directly via CLI in modern web dev; it's usually integrated into build tools like Vite, Webpack, or Next.js.

## Configuration
- `postcss.config.js`: The standard configuration file where you list your plugins.
  ```javascript
  module.exports = {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  }
  ```

## Notes
PostCSS is the engine that powers Tailwind CSS. It's incredibly flexible due to its plugin architecture.

---

# Version Française

## Description
PostCSS est un outil pour transformer le CSS avec des plugins JavaScript. Il fournit un analyseur, un système de plugins et un stringifier. Il vous permet d'utiliser des fonctionnalités CSS modernes dès aujourd'hui, de linter votre CSS, et plus encore. Les plugins courants incluent Tailwind CSS et Autoprefixer.

## Site Web / Lien
- [Site Officiel](https://postcss.org/)
- [Dépôt](https://github.com/postcss/postcss)

## Installation
```bash
# Installer PostCSS
npm install postcss
```

## Commandes Utiles / Astuces
- PostCSS est rarement exécuté directement via CLI dans le développement web moderne ; il est généralement intégré dans des outils de build comme Vite, Webpack ou Next.js.

## Configuration
- `postcss.config.js`: Le fichier de configuration standard où vous listez vos plugins.
  ```javascript
  module.exports = {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  }
  ```

## Notes
PostCSS est le moteur qui propulse Tailwind CSS. Il est incroyablement flexible grâce à son architecture de plugins.
