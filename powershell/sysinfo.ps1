function getIP {(Get-NetIPAddress).ipv4address | Select-String "192*"}
Write-Host(getIP)