import sys
from collections import defaultdict, deque

'''
1)sys.setrecursionlimit: Diese Funktion setzt das maximale Rekursionslimit in Python. 
Das Rekursionslimit gibt an, wie tief rekursive Funktionsaufrufe verschachtelt sein dürfen, 
bevor Python einen RecursionError auslöst. 
1 << 25: Dies ist eine bitweise Verschiebung nach links. 1 << 25 bedeutet 2^25 also 33.554.432. 
Das Rekursionslimit wird auf diesen Wert gesetzt.
Bei sehr großen Bäumen (z.B.n=100.000) kann die Rekursionstiefe der DFS sehr groß werden. 
2)input = sys.stdin.read:
sys.stdin.read ist eine Funktion, die die gesamte Eingabe von der Standardeingabe (stdin) als einen einzigen String liest.
Durch input = sys.stdin.read wird die Funktion sys.stdin.read der Variablen input zugewiesen. 
Das bedeutet, dass input() jetzt die gesamte Eingabe auf einmal liest.
data = input().split(): input() ruft die Funktion sys.stdin.read auf und liest die gesamte Eingabe als einen String.
.split() teilt diesen String an Leerzeichen (oder anderen Whitespace-Zeichen) und gibt eine Liste von Teilstrings zurück.

Beispiel: Angenommen, die Eingabe ist:
5 1
1 1 0 0 0
1 2
1 3
2 4
2 5
input(): Liest die gesamte Eingabe als einen String: "5 1\n1 1 0 0 0\n1 2\n1 3\n2 4\n2 5"
.split(): Teilt den String an Leerzeichen und Zeilenumbrüchen und gibt eine Liste zurück:
['5', '1', '1', '1', '0', '0', '0', '1', '2', '1', '3', '2', '4', '2', '5']
'''
def main():
    sys.setrecursionlimit(1 << 25)  # Erhöhe das Rekursionslimit (falls noch benötigt)
    input = sys.stdin.read  # Schnellere Eingabe
    data = input().split()
    
    # Eingabe lesen
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2 + n]))  # Liste der Katzen
    
    # Adjazenzliste erstellen
    '''
    Iteration 1:
    x = int(data[7]) = 1
    y = int(data[8]) = 2
    adj[1].append(2) → adj = {1: [2]}
    adj[2].append(1) → adj = {1: [2], 2: [1]}
    index += 2 → index = 9
    ......
    Ergibnis
    adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

    '''
    adj = defaultdict(list)
    index = 2 + n
    for _ in range(n - 1):
        x = int(data[index])
        y = int(data[index + 1])
        adj[x].append(y)
        adj[y].append(x)
        index += 2
    
    # Iterative DFS-Funktion
    '''
    stack: Ein Stack, der Tupel speichert. Jedes Tupel enthält:
    node: Der aktuelle Knoten.
    parent: Der Elternknoten des aktuellen Knotens (um Zyklen zu vermeiden).
    consecutive_cats: Die Anzahl der aufeinanderfolgenden Katzen auf dem aktuellen Pfad.
    count: Zählt die Anzahl der gültigen Blattknoten (Restaurants).
    Ergebnis:
    Der Stack wird mit dem Startknoten (start), einem Elternknoten von -1 (da die Wurzel keinen Eltern hat) 
    und consecutive_cats = 0 initialisiert.
    '''
    def iterative_dfs(start):
        stack = [(start, -1, 0)]  # (node, parent, consecutive_cats)
        count = 0
        
        while stack:
            node, parent, consecutive_cats = stack.pop()
            
            # Wenn der aktuelle Knoten eine Katze hat, erhöhe den Zähler
            if a[node - 1] == 1:
                consecutive_cats += 1
            else:
                consecutive_cats = 0  # Zurücksetzen, wenn keine Katze
            
            # Wenn die Anzahl der aufeinanderfolgenden Katzen m überschreitet, überspringe diesen Pfad
            if consecutive_cats > m:
                continue
            
            # Überprüfe, ob der aktuelle Knoten ein Blatt ist (außer der Wurzel)
            is_leaf = True
            for neighbor in adj[node]:
                if neighbor != parent:  # Gehe nicht zurück zum Elternknoten
                    is_leaf = False
                    stack.append((neighbor, node, consecutive_cats))
            
            # Wenn es ein Blatt ist, zähle es als gültiges Restaurant
            if is_leaf:
                count += 1
        
        return count
    
    # DFS starten (Wurzel ist Knoten 1)
    result = iterative_dfs(1)
    print(result)

if __name__ == "__main__":
    main()