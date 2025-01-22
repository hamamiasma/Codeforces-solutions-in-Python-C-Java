'''
Gegeben ist eine ganze Zahl n (mit 12 ≤ n ≤ 10^6). 
Die Aufgabe besteht darin, zwei zusammengesetzte Zahlen x und y zu finden, sodass x + y = n. 
Eine zusammengesetzte Zahl ist eine positive ganze Zahl, die mindestens einen Teiler außer 1 und sich selbst hat, also keine Primzahl ist.
'''

def is_composite(num):
    """Überprüft, ob eine Zahl zusammengesetzt ist."""
    if num < 2:
        return False
    # Wenn eine Zahl num zusammengesetzt ist, dann hat sie mindestens einen Teiler, der kleiner oder gleich der Quadratwurzel von num ist.
    # num**0.5 berechnet die Quadratwurzel von num.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def find_composite_sum(n):
    """Findet zwei zusammengesetzte Zahlen x und y, sodass x + y = n."""
    # Wir wählen x als 4, 6, 8, 9 usw. und überprüfen, ob y = n - x zusammengesetzt ist
    for x in [4, 6, 8, 9]:
        y = n - x
        if is_composite(y):
            return x, y
    return None  # Sollte nie erreicht werden, da die Aufgabe garantiert, dass eine Lösung existiert

# Eingabe
n = int(input())

# Berechne die Lösung
x, y = find_composite_sum(n)

# Ausgabe
print(x, y)