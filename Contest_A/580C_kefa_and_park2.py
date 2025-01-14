import sys
from collections import defaultdict, deque

def main():
    sys.setrecursionlimit(1 << 25)  # Erhöhe das Rekursionslimit (falls noch benötigt)
    input = sys.stdin.read  # Schnellere Eingabe
    data = input().split()
    
    # Eingabe lesen
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2 + n]))  # Liste der Katzen
    
    # Adjazenzliste erstellen
    adj = defaultdict(list)
    index = 2 + n
    for _ in range(n - 1):
        x = int(data[index])
        y = int(data[index + 1])
        adj[x].append(y)
        adj[y].append(x)
        index += 2
    
    # Iterative DFS-Funktion
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