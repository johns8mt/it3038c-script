Function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP

Write-Host("This machine's IP is $IP")

Function TheDate{
    (Get-Date -DisplayHint Date)
    }

$DATE = TheDate
write-host("Todays date is $DATE")


Function GetTheUser{
    (Get-LocalUser -Name "Administrator")
}

$UserName = GetTheUser
Write-Host("The User is $UserName")

Function Host{
    ([System.Net.Dns]::GetHostName())

$HostName = Host
Write-Host("Host is $HostName")

Function Version{
    ($PSVersionTable.PSVersion.ToString())

$Version = Version
Write-Host("Version of PS is $Version")

Send-MailMessage -To "johns8mt@ucmail.uc.edu" -From "18johnson.matthew@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
