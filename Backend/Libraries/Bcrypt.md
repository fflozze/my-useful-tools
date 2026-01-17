# Bcrypt

> [!TIP]
> [Passer à la version française](#version-française)

## Description
A library to help you hash passwords. `bcrypt` is a password-hashing function designed by Niels Provos and David Mazières. This package is a native Node.js implementation (C++ binding) which makes it very fast, but requires compilation.

## Website / Link
- [Repository](https://github.com/kelektiv/node.bcrypt.js)
- [NPM](https://www.npmjs.com/package/bcrypt)

## Installation
```bash
# Install bcrypt
npm install bcrypt
```

## Useful Commands / Tips
- `bcrypt.hash(password, saltRounds)`: Asynchronously generates a hash for the given string.
- `bcrypt.compare(password, hash)`: Asynchronously compares the given data against the given hash.

## Configuration
- No specific configuration file, usages are configured via function arguments (e.g., salt rounds).

## Notes
Dependencies on C++ compilation can sometimes cause issues in certain environments (like some Docker containers or Windows setups without build tools), in which case `bcryptjs` is a good alternative.

---

# Version Française

## Description
Une bibliothèque pour vous aider à hacher les mots de passe. `bcrypt` est une fonction de hachage de mot de passe conçue par Niels Provos et David Mazières. Ce paquet est une implémentation native Node.js (liaison C++) ce qui le rend très rapide, mais nécessite une compilation.

## Site Web / Lien
- [Dépôt](https://github.com/kelektiv/node.bcrypt.js)
- [NPM](https://www.npmjs.com/package/bcrypt)

## Installation
```bash
# Installer bcrypt
npm install bcrypt
```

## Commandes Utiles / Astuces
- `bcrypt.hash(password, saltRounds)`: Génère de manière asynchrone un hachage pour la chaîne donnée.
- `bcrypt.compare(password, hash)`: Compare de manière asynchrone les données fournies avec le hachage donné.

## Configuration
- Pas de fichier de configuration spécifique, les utilisations sont configurées via les arguments de fonction (par exemple, les tours de sel).

## Notes
Les dépendances à la compilation C++ peuvent parfois causer des problèmes dans certains environnements (comme certains conteneurs Docker ou des configurations Windows sans outils de build), auquel cas `bcryptjs` est une bonne alternative.
