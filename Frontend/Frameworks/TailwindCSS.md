# TailwindCSS

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Tailwind CSS is an open-source, utility-first CSS framework designed for rapidly building modern websites directly within HTML. Unlike traditional CSS frameworks that offer predefined components, Tailwind provides a comprehensive set of "utility" classes (e.g., `flex`, `pt-4`, `text-center`) that can be combined to create unique designs without writing custom CSS.

## Website / Link
- [Official Website](https://tailwindcss.com/)
- [Repository](https://github.com/tailwindlabs/tailwindcss)

## Installation
```bash
# Install Tailwind CSS via npm
npm install -D tailwindcss postcss autoprefixer
# Initialize configuration
npx tailwindcss init
```

## Useful Commands / Tips
- `npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch`: Start the Tailwind CLI build process in watch mode.

## Configuration
- `tailwind.config.js`: Configuration file to customize the design system, colors, fonts, and plugins.
- `postcss.config.js`: Configuration for PostCSS, typically requires `tailwindcss` and `autoprefixer`.

## Notes
Tailwind drastically speeds up the styling process by keeping you in the HTML, avoiding context switching to CSS files.

---

# Version Française

## Description
Tailwind CSS est un framework CSS open-source et "utility-first" conçu pour construire rapidement des sites web modernes directement dans le HTML. Contrairement aux frameworks CSS traditionnels qui offrent des composants prédéfinis, Tailwind fournit un ensemble complet de classes "utilitaires" (par exemple, `flex`, `pt-4`, `text-center`) qui peuvent être combinées pour créer des designs uniques sans écrire de CSS personnalisé.

## Site Web / Lien
- [Site Officiel](https://tailwindcss.com/)
- [Dépôt](https://github.com/tailwindlabs/tailwindcss)

## Installation
```bash
# Installer Tailwind CSS via npm
npm install -D tailwindcss postcss autoprefixer
# Initialiser la configuration
npx tailwindcss init
```

## Commandes Utiles / Astuces
- `npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch`: Démarre le processus de build CLI de Tailwind en mode surveillance (watch).

## Configuration
- `tailwind.config.js`: Fichier de configuration pour personnaliser le système de design, les couleurs, les polices et les plugins.
- `postcss.config.js`: Configuration pour PostCSS, nécessite généralement `tailwindcss` et `autoprefixer`.

## Notes
Tailwind accélère considérablement le processus de stylisme en vous gardant dans le HTML, évitant les changements de contexte vers les fichiers CSS.
