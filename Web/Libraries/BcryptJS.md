# BcryptJS

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Optimized bcrypt in JavaScript with zero dependencies. Compatible to the C++ binding `bcrypt` binding on node.js and also working in the browser. It is slightly slower than the native C++ version but much easier to install and deploy since it doesn't require compilation.

## Website / Link
- [Repository](https://github.com/dcodeIO/bcrypt.js)
- [NPM](https://www.npmjs.com/package/bcryptjs)

## Installation
```bash
# Install bcryptjs
npm install bcryptjs
```

## Useful Commands / Tips
- API is compatible with `bcrypt`.
- `bcrypt.hash(password, salt)`: Hashes a password.
- `bcrypt.compare(password, hash)`: Verifies a password.

## Configuration
- No configuration file needed.

## Notes
Perfect for environments where you cannot or do not want to install build tools (like python, make, g++) for native modules.

---

# Version Française

## Description
Bcrypt optimisé en JavaScript sans aucune dépendance. Compatible avec la liaison C++ `bcrypt` sur node.js et fonctionne également dans le navigateur. Il est légèrement plus lent que la version native C++ mais beaucoup plus facile à installer et à déployer car il ne nécessite pas de compilation.

## Site Web / Lien
- [Dépôt](https://github.com/dcodeIO/bcrypt.js)
- [NPM](https://www.npmjs.com/package/bcryptjs)

## Installation
```bash
# Installer bcryptjs
npm install bcryptjs
```

## Commandes Utiles / Astuces
- L'API est compatible avec `bcrypt`.
- `bcrypt.hash(password, salt)`: Hache un mot de passe.
- `bcrypt.compare(password, hash)`: Vérifie un mot de passe.

## Configuration
- Aucun fichier de configuration nécessaire.

## Notes
Parfait pour les environnements où vous ne pouvez pas ou ne voulez pas installer d'outils de build (comme python, make, g++) pour les modules natifs.
