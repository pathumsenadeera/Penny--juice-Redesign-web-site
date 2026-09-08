Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\pathu\.gemini\antigravity-ide\brain\5c46c672-9c61-43e0-963e-05d5e9a987f5\.user_uploaded\media_1788801950803.png"
$img = [System.Drawing.Bitmap]::FromFile($srcPath)

Write-Host "Source Width: $($img.Width), Height: $($img.Height)"
$img.Dispose()
