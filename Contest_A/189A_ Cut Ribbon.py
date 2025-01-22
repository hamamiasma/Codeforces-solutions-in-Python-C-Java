'''
Polycarpus hat ein Band der Länge n. Er möchte das Band so schneiden, dass die folgenden Bedingungen erfüllt sind:
Bedingung 1: Jedes Teilstück des Bandes muss eine Länge von a, b oder c haben.
Bedingung 2: Die Anzahl der Teilstücke soll maximal sein.

Eingabe:
Die erste Zeile enthält vier durch Leerzeichen getrennte ganze Zahlen:
n: Die Länge des ursprünglichen Bandes (1 ≤ n ≤ 4000).
a, b, c: Die erlaubten Längen der Teilstücke nach dem Schneiden (1 ≤ a, b, c ≤ 4000).
Die Werte a, b und c können gleich sein.

Ausgabe:
Gib eine einzige ganze Zahl aus: die maximale Anzahl von Teilstücken, die nach dem Schneiden des Bandes entstehen können.
Es ist garantiert, dass mindestens eine gültige Möglichkeit existiert, das Band zu schneiden.

dp = [-1] * (n + 1) ist eine Initialisierung eines Arrays (oder einer Liste in Python), das für die dynamische Programmierung verwendet wird.
verwendet wird, um Zwischenergebnisse zu speichern und wiederzuverwenden, anstatt sie immer wieder neu zu berechnen.
[-1] ist eine Liste mit einem einzigen Element, nämlich -1.
* (n + 1) bedeutet, dass diese Liste n + 1 Mal wiederholt wird.
Das Ergebnis ist eine Liste der Länge n + 1, bei der jedes Element -1 ist.
'''

def max_ribbon_pieces(n, a, b, c):
    # Initialisiere das dp-Array
    dp = [-1] * (n + 1)
    dp[0] = 0  # Ein Band der Länge 0 kann in 0 Teile geschnitten werden

    # Fülle das dp-Array
    for i in range(1, n + 1):
        # Überprüfe, ob ein Schnitt der Länge a möglich ist
        if i >= a and dp[i - a] != -1:
            dp[i] = max(dp[i], dp[i - a] + 1)
        # Überprüfe, ob ein Schnitt der Länge b möglich ist
        if i >= b and dp[i - b] != -1:
            dp[i] = max(dp[i], dp[i - b] + 1)
        # Überprüfe, ob ein Schnitt der Länge c möglich ist
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)

    # Das Ergebnis ist dp[n]
    return dp[n]

# Eingabe
n, a, b, c = map(int, input().split())

# Berechne die Lösung
result = max_ribbon_pieces(n, a, b, c)

# Ausgabe
print(result)

