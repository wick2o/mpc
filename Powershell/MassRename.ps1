#region ****************************** Execution started - TreeNode: E ******************************
function func_E()
{
& {
    param(
		$Path) Get-ChildItem -LiteralPath $Path -Force -ErrorAction SilentlyContinue | ForEach-Object {
		
	}

} 'E:\'
}

function action()
{
param(
	[string]$NewName
)
if ($NewName -match '[\\/:*?"<>|]') {
	throw 'Illegal characters in path. A file name cannot contain any of the following characters: \ / : * ? " < > |'
} else {
	$input | ForEach-Object {
		$_ | Move-Item -Destination (Join-Path -Path $_.PSParentPath -ChildPath $NewName) -Force
	}
}
}


  func_E | where { $_.Name -eq 'MAXWELL 2009'} | Get-ChildItem -Force -ErrorAction SilentlyContinue | where { $_.Name -eq 'X-REF MASTER FILES'} | Get-ChildItem -Force -ErrorAction SilentlyContinue | where { $_.Name -eq 'MX3Z - Dollies'} | action -relace( 'MX2','MX34')
#endregion ****************************** Execution completed - TreeNode: E ******************************
