tracks = []

track_M = open("Name der Datei", "r")


def einfuegen_liste():  # packt die Datei erstmals in eine Liste
    for i in track_M:
        tracks.append(i)


def liste_doppelwert():  # prüft, ob ein Wert doppelt vorkommt
    for i in tracks:
        if tracks.count(i) > 1:
            tracks.remove(i)


einfuegen_liste()
liste_doppelwert()

print(tracks)
