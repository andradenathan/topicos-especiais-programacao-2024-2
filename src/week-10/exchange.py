from collections import defaultdict, deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class ExchangeRateGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_exchange_rate(self, m, itemA, n, itemB):
        self.graph[itemA][itemB] = (m, n)
        self.graph[itemB][itemA] = (n, m)

    def find_exchange_rate(self, itemA, itemB):
        if itemA not in self.graph or itemB not in self.graph:
            return None
            
        queue = deque([(itemA, 1, 1)]) 
        visited = {itemA}

        while queue:
            current_item, num, denom = queue.popleft()
            
            if current_item == itemB:
                common_divisor = gcd(num, denom)
                return num // common_divisor, denom // common_divisor
            
            for neighbor, (m, n) in self.graph[current_item].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, num * m, denom * n))
        return None

def process_input():
    exchange_graph = ExchangeRateGraph()
    results = []
    
    while True:
        line = input().strip()
        if line == ".":
            break
        
        if line.startswith("!"):
            parts = line.split()
            m = int(parts[1])
            itemA = parts[2]
            n = int(parts[4])
            itemB = parts[5]
            exchange_graph.add_exchange_rate(m, itemA, n, itemB)
        
        elif line.startswith("?"):
            parts = line.split()
            itemA = parts[1]
            itemB = parts[3]
            result = exchange_graph.find_exchange_rate(itemA, itemB)
            
            if result:
                num, denom = result
                results.append(f"{num} {itemA} = {denom} {itemB}")
            else:
                results.append(f"? {itemA} = ? {itemB}")
    
    for result in results:
        print(result)

process_input()
