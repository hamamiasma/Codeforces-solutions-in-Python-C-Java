'''
A. Odd Divisor
'''
def has_odd_divisor(n):
    # Teile n solange durch 2, bis es ungerade ist
    while n % 2 == 0:
        n //= 2
    # Wenn n > 1, hat es einen ungeraden Teiler
    if n > 1:
        return "YES"
    else:
        return "NO"
    
# Eingabe erstellen
t = int(input())  # Lese die Anzahl der Testfälle
for _ in range(t):  # Schleife über alle Testfälle
    n = int(input())  # Lese die Zahl n für den aktuellen Testfall
    print(has_odd_divisor(n))  # Verarbeite n und gib das Ergebnis aus