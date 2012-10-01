<#

.SYNOPSIS
This is a powershell script

.DESCRIPTION
I have no description

.EXAMPLE
./UpdateTaitContact.ps1 -fname Jaime -lname Filson -email Jaime@taittowers.com -iscell $true

.NOTES
no notes

.LINK
www.google.com

#>

param(
	[parameter(Mandatory = $True)]
	[string]$FName,
	[parameter(Mandatory = $True)]
	[string]$LName, 
	[parameter(Mandatory = $True)]
	[string]$Email, 
	[parameter(Mandatory = $True)]
	[boolean]$isCell

);
 
if ($isCell -eq $False) {
    Set-MailContact -identity "$FName $LName" -ExternalEmailAddress $Email
}
else {
	Set-MailContact -identity "$FName $LName Cell" -ExternalEmailAddress $Email
}
