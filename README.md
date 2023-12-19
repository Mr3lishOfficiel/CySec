![image](https://github.com/Mr3lishOfficiel/CySec/assets/152335477/43bf8212-a485-4202-a241-7e74811013ff)

# Introduction CySec
CySec est un programme en Python qui offre une interface utilisateur en ligne de commande (CLI) pour exécuter des tâches de cybersécurité offensives et défensives. Le programme utilise divers outils et commandes pour scanner, analyser et sécuriser un système.


# Fonctionnalités

Lorsque vous exécutez le programme, vous êtes accueilli par un menu principal qui vous permet de choisir entre les modes offensif et défensif, ou de quitter le programme.

## Menu Offensif (🗡️)
- Scan Simple: Utilise nmap pour effectuer un scan basique d'une adresse IP.
- Scan Vulnérabilité: Effectue un scan de vulnérabilité en utilisant des scripts nmap.
- Traceroute: Utilise nmap pour tracer la route vers une adresse IP.
- Scan Web: Utilise nikto pour scanner un serveur web sur le port 80.
- Searchploit: Permet de rechercher des exploits pour une vulnérabilité spécifique.

## Menu Défensif (🛡️)
Sécurisation de votre serveur - Méthode Complète:

- Met à jour les paquets du système.
- Installe et configure fail2ban pour bloquer les tentatives d'intrusion.
- Installe et configure UFW (Uncomplicated Firewall).
- Installe chkrootkit pour détecter les rootkits.
- Installe AIDE pour surveiller les modifications de fichiers.
- Installe ClamAV et Lynis pour la surveillance et l'analyse des vulnérabilités.
- Configure les mises à jour automatiques.
- Générer un rapport ClamAV et Lynis:

Effectue une analyse complète du système avec clamscan.
Exécute une analyse de vulnérabilité avec lynis.

## Fonctions auxiliaires

demander_approbation: Une fonction qui demande l'approbation de l'utilisateur avant d'exécuter certaines tâches.

## Comment cela aide-t-il ?

- Menu Offensif: Il permet aux utilisateurs de tester et d'évaluer la sécurité de leurs systèmes ou réseaux.
- Menu Défensif: Il fournit des outils pour sécuriser activement un système contre les menaces courantes.
- Facilité d'utilisation: Le programme offre une interface conviviale pour accéder à divers outils de cybersécurité sans avoir à se souvenir de commandes complexes.

En résumé, OPM est un outil polyvalent qui vise à éduquer, tester et protéger les utilisateurs contre les menaces de cybersécurité.
