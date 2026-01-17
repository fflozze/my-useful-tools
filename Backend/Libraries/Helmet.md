# Helmet

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Helmet helps you secure your Express apps by setting various HTTP headers. It's not a silver bullet, but it can help! It includes middleware functions for setting security-related HTTP headers like `Content-Security-Policy`, `X-Frame-Options`, and others.

## Website / Link
- [Official Website](https://helmetjs.github.io/)
- [Repository](https://github.com/helmetjs/helmet)

## Installation
```bash
# Install helmet
npm install helmet
```

## Useful Commands / Tips
- `app.use(helmet())`: Adds all standard security headers to your responses.
- You can also use individual headers: `app.use(helmet.contentSecurityPolicy(...))`

## Configuration
- Highly configurable. You can pass an object to `helmet()` to enable/disable or configure specific headers.

## Notes
Always a good idea to include this in any production Express/Node.js application for basic security hardening.

---

# Version Française

## Description
Helmet vous aide à sécuriser vos applications Express en définissant divers en-têtes HTTP. Ce n'est pas une solution miracle, mais cela peut aider ! Il comprend des fonctions middleware pour définir des en-têtes HTTP liés à la sécurité comme `Content-Security-Policy`, `X-Frame-Options`, et autres.

## Site Web / Lien
- [Site Officiel](https://helmetjs.github.io/)
- [Dépôt](https://github.com/helmetjs/helmet)

## Installation
```bash
# Installer helmet
npm install helmet
```

## Commandes Utiles / Astuces
- `app.use(helmet())`: Ajoute tous les en-têtes de sécurité standard à vos réponses.
- Vous pouvez également utiliser des en-têtes individuels : `app.use(helmet.contentSecurityPolicy(...))`

## Configuration
- Hautement configurable. Vous pouvez passer un objet à `helmet()` pour activer/désactiver ou configurer des en-têtes spécifiques.

## Notes
Toujours une bonne idée d'inclure ceci dans toute application Express/Node.js en production pour un renforcement basique de la sécurité.
