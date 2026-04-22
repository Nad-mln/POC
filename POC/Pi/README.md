# Raspberry Pi

Ce dossier contient la partie Raspberry Pi du projet.

- `tkinter_gpio_app.py` : interface Tkinter principale permettant d'envoyer altitude et orientation en GET et en POST.
- `av.py` : script complémentaire de gestion de boutons GPIO physiques avec `gpiozero`.

## Lancer l'application Tkinter
```bash
python tkinter_gpio_app.py
```

## Dépendances
```bash
pip install requests
```

Sur Raspberry Pi, pour les GPIO :
```bash
pip install gpiozero
```
