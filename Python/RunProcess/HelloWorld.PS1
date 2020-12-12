$SCRIPT_DIR = Split-Path -Parent $PSCommandPath
$TEMP_DIR_NAME = "Temp"
$TEMP_DIR = Join-Path -Path $SCRIPT_DIR -ChildPath $TEMP_DIR_NAME
if ( !$(Test-Path -Path $TEMP_DIR) )   {
    New-Item -Path $SCRIPT_DIR -Name $TEMP_DIR_NAME -Type "directory"
}
for($i=1; $i -lt 16; $i++) {
    Write-Host "$i. Hello, world!"
    $TestString = "$i. Hello, world!"
    Out-File -FilePath $(Join-Path -Path $TEMP_DIR -ChildPath "temp.temp") -Append -InputObject $TestString
    Start-Sleep -s 1
}
# C:\Work\Examples>powershell.exe "C:\\Work\\Examples\\HelloWorld.PS1"