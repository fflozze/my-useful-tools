# ASR Whisper (OpenAI)

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

## Website / Link
- [Official Repository](https://github.com/openai/whisper)
- [Paper](https://arxiv.org/abs/2212.04356)

## Installation
```bash
# Install ffmpeg first (required)
# on Ubuntu
sudo apt update && sudo apt install ffmpeg
# on MacOS using Homebrew
brew install ffmpeg
# on Windows using Chocolatey
choco install ffmpeg

# Install Whisper
pip install -U openai-whisper

# Or force install from GitHub
pip install git+https://github.com/openai/whisper.git 
```

## Useful Commands / Tips
- `whisper audio.mp3`: Transcribe audio.mp3 using the default model.
- `whisper audio.mp3 --model medium`: Use the medium model for better accuracy (requires more VRAM).
- `whisper audio.wav --language French`: Force the language to French.
- `whisper audio.wav --task translate`: Translate the audio to English.

## Configuration
Models available: `tiny`, `base`, `small`, `medium`, `large`.
The models are stored in `~/.cache/whisper`.

## Notes
- It requires Python 3.8-3.11 and a recent version of PyTorch.
- GPU is highly recommended for reasonable processing times.

---

# Version Française

## Description
Whisper est un modèle de reconnaissance vocale polyvalent. Il est entraîné sur un vaste ensemble de données audio diverses et est également un modèle multitâche capable d'effectuer la reconnaissance vocale multilingue, la traduction de la parole et l'identification de la langue.

## Site Web / Lien
- [Dépôt Officiel](https://github.com/openai/whisper)
- [Article de recherche](https://arxiv.org/abs/2212.04356)

## Installation
```bash
# Installez d'abord ffmpeg (requis)
# sur Ubuntu
sudo apt update && sudo apt install ffmpeg
# sur MacOS avec Homebrew
brew install ffmpeg
# sur Windows avec Chocolatey
choco install ffmpeg

# Installer Whisper
pip install -U openai-whisper

# Ou forcer l'installation depuis GitHub
pip install git+https://github.com/openai/whisper.git 
```

## Commandes Utiles / Astuces
- `whisper audio.mp3` : Transcrire audio.mp3 en utilisant le modèle par défaut.
- `whisper audio.mp3 --model medium` : Utiliser le modèle medium pour une meilleure précision (nécessite plus de VRAM).
- `whisper audio.wav --language French` : Forcer la langue en français.
- `whisper audio.wav --task translate` : Traduire l'audio en anglais.

## Configuration
Modèles disponibles : `tiny`, `base`, `small`, `medium`, `large`.
Les modèles sont stockés dans `~/.cache/whisper`.

## Notes
- Nécessite Python 3.8-3.11 et une version récente de PyTorch.
- Un GPU est fortement recommandé pour des temps de traitement raisonnables.
