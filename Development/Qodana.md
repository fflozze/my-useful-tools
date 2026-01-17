# Qodana (JetBrains)

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Qodana is JetBrains' static analysis engine (creators of IntelliJ and PyCharm) ported to the cloud or your deployment pipelines. It scans your code to detect potential bugs, security vulnerabilities, and technical debt. It's like having the "intelligence" of a JetBrains IDE automatically checking your project with every change.

**Domain**: Code Quality (CI/CD)

## Website / Link
- [Official Website](https://www.jetbrains.com/qodana/)

## Installation
Qodana can be integrated into various CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins, etc.) or run locally using Docker.

```bash
# Example: Run locally with Docker
docker run --rm -it -p 8080:8080 -v $(pwd):/data/project jetbrains/qodana-js
```

## Useful Commands / Tips
- **Local Analysis**: Run Qodana locally before pushing code to catch issues early.
- **Cloud Integration**: Connect with Qodana Cloud for historical analysis and team-wide reports.

## Configuration
- `qodana.yaml`: Configuration file at the root of your project to customize inspections, exclude paths, and set failure conditions.

## Notes
- Helps maintain code quality standards across a team.
- Offers a visual report that looks very similar to the problems view in JetBrains IDEs.

---

# Version Française

## Description
C'est le moteur d'analyse statique de JetBrains (les créateurs d'IntelliJ et PyCharm) porté dans le cloud ou dans vos pipelines de déploiement. Il scanne votre code pour détecter les bugs potentiels, les failles de sécurité et les dettes techniques. C'est comme avoir "l'intelligence" d'un IDE JetBrains qui vérifie votre projet automatiquement à chaque modification.

**Domaine** : Qualité du code (CI/CD)

## Site Web / Lien
- [Site Officiel](https://www.jetbrains.com/qodana/)

## Installation
Qodana peut être intégré dans divers pipelines CI/CD (GitHub Actions, GitLab CI, Jenkins, etc.) ou exécuté localement via Docker.

```bash
# Exemple : Exécuter localement avec Docker
docker run --rm -it -p 8080:8080 -v $(pwd):/data/project jetbrains/qodana-js
```

## Commandes Utiles / Astuces
- **Analyse locale** : Exécutez Qodana localement avant de pousser votre code pour détecter les problèmes tôt.
- **Intégration Cloud** : Connectez-vous à Qodana Cloud pour des analyses historiques et des rapports d'équipe.

## Configuration
- `qodana.yaml` : Fichier de configuration à la racine de votre projet pour personnaliser les inspections, exclure des chemins et définir les conditions d'échec.

## Notes
- Aide à maintenir les standards de qualité du code au sein d'une équipe.
- Offre un rapport visuel très similaire à la vue des problèmes dans les IDE JetBrains.
