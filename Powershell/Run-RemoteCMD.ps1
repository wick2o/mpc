<#

.SYNOPSIS
This is a powershell script

.DESCRIPTION
I have no description

.EXAMPLE
./Run-RemoteCMD.ps1 -compname jaime_filson -cmd "gpupdate /force"

.NOTES
no notes

.LINK
www.google.com

#>

param(
	[parameter(Mandatory = $true)]
	[string]$compname,
	[parameter(Mandatory = $True)]
	[string]$cmd
);


$newproc = Invoke-WmiMethod -class Win32_process -name Create -ArgumentList ("cmd.exe /c " + $cmd) -ComputerName $compname -Credential taittowers\administrator

if ($newproc.ReturnValue -eq 0)
{
	Write-Host "Command $($cmd) was successful on $($compname)" 
}
else {
	Write-Host "Command $($cmd) was unsuccessful on $($compname)"
}

