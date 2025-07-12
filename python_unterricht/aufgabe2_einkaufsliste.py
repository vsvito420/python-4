#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe 2: Einkaufsliste

Schreibe ein Programm, das:
1. Eine Einkaufsliste als Dictionary verwaltet (Artikel: Menge)
2. Artikel hinzufügen und entfernen kann
3. Die Liste in eine Textdatei speichert
4. Die Liste aus der Datei laden kann

Beispiel-Dictionary:
{
    "Äpfel": "2 kg",
    "Milch": "1 Liter",
    "Brot": "2 Stück",
    "Käse": "500g"
}
"""


def einkaufsliste_erstellen():
    """
    Erstellt eine neue Einkaufsliste
    """
    print("=== Neue Einkaufsliste erstellen ===")

    # TODO: Erstelle ein leeres Dictionary für die Einkaufsliste
    einkaufsliste = {
        # Deine Lösung hier
    }

    # TODO: Füge einige Beispiel-Artikel hinzu
    # Beispiel: einkaufsliste["Äpfel"] = "2 kg"
    # Deine Lösung hier

    print("Einkaufsliste erstellt:")
    einkaufsliste_anzeigen(einkaufsliste)

    return einkaufsliste


def artikel_hinzufuegen(einkaufsliste):
    """
    Fügt einen Artikel zur Einkaufsliste hinzu
    """
    print("\n=== Artikel hinzufügen ===")

    # TODO: Frage Benutzer nach Artikel und Menge
    # Tipp: Verwende input() Funktionen
    artikel = ""  # Deine Lösung hier
    menge = ""    # Deine Lösung hier

    # TODO: Füge Artikel zur Liste hinzu
    # Deine Lösung hier

    print(f"'{artikel}' wurde zur Einkaufsliste hinzugefügt!")


def artikel_entfernen(einkaufsliste):
    """
    Entfernt einen Artikel aus der Einkaufsliste
    """
    print("\n=== Artikel entfernen ===")

    if not einkaufsliste:
        print("Die Einkaufsliste ist leer!")
        return

    einkaufsliste_anzeigen(einkaufsliste)

    # TODO: Frage Benutzer nach dem zu entfernenden Artikel
    artikel = ""  # Deine Lösung hier

    # TODO: Prüfe ob Artikel existiert und entferne ihn
    # Tipp: Verwende 'in' Operator und 'del' oder 'pop()'
    # Deine Lösung hier


def einkaufsliste_anzeigen(einkaufsliste):
    """
    Zeigt die komplette Einkaufsliste an
    """
    print("\n=== Aktuelle Einkaufsliste ===")

    if not einkaufsliste:
        print("Die Einkaufsliste ist leer!")
        return

    # TODO: Zeige alle Artikel mit Mengen an
    # Tipp: Verwende eine for-Schleife mit items()
    # Deine Lösung hier

    print(f"Gesamt: {len(einkaufsliste)} Artikel")


def liste_speichern(einkaufsliste, dateiname="einkaufsliste.txt"):
    """
    Speichert die Einkaufsliste in eine Textdatei
    """
    print(f"\n=== Liste in '{dateiname}' speichern ===")

    try:
        # TODO: Öffne Datei zum Schreiben mit UTF-8 Encoding
        # Tipp: Verwende 'with open()' Statement
        # Deine Lösung hier

        # TODO: Schreibe Überschrift
        # Deine Lösung hier

        # TODO: Schreibe jeden Artikel in eine neue Zeile
        # Format: "Artikel: Menge"
        # Deine Lösung hier

        print(f"Einkaufsliste wurde erfolgreich in '{dateiname}' gespeichert!")

    except Exception as e:
        print(f"Fehler beim Speichern: {e}")


def liste_laden(dateiname="einkaufsliste.txt"):
    """
    Lädt die Einkaufsliste aus einer Textdatei
    """
    print(f"\n=== Liste aus '{dateiname}' laden ===")

    einkaufsliste = {}

    try:
        # TODO: Öffne Datei zum Lesen mit UTF-8 Encoding
        # Deine Lösung hier

        # TODO: Lese jede Zeile und parse sie
        # Tipp: Verwende split(":") um Artikel und Menge zu trennen
        # Ignoriere Leerzeilen und die Überschrift
        # Deine Lösung hier

        print(f"Einkaufsliste wurde erfolgreich aus '{dateiname}' geladen!")
        return einkaufsliste

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden!")
        return {}
    except Exception as e:
        print(f"Fehler beim Laden: {e}")
        return {}


def liste_als_json_speichern(einkaufsliste, dateiname="einkaufsliste.json"):
    """
    Speichert die Einkaufsliste als JSON-Datei (Bonus-Aufgabe)
    """
    print(f"\n=== Liste als JSON in '{dateiname}' speichern ===")

    import json

    try:
        # TODO: Speichere Dictionary als JSON-Datei
        # Tipp: Verwende json.dump() mit indent=4 und ensure_ascii=False
        # Deine Lösung hier

        print(
            f"Einkaufsliste wurde erfolgreich als JSON in '{dateiname}' gespeichert!")

    except Exception as e:
        print(f"Fehler beim JSON-Speichern: {e}")


def liste_aus_json_laden(dateiname="einkaufsliste.json"):
    """
    Lädt die Einkaufsliste aus einer JSON-Datei (Bonus-Aufgabe)
    """
    print(f"\n=== Liste aus JSON '{dateiname}' laden ===")

    import json

    try:
        # TODO: Lade Dictionary aus JSON-Datei
        # Tipp: Verwende json.load()
        # Deine Lösung hier
        einkaufsliste = {}

        print(
            f"Einkaufsliste wurde erfolgreich aus JSON '{dateiname}' geladen!")
        return einkaufsliste

    except FileNotFoundError:
        print(f"Fehler: Die JSON-Datei '{dateiname}' wurde nicht gefunden!")
        return {}
    except json.JSONDecodeError:
        print(f"Fehler: Die JSON-Datei '{dateiname}' ist beschädigt!")
        return {}
    except Exception as e:
        print(f"Fehler beim JSON-Laden: {e}")
        return {}


def main():
    """
    Hauptprogramm
    """
    einkaufsliste = {}

    while True:
        print("\n" + "="*50)
        print("EINKAUFSLISTEN-MANAGER")
        print("="*50)
        print("1. Neue Einkaufsliste erstellen")
        print("2. Artikel hinzufügen")
        print("3. Artikel entfernen")
        print("4. Einkaufsliste anzeigen")
        print("5. Liste in Textdatei speichern")
        print("6. Liste aus Textdatei laden")
        print("7. Liste als JSON speichern (Bonus)")
        print("8. Liste aus JSON laden (Bonus)")
        print("9. Programm beenden")
        print("="*50)

        auswahl = input("Wähle eine Option (1-9): ").strip()

        if auswahl == "1":
            einkaufsliste = einkaufsliste_erstellen()
        elif auswahl == "2":
            artikel_hinzufuegen(einkaufsliste)
        elif auswahl == "3":
            artikel_entfernen(einkaufsliste)
        elif auswahl == "4":
            einkaufsliste_anzeigen(einkaufsliste)
        elif auswahl == "5":
            liste_speichern(einkaufsliste)
        elif auswahl == "6":
            geladene_liste = liste_laden()
            if geladene_liste:
                einkaufsliste = geladene_liste
        elif auswahl == "7":
            liste_als_json_speichern(einkaufsliste)
        elif auswahl == "8":
            geladene_liste = liste_aus_json_laden()
            if geladene_liste:
                einkaufsliste = geladene_liste
        elif auswahl == "9":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle eine Zahl zwischen 1 und 9.")


if __name__ == "__main__":
    main()
