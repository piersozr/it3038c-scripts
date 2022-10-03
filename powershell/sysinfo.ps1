
function getIP{(Get-NetIPAddress).IPv4Address | Select-String "192*"}
Write-Host(getIP)
function getUser{($env:USERNAME)}
Write-Host(getUser)
function getHostname{(HOSTNAME)}
Write-Host(getHostname)
function getDate{(Get-Date)}
Write-Host(getDate)
function getPSVersion {($HOST.Version)}
$IP= getIP 
$USER = getUser 
$HOSTNAME = getHostName
$VERSION = getPSVersion 
$Date = getDate 
$BODY = "This machine's IP is $IP. User is $USER. The version is POWERSHELL $VERSION. Today's date is $DATE."
$BODY | Out-File C:\it3038c-scripts\Lab3output.txt