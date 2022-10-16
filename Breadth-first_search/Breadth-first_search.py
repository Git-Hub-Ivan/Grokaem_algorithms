from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is seller!')
                return True
            else:
                try:
                    search_queue += graph[person]
                    searched.append(person)
                except KeyError:
                    print(f'У {person} нет друзей')
    return False


def person_is_seller(man):
    if man[-1] == 'r':
        return man


graph = {'you': ['alice', 'bob', 'clair']}

search('you')
