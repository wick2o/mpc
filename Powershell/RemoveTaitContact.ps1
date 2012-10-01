<#

.SYNOPSIS
This is a powershell script

.DESCRIPTION
I have no description

.EXAMPLE
./RemoveTaitContact.ps1 -fname Jaime -lname Filson

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
);
 
    Remove-MailContact -identity "$FName $LName" -confirm:$false
	Remove-MailContact -identity "$FName $LName Cell" -confirm:$false

