'''
DFS (Depth-First Search) ist ein Algorithmus, der verwendet wird, um Bäume oder Graphen zu durchlaufen. 
Der Algorithmus erkundet einen Pfad so weit wie möglich, bevor er zurückgeht und einen anderen Pfad erkundet. 
Im Kontext von Bäumen bedeutet dies, dass DFS so tief wie möglich in einen Teilbaum vordringt, bevor er zu anderen Teilbäumen wechselt.

Kefa decided to celebrate his first big salary by going to the restaurant.

He lives by an unusual park. The park is a rooted tree consisting of n vertices with the root at vertex 1. 
Vertex 1 also contains Kefa's house. Unfortunaely for our hero, the park also contains cats. Kefa has already found out what are the vertices with cats in them.

The leaf vertices of the park contain restaurants. Kefa wants to choose a restaurant where he will go, but unfortunately he is very afraid of cats, 
so there is no way he will go to the restaurant if the path from the restaurant to his house contains more than m consecutive vertices with cats.

Your task is to help Kefa count the number of restaurants where he can go.
'''
from collections import defaultdict

def main():
    # Eingabe lesen
    n, m = map(int, input().split())  # n = 4, m = 1
    #Eine Liste, die angibt, ob ein Knoten eine Katze hat (1) oder nicht (0). 
    a = list(map(int, input().split())) # a = [1, 1, 0, 0]
    
    '''
    adj: Ein defaultdict, das die Adjazenzliste des Baums speichert. Jeder Schlüssel im Wörterbuch ist ein Knoten, 
    und der Wert ist eine Liste seiner Nachbarn.
    Für jede Kante (Verbindung zwischen zwei Knoten) wird der Nachbar in die Liste des jeweiligen Knotens eingefügt.
    Beispiel: Wenn die Eingabe 1 2 ist, wird Knoten 2 zur Nachbarliste von Knoten 1 hinzugefügt und umgekehrt.
    '''
    
    # Adjazenzliste erstellen
    # out: adj = {1: [2, 3, 4], 2: [1], 3: [1], 4: [1]}
    adj = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    
    # DFS-Funktion
    '''
    Parameter:
    node: Der aktuelle Knoten, der untersucht wird.
    parent: Der Elternknoten des aktuellen Knotens (um Zyklen zu vermeiden).
    consecutive_cats: Die Anzahl der aufeinanderfolgenden Katzen auf dem aktuellen Pfad.
    '''
    def dfs(node, parent, consecutive_cats):
        # Wenn der aktuelle Knoten eine Katze hat, erhöhe den Zähler
        if a[node - 1] == 1:
            consecutive_cats += 1
        else:
            consecutive_cats = 0  # Zurücksetzen, wenn keine Katze
        
        # Wenn die Anzahl der aufeinanderfolgenden Katzen m überschreitet, stoppe die Suche
        if consecutive_cats > m:
            return 0
        
        # Überprüfe, ob der aktuelle Knoten ein Blatt ist (außer der Wurzel)
        is_leaf = True
        count = 0
        for neighbor in adj[node]:
            if neighbor != parent:  # Gehe nicht zurück zum Elternknoten
                is_leaf = False
                count += dfs(neighbor, node, consecutive_cats)
        
        # Wenn es ein Blatt ist, gib 1 zurück (gültiges Restaurant), sonst die Summe der Kinder
        return 1 if is_leaf else count
    
    # DFS starten (Wurzel ist Knoten 1)
    result = dfs(1, -1, 0)
    print(result)

if __name__ == "__main__":
    main()
