Set shell = CreateObject("WScript.Shell")
scriptPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
command = "pythonw.exe """ & scriptPath & "\main.py""""
shell.Run command, 0
