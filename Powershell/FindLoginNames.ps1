<#

.SYNOPSIS
This is a powershell script

.DESCRIPTION
I have no description

.EXAMPLE
./FindLoginNames.ps1 -filename C:\path\to\file.txt

.NOTES
no notes

.LINK
www.google.com

#>

param(
	[parameter(Mandatory = $true)]
	[string]$filename
);


$my_data = Get-Content $filename
foreach ($full_name in $my_data ) {
	$name = $full_name.split(" ")
	$Search = New-Object DirectoryServices.DirectorySearcher([ADSI]“”)
	$Search.filter = “(&(objectClass=user)(givenName=$($name[0]))(sn=$($name[1])))”
	$results = $Search.Findall()
	foreach($result in $results){
		$username = $result.GetDirectoryEntry()
		Write-Output "$($full_name)|$($username.sAMAccountName)"
	}
	
}


