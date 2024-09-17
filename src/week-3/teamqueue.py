from collections import deque, defaultdict

def team_queue_simulation():
    case_number = 1

    while True:
        t = int(input())
        if t == 0:
            break
        
        print(f"Scenario #{case_number}")
        case_number += 1

        team_of = {}  
        teams = []  
        for i in range(t):
            members = list(map(int, input().split()))[1:]  
            teams.append(deque())  
            for member in members:
                team_of[member] = i

        team_queue = deque()  

        
        while True:
            command = input().strip()
            if command == "STOP":
                break
            elif command.startswith("ENQUEUE"):
                _, x = command.split()
                x = int(x)
                team_id = team_of[x]
                
                
                if not teams[team_id]:
                    team_queue.append(team_id)
                
                
                teams[team_id].append(x)
            elif command == "DEQUEUE":
                
                front_team_id = team_queue[0]
                
                print(teams[front_team_id].popleft())
                
                if not teams[front_team_id]:
                    team_queue.popleft()
        
        print()


team_queue_simulation()
