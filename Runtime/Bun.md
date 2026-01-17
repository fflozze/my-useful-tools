# Bun

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Bun is an all-in-one toolkit for JavaScript and TypeScript apps. It ships as a single executable called `bun`. It includes a bundler, test runner, and native npm package manager. It is designed to be a drop-in replacement for Node.js, but faster.

## Website / Link
- [Official Website](https://bun.sh/)
- [Repository](https://github.com/oven-sh/bun)

## Installation
```bash
# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1 | iex"

# macOS / Linux
curl -fsSL https://bun.sh/install | bash

# npm
npm install -g bun
```

## Useful Commands / Tips
- `bun run start`: Run the `start` script in `package.json`.
- `bun install`: Install dependencies (faster than npm/yarn).
- `bun test`: Run tests with the built-in test runner.
- `bunx <package>`: Run a package executable (similar to `npx`).
- `bun init`: Initialize a new project.

## Configuration
- `bunfig.toml`: Configuration file for Bun (optional).

## Notes
- Bun is incredibly fast for installing packages and starting up projects.
- It has built-in support for TypeScript, JSX, and environmental variables (`.env`).

---

# Version Française

## Description
Bun est une boîte à outils tout-en-un pour les applications JavaScript et TypeScript. Il est livré sous la forme d'un exécutable unique appelé `bun`. Il comprend un bundler, un exécuteur de tests et un gestionnaire de paquets npm natif. Il est conçu pour être un remplacement direct de Node.js, mais en plus rapide.

## Site Web / Lien
- [Site Officiel](https://bun.sh/)
- [Dépôt](https://github.com/oven-sh/bun)

## Installation
```bash
# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1 | iex"

# macOS / Linux
curl -fsSL https://bun.sh/install | bash

# npm
npm install -g bun
```

## Commandes Utiles / Astuces
- `bun run start`: Exécuter le script `start` dans `package.json`.
- `bun install`: Installer les dépendances (plus rapide que npm/yarn).
- `bun test`: Lancer les tests avec l'exécuteur de tests intégré.
- `bunx <package>`: Exécuter un exécutable de paquet (similaire à `npx`).
- `bun init`: Initialiser un nouveau projet.

## Configuration
- `bunfig.toml`: Fichier de configuration pour Bun (optionnel).

## Notes
- Bun est incroyablement rapide pour installer des paquets et démarrer des projets.
- Il a un support intégré pour TypeScript, JSX et les variables d'environnement (`.env`).
