# New-Item -Path ".\ScriptForDiskpart_PrepareHDD.txt" -Verbose999
# Start-Process -FilePath "diskpart.exe"  -ArgumentList "/s c:\\Users\\м\\Documents\\ScriptForDiskpart_ViewListOfDisks.txt > .\\temp.txt" -Verb RunAs

# Start-Process -FilePath "diskpart.exe"  -ArgumentList "/s c:\\Users\\м\\Documents\\ScriptForDiskpart_ViewListOfDisks.txt" -Wait
# > powershell.exe -executionpolicy bypass -File .\PrepareDiskForWindowsAndLinux.ps1

# ---------------  Delete partition from selected drive ---------------


 #>