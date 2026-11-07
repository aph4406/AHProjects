$RemoveList = @("")
$ExcludeFromPasswordChange = @("")
$Password = Read-Host "Enter the new password" -AsSecureString

# Remove extra users
$UsersToRemove = @(Get-LocalUser | Where-Object { $_.Name -in $RemoveList })
foreach($Account in $UsersToRemove) {
    try {
        Remove-LocalUser -Name $Account.Name -ErrorAction Stop
        Write-Output "Removed: $($Account.Name)"
    }
    catch {
        Write-Warning "Could not remove '$($Account.Name)': $($_.Exception.Message)"
        throw
    }
}
$RemainingUsers = @(Get-LocalUser)

# Change passwords
foreach ($Account in $RemainingUsers) {
    if ($Account.Name -in $ExcludeFromPasswordChange) { continue }
    try {
        Set-LocalUser -Name $Account.Name -Password $Password -ErrorAction Stop
        Write-Output "Password changed: $($Account.Name)"
    }
    catch {
        Write-Warning "Could not change password for '$($Account.Name)': $($_.Exception.Message)"
    }
}
