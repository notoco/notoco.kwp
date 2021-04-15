# -*- coding: UTF-8 -*-
# Import
import xbmcaddon
import xbmcgui
import xbmcvfs
import shutil
import xbmc
import os
import requests
import sys

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

listarepo = requests.get("https://raw.githubusercontent.com/notoco/notoco.kwp/master/lista.txt").text.split("\n")
listarepo = [x for x in listarepo if x]

xbmcgui.Dialog().textviewer(addonname, "Program usuwa repozytoria i programy, subbiektywnie ocenione przez ekipę "
                                       "KODIWPIGULCE.pl jako niebezpieczne.\nNie odpowiadamy za straty wywołane "
                                       "usunięciem repozytoriów bądź programów.\nUżywasz na własną "
                                       "odpowiedzialność\nRepozytoria są usuwane bezpośrednio, z pominięciem "
                                       "odinstalowania przez kodi, co często jest niemożliwe przez istniejące "
                                       "zależności.\nPonadto usuwany jest program INDIGO")

potwierdz = xbmcgui.Dialog().yesno(addonname, "Potwierdzasz wykonanie czyszczenia z użyciem sprzątaczki KWP?")

if potwierdz:
    usuniete = ""
    for sciezka in listarepo:
        addon_sciezka = xbmcvfs.translatePath('special://home/addons/' + sciezka + '/')
        if os.path.isdir(addon_sciezka):
            xbmc.executeJSONRPC(
                '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "' + sciezka + '","enabled":false}}')
            usunac = xbmcgui.Dialog().yesno(addonname, "Usunąć repozytorium?\n" + sciezka)
            if usunac:
                shutil.rmtree(addon_sciezka, ignore_errors=True)
                usuniete = (usuniete + " " + sciezka)
    if usuniete:
        xbmcgui.Dialog().ok(addonname, f"Usunięto następujące repozytoria\n{usuniete}\nZrestaruj kodi.")
        xbmcgui.Dialog().ok(addonname, "Wymagany jest ponowne uruchomienie kodi.\nZrestaruj kodi.")
    else:
        xbmcgui.Dialog().ok(addonname, "Jest super!\nNie znaleziono żadnych niebezpiecznych repozytoriów.")

else:
    sys.exit()
