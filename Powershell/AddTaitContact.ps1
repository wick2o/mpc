<#

.SYNOPSIS
This is a powershell script

.DESCRIPTION
I have no description

.EXAMPLE
./AddTaitContact.ps1 -fname Jaime -lname Filson -Email jaime@taittowers.com -isCell $False

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
	New-MailContact -ExternalEmailAddress $Email -Name "$FName $LName" -Alias $FName$LName -FirstName $FName -LastName $LName
	Set-MailContact -Identity "$FName $LName" -HiddenFromAddressListsEnabled $true
	Add-DistributionGroupMember  -ID TaitShop -Member "$FName $LName"
	Write-Host "$FName $LName Has Been Added"
}
else {
	New-MailContact -ExternalEmailAddress $Email -Name "$FName $LName Cell" -Alias $FName$LName -FirstName $FName -LastName $LName
	Set-MailContact -Identity "$FName $LName Cell" -HiddenFromAddressListsEnabled $true
	Add-DistributionGroupMember  -ID TaitEmergency -Member "$FName $LName Cell"
	Write-Host "$FName $LName Cell Has Been Added"
}

#New-MailContact -ExternalEmailAddress 'SMTP:whosyourdata@gmail.com' -Name 'Franko Williams' -Alias 'FrankoWilliams' -FirstName 'Franko' -LastName 'Williams';
