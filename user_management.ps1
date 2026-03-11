$KeepList = @("Administrator", "drwho", "martymcfly", "arthurdent", "sambeckett", "loki", "riphunter", "theflash", "tonystark", "drstrange", "bartallen", "whiteteam", "blackteam", "grayteam", "datadog", "dd-dog", "ddagentuser", "dd-agent")
$ExcludeFromPasswordChange = @("whiteteam", "blackteam", "grayteam", "datadog", "dd-dog", "ddagentuser", "dd-agent")
$Password = ConvertTo-SecureString "ChangeMeNow!2025" -AsPlainText -Force

# Remove extra users
Get-LocalUser | Where-Object { $_.Name -notin $KeepList } | ForEach-Object {
    Remove-LocalUser -Name $_.Name
    Write-Output "Removed: $($_.Name)"
}

# Change passwords
foreach ($user in $KeepList) {
    if ($user -in $ExcludeFromPasswordChange) { continue }
    Set-LocalUser -Name $user -Password $Password
    Write-Output "Password changed: $user
}
Admin, Administrator, arthurdent, bartallen, ddagentuser, drstrange, drwho, loki, martymcfly, riphunter, sambeckett, theflash, tonystark, whiteteam

#Single Line
Get-LocalUser | Where-Object { $_.Name -notin $KeepList } | ForEach-Object { Remove-LocalUser -Name $_.Name; Write-Output "Removed: $($_.Name)" }; $KeepList | Where-Object { $_ -notin $ExcludeFromPasswordChange } | ForEach-Object { Set-LocalUser -Name $_ -Password $Password; Write-Output "Password changed: $_" }



