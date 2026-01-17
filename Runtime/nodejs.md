# Node.js

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Node.js is an open-source, cross-platform JavaScript runtime environment that executes JavaScript code outside a web browser. Built on Chrome's V8 JavaScript engine, it uses an event-driven, non-blocking I/O model that makes it lightweight and efficient. It is widely used for server-side scripting, building scalable network applications, and as a runtime for modern web development tools.

## Website / Link
- [Official Website](https://nodejs.org/)
- [Repository](https://github.com/nodejs/node)
- [NPM Registry](https://www.npmjs.com/)

## Installation
```bash
# Download and install from official website (Windows/macOS)
# https://nodejs.org/en/download/

# Using NVM (Node Version Manager) - Recommended for managing multiple versions
nvm install node # Installs the latest version
nvm install --lts # Installs the latest LTS version
nvm use <version>
```

## Useful Commands / Tips
- `node -v`: Check the installed Node.js version.
- `npm -v`: Check the installed NPM version.
- `node file.js`: Run a JavaScript file using Node.js.
- `node`: Enter the Node.js REPL (interactive shell).
- `npm init -y`: Initialize a new project with a default `package.json`.
- `npm install <package>`: Install a package locally.
- `npm install -g <package>`: Install a package globally.
- `npm run <script>`: Run a script defined in `package.json`.

## Configuration
- **package.json**: The core configuration file for any Node.js project. It lists dependencies, scripts, version, and other metadata.
- **.npmrc**: Configuration file for npm (e.g., setting registry, auth tokens).
- **Environment Variables**: Often accessed via `process.env`. Use `dotenv` package to manage them in a `.env` file.

## Notes
- Always use an LTS (Long Term Support) version for production environments to ensure stability.
- Use `nvm` (on Linux/Mac) or `nvm-windows` to manage Node versions effectively, as different projects might require different versions.
- Asynchronous programming (Promises, async/await) is fundamental in Node.js due to its single-threaded nature.

---

# Version Française

## Description
Node.js est un environnement d'exécution JavaScript open-source et multiplateforme qui exécute du code JavaScript en dehors d'un navigateur web. Construit sur le moteur JavaScript V8 de Chrome, il utilise un modèle d'E/S non bloquant et orienté événement qui le rend léger et efficace. Il est largement utilisé pour les scripts côté serveur, la création d'applications réseau évolutives et comme environnement d'exécution pour les outils de développement web modernes.

## Site Web / Lien
- [Site Officiel](https://nodejs.org/)
- [Dépôt](https://github.com/nodejs/node)
- [Registre NPM](https://www.npmjs.com/)

## Installation
```bash
# Télécharger et installer depuis le site officiel (Windows/macOS)
# https://nodejs.org/en/download/

# Utiliser NVM (Node Version Manager) - Recommandé pour gérer plusieurs versions
nvm install node # Installe la dernière version
nvm install --lts # Installe la dernière version LTS
nvm use <version>
```

## Commandes Utiles / Astuces
- `node -v`: Vérifier la version de Node.js installée.
- `npm -v`: Vérifier la version de NPM installée.
- `node file.js`: Exécuter un fichier JavaScript avec Node.js.
- `node`: Entrer dans le REPL Node.js (shell interactif).
- `npm init -y`: Initialiser un nouveau projet avec un `package.json` par défaut.
- `npm install <package>`: Installer un paquet localement.
- `npm install -g <package>`: Installer un paquet globalement.
- `npm run <script>`: Exécuter un script défini dans `package.json`.

## Configuration
- **package.json**: Le fichier de configuration central pour tout projet Node.js. Il liste les dépendances, les scripts, la version et d'autres métadonnées.
- **.npmrc**: Fichier de configuration pour npm (ex: définition du registre, jetons d'authentification).
- **Variables d'environnement**: Souvent accessibles via `process.env`. Utilisez le paquet `dotenv` pour les gérer dans un fichier `.env`.

## Notes
- Utilisez toujours une version LTS (Long Term Support) pour les environnements de production afin d'assurer la stabilité.
- Utilisez `nvm` (sur Linux/Mac) ou `nvm-windows` pour gérer efficacement les versions de Node, car différents projets peuvent nécessiter des versions différentes.
- La programmation asynchrone (Promesses, async/await) est fondamentale dans Node.js en raison de sa nature monothread.
