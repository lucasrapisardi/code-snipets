from collections import deque

def breadth_first(name):
    """deque is double ended queue"""
    search_list = deque()
    search_list += graphe[name]
    verified = {}

    while search_list:
        person = search_list.popleft()
        if not person in verified:
            if is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_list += graphe[person]
                """We can solve this by creating a hash, that has written and reading O(1)"""
                verified[person] = True
                """Also we can solve it by includind into a list, that will take O(n) on insertion and O[1] on reading"""
                # verified.append(person)
    return False
    
def is_seller(name):
    return name[-1] == "m"

graphe = {}
graphe["you"] = [ "alice", "bob", "claire" ]
graphe["bob"] = [ "anuj", "peggy" ]
graphe["alice"] = [ "peggy" ]
graphe["claire"] = ["thom", "jonny"]
graphe["anuj"] = []
graphe["peggy"] = []
graphe["thom"] = []
graphe["jonny"] = []

print(breadth_first("you"))