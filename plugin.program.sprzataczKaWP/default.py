# -*- coding: UTF-8 -*-
# Import
import xbmcaddon
import xbmcgui
import shutil
import xbmc
import os
import requests
import json
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

listarepo = requests.get("lista.txt").text.split("\n")
listarepo = [x for x in listarepo if x]

potwierdz = xbmcgui.Dialog().ok(addonname, "Program usuwa repozytoria i programy, subbiektywnie ocenione przez ekipę KODIWPIGULCE.pl jako niebezpieczne.", "Nie odpowiadamy za straty wywołane usunięciem repozytoriów bądź programów.\nUżywasz na własną odpowiedzialność", "Repozytoria są usuwane bezpośrednio, z pominięciem odinstalowania przez kodi, co często jest niemożliwe przez istniejące zależności.\nPonadto usuwany jest program INDIGO") 
if potwierdz:
	usuniete = ""
	for sciezka in listarepo:
		addon_sciezka = xbmc.translatePath(('special://home/addons/'+sciezka+'/')).decode('utf-8')
		if os.path.isdir(addon_sciezka):
			xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "'+sciezka+'","enabled":false}}')
			usunac = xbmcgui.Dialog().yesno(addonname, "Usunąć repozytorium?\n", sciezka) 
			if usunac:
				shutil.rmtree(addon_sciezka, ignore_errors=True)
				usuniete = (usuniete + " "+sciezka)
	if usuniete:
		xbmcgui.Dialog().ok(addonname, "Usunięto następujące repozytoria", usuniete,"Zrestaruj kodi.")
		xbmcgui.Dialog().ok(addonname, "Wymagany jest ponowne uruchomienie kodi.","Zrestaruj kodi.")
	else:
		xbmcgui.Dialog().ok(addonname, "Jest super!","Nie znaleziono żadnych niebezpiecznych repozytoriów.")

else:
	sys.exit()
