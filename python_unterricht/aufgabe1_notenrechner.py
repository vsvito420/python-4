#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe 1: Notenrechner

Erstelle ein Programm, das:
1. Ein Dictionary mit Fächern und Noten erstellt
2. Die Durchschnittsnote berechnet
3. Das Dictionary in eine JSON-Datei speichert
4. Die Daten wieder lädt und anzeigt

Beispiel-Dictionary:
{
    "Deutsch": 2,
    "Mathematik": 1,
    "Englisch": 2,
    "Geschichte": 3,
    "Biologie": 1
}
"""

import json


def notenrechner():
    """
    Hauptfunktion für den Notenrechner
    """
    print("=== Notenrechner ===")

    # TODO: Erstelle ein Dictionary mit Fächern und Noten
    # Beispiel: noten = {"Deutsch": 2, "Mathematik": 1, ...}
    noten = {
        # Deine Lösung hier
    }

    # TODO: Berechne die Durchschnittsnote
    # Tipp: Verwende sum() und len() Funktionen
    durchschnitt = 0.0
    # Deine Lösung hier

    print(f"Noten: {noten}")
    print(f"Durchschnittsnote: {durchschnitt:.2f}")

    # TODO: Speichere das Dictionary in eine JSON-Datei
    # Dateiname: "noten.json"
    # Tipp: Verwende json.dump() mit indent=4 und ensure_ascii=False
    # Deine Lösung hier

    print("Noten wurden in 'noten.json' gespeichert!")


def noten_laden():
    """
    Lädt die Noten aus der JSON-Datei und zeigt sie an
    """
    print("\n=== Noten laden ===")

    try:
        # TODO: Lade die Noten aus der JSON-Datei
        # Tipp: Verwende json.load() mit encoding="utf-8"
        # Deine Lösung hier
        geladene_noten = {}

        print("Geladene Noten:")
        for fach, note in geladene_noten.items():
            print(f"  {fach}: {note}")

        # TODO: Berechne erneut die Durchschnittsnote der geladenen Daten
        durchschnitt = 0.0
        # Deine Lösung hier

        print(f"Durchschnittsnote: {durchschnitt:.2f}")

    except FileNotFoundError:
        print("Fehler: Die Datei 'noten.json' wurde nicht gefunden!")
    except json.JSONDecodeError:
        print("Fehler: Die JSON-Datei ist beschädigt!")


def note_hinzufuegen():
    """
    Fügt eine neue Note hinzu (Bonus-Aufgabe)
    """
    print("\n=== Note hinzufügen ===")

    try:
        # TODO: Lade bestehende Noten
        # Deine Lösung hier
        noten = {}

        # TODO: Frage Benutzer nach Fach und Note
        # Tipp: Verwende input() Funktionen
        # Deine Lösung hier
        fach = ""
        note = 0

        # TODO: Füge neue Note hinzu
        # Deine Lösung hier

        # TODO: Speichere aktualisierte Noten
        # Deine Lösung hier

        print(f"Note für {fach} wurde hinzugefügt!")

    except Exception as e:
        print(f"Fehler beim Hinzufügen der Note: {e}")


def main():
    """
    Hauptprogramm
    """
    while True:
        print("\n" + "="*40)
        print("NOTENRECHNER")
        print("="*40)
        print("1. Noten eingeben und speichern")
        print("2. Noten laden und anzeigen")
        print("3. Note hinzufügen")
        print("4. Programm beenden")
        print("="*40)

        auswahl = input("Wähle eine Option (1-4): ").strip()

        if auswahl == "1":
            notenrechner()
        elif auswahl == "2":
            noten_laden()
        elif auswahl == "3":
            note_hinzufuegen()
        elif auswahl == "4":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle 1, 2, 3 oder 4.")


if __name__ == "__main__":
    main()
