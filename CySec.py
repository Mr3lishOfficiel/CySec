import os
import subprocess
import time


# Fonctions d'impression en couleur
def white(text):
    print("\033[37m" + text + "\033[0m")


def red(text):
    print("\033[31m" + text + "\033[0m")


def green(text):
    print("\033[92m" + text + "\033[0m")


# Efface l'écran
os.system("clear")

# Affichage du texte stylisé
print("""
 ██████╗██╗   ██╗███████╗███████╗ ██████╗
██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
██║      ╚████╔╝ ███████╗█████╗  ██║     
██║       ╚██╔╝  ╚════██║██╔══╝  ██║     
╚██████╗   ██║   ███████║███████╗╚██████╗
 ╚═════╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝
""")

# Menu principal
while True:
    os.system("clear")
    print("********************************************")
    print("                Menu Principal              ")
    print("********************************************")
    print(" ")
    print("1. Menu Offensif" + " " + "(🗡️)")
    print("2. Menu Défensif" + " " + "(🛡️)")
    print(" ")
    print("3. Quitter")
    print(" ")

    choice = input("Votre choix : ")

    if choice == "1":
        # Menu Offensif
        while True:
            os.system("clear")
            print("""
 ██████╗██╗   ██╗███████╗███████╗ ██████╗
██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
██║      ╚████╔╝ ███████╗█████╗  ██║     
██║       ╚██╔╝  ╚════██║██╔══╝  ██║     
╚██████╗   ██║   ███████║███████╗╚██████╗
 ╚═════╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝
""")
            print("********************************************")
            print("                Menu Offensif              ")
            print("********************************************")
            print(" ")
            print("1.(🗡️) - Scan Simple")
            print("2.(🗡️) - Scan Vulnérabilité")
            print("3.(🗡️) - Traceroute")
            print("4.(🗡️) - Scan Web")
            print("5.(🗡️) - Searchploit")
            print(" ")
            print("6. Retour au menu principal")
            print(" ")

            choice_offensive = input("Votre choix : ")

            if choice_offensive == "1":
                # Scan Simple
                s = input("Quelle IP voulez-vous analyser ? (IP uniquement) : ")
                print("")
                subprocess.run(["nmap", "-v", s])

            elif choice_offensive == "2":
                # Scan Vulnérabilité
                s = input("Quelle IP voulez-vous analyser ? (IP uniquement) : ")
                print("")
                subprocess.run(["nmap", "-v", "--script", "default", s])

            elif choice_offensive == "3":
                # Traceroute
                s = input("Quelle IP voulez-vous analyser ? (IP uniquement) : ")
                print("")
                subprocess.run(["nmap", "-sn", "-traceroute", s])

            elif choice_offensive == "4":
                # Scan Web
                s = input("Quelle IP voulez-vous analyser ? (IP uniquement) : ")
                print("")
                subprocess.run(["nikto", "-h", s, "-p", "80"])

            elif choice_offensive == "5":
                # Searchploit
                vuln = input("Quelle vulnérabilité t'interesse ? : ")
                print("")
                subprocess.run(["searchsploit", vuln])

            elif choice_offensive == "6":
                # Retour au menu principal
                break

            input("Appuyez sur Entrée pour continuer...")

    elif choice == "2":
        # Menu Défensif
        while True:
            os.system("clear")
            print("""
 ██████╗██╗   ██╗███████╗███████╗ ██████╗
██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
██║      ╚████╔╝ ███████╗█████╗  ██║     
██║       ╚██╔╝  ╚════██║██╔══╝  ██║     
╚██████╗   ██║   ███████║███████╗╚██████╗
 ╚═════╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝
""")
            print("********************************************")
            print("                Menu Défensif              ")
            print("********************************************")
            print("")
            print("1.(🛡️) - Sécurisation de votre serveur - Méthode Complète")
            print("2.(🛡️) - Générer un rapport ClamAV et Lynis")
            print("")
            print("2. Retour au menu principal")
            print("")

            choice_defensive = input("Votre choix : ")

            if choice_defensive == "1":
                import subprocess


                # Fonction pour demander l'approbation de l'utilisateur
                def demander_approbation(message):
                    print(message)
                    while True:
                        reponse = input("Voulez-vous continuer ? (o/n) ")
                        if reponse.lower() == "o":
                            return True
                        elif reponse.lower() == "n":
                            return False


                # Mise à jour des paquets
                if demander_approbation("Voulez-vous mettre à jour les paquets du système ?"):
                    subprocess.run(["apt-get", "update"])
                    subprocess.run(["apt-get", "upgrade", "-y"])
                    print("Paquets mis à jour avec succès.")

                # Installation de fail2ban
                if demander_approbation("Voulez-vous installer Fail2ban pour bloquer les tentatives d'intrusion ?"):
                    subprocess.run(["apt-get", "install", "fail2ban", "-y"])
                    print("Fail2ban installé avec succès.")

                    # Configuration de fail2ban
                    fail2ban_config = """
                [sshd]
                enabled = true
                port = ssh
                logpath = %(sshd_log)s
                maxretry = 3
                """
                    with open('/etc/fail2ban/jail.local', 'a') as f:
                        f.write(fail2ban_config)

                    # Redémarrage de fail2ban
                    subprocess.run(["service", "fail2ban", "restart"])
                    print("Fail2ban configuré et redémarré.")

                # Installation de UFW et configuration du pare-feu
                if demander_approbation(
                        "Voulez-vous installer UFW et configurer le pare-feu pour autoriser SSH, HTTP et HTTPS ?"):
                    subprocess.run(["apt-get", "install", "ufw", "-y"])
                    print("UFW installé avec succès.")

                    # Autorisation de l'accès à SSH, HTTP et HTTPS
                    subprocess.run(["ufw", "allow", "22/tcp"])
                    subprocess.run(["ufw", "allow", "80/tcp"])
                    subprocess.run(["ufw", "allow", "443/tcp"])

                    # Activation du pare-feu
                    subprocess.run(["ufw", "enable"])
                    print("Pare-feu configuré et activé.")

                # Installation de chkrootkit
                if demander_approbation("Voulez-vous installer chkrootkit pour vérifier si le système est compromis ?"):
                    subprocess.run(["apt-get", "install", "chkrootkit", "-y"])
                    print("chkrootkit installé avec succès.")

                # Installation de AIDE
                if demander_approbation("Voulez-vous installer AIDE pour détecter les modifications de fichiers ?"):
                    subprocess.run(["apt-get", "install", "aide", "-y"])
                    print("AIDE installé avec succès.")

                    # Configuration de AIDE pour vérifier les fichiers tous les jours
                    aide_config = "daily_aide_enable=1\n"
                    with open('/etc/default/aide', 'a') as f:
                        f.write(aide_config)

                    # Redémarrage de AIDE
                    subprocess.run(["service", "aide", "restart"])
                    print("AIDE configuré et redémarré.")

                # Installation d'un antivirus (ClamAV)
                if demander_approbation("Voulez-vous installer ClamAV pour surveiller les logiciels malveillants ?"):
                    subprocess.run(["apt-get", "install", "clamav", "clamav-daemon", "-y"])
                    print("ClamAV installé avec succès.")

                # Analyse de vulnérabilités (Lynis)
                if demander_approbation(
                        "Voulez-vous installer Lynis pour effectuer une analyse de vulnérabilités du serveur ?"):
                    subprocess.run(["apt-get", "install", "lynis", "-y"])
                    print("Lynis installé avec succès.")

                    # Exécution de l'analyse
                    subprocess.run(["lynis", "audit", "system"])
                    print(
                        "Analyse de vulnérabilités effectuée. Les résultats sont disponibles dans /var/log/lynis.log.")

                # Mises à jour automatiques
                if demander_approbation("Voulez-vous configurer les mises à jour automatiques du système ?"):
                    with open("/etc/apt/apt.conf.d/10periodic", "w") as f:
                        f.write('APT::Periodic::Update-Package-Lists "1";\n')
                        f.write('APT::Periodic::Download-Upgradeable-Packages "1";\n')
                        f.write('APT::Periodic::AutocleanInterval "7";\n')
                        f.write('APT::Periodic::Unattended-Upgrade "1";\n')
                    print("Mises à jour automatiques configurées.")

                # Autres mesures de sécurité peuvent être ajoutées en fonction des besoins, telles que la surveillance des journaux, la gestion des certificats, etc.

                print("Le script de sécurisation du serveur est terminé.")



            elif choice_defensive == "2":

                # Générer un rapport ClamAV et Lynis

                print("Génération du rapport ClamAV...")

                subprocess.run(["clamscan", "-r", "/"])  # Analyse complète du système

                print("Rapport ClamAV généré. Vous pouvez trouver les résultats dans /var/log/clamav/clamscan.log.")

                print("Exécution de l'analyse de vulnérabilité Lynis...")

                subprocess.run(["lynis", "audit", "system"])

                print("Analyse de vulnérabilité effectuée. Les résultats sont disponibles dans /var/log/lynis.log.")

                print("Rapports générés avec succès.")


            elif choice_defensive == "3":

                # Retour au menu principal

                break

            input("Appuyez sur Entrée pour continuer...")

    elif choice == "3":
        # Quitter
        print("Merci d'avoir utilisé OPM !")
        break

    input("Appuyez sur Entrée pour continuer...")
