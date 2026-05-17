# Orchestration d'une Application de CPU Scheduling avec Docker Compose

Ce projet présente la conception, la conteneurisation et l'orchestration multi-conteneurs d'une application de simulation des algorithmes d'ordonnancement du processeur (CPU Scheduling).

## 👥 Équipe du Projet
* **sidelemine elghadi**
* **ahmed bechir**
* **tfeylouhe ahmedou**

**Encadré par :** Dr. EL BENANY  

---

## 🛠️ Architecture du Système
L'application repose sur une architecture micro-services composée de deux conteneurs principaux :
1. **web_app** : Le serveur Flask (Python 3.9) qui gère la logique de simulation des algorithmes (FIFO, SRTF).
2. **database** : Le moteur de base de données MySQL 8.0 pour la persistance des données et de l'historique d'ordonnancement.

---

## 🚀 Prerequis
Pour exécuter ce projet sur votre machine locale, vous devez avoir installé :
* **Windows Subsystem for Linux (WSL 2)** (Ubuntu)
* **Docker Desktop** (connecté à votre environnement WSL 2)

---

## 💻 Instructions de Déploiement

Suivez ces étapes simples pour lancer l'architecture complète via votre terminal WSL :

1. **Cloner ou télécharger le dépôt** dans votre environnement WSL.
2. **Lancer l'orchestration** avec la commande suivante :
   ```bash
   sudo docker-compose up --build
