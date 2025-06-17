# 1.
$produktname = "Tastatur"
$stückpreis = 25.99
$anzahl = 3
$mwstSatz = 0.19  # 19% Mehrwertsteuer

$result = ($stückpreis + ($stückpreis * $mwstSatz)) * $anzahl

Write-Host "Produkt: $produktname, Netto: $stückpreis, Brutto: $($stückpreis + ($stückpreis * $mwstSatz)), Gesamt: $result"

# 2.
$x = 3
$y = 1

$sum = $x + $y
$sub = $x - $y
$mult = $x * $y
$div = $x / $y
$mod = $x % 2

Write-Output "Sum: $sum, Substraction: $sub, Multiplication: $mult, Division: $div, Modulo: $mod"