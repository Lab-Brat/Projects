from enum import Enum
from collections import namedtuple
from functools import partial


def breadth_first_search(*, start, is_goal, get_neighbors):
    parent = dict()
    to_visit = [start]
    discovered = set([start])

    while to_visit:
        vertex = to_visit.pop(0)

        if is_goal(vertex):
            path = []
            while vertex is not None:
                path.insert(0, vertex)
                vertex = parent.get(vertex)
            return path

        for neighbor in get_neighbors(vertex):
            if neighbor not in discovered:
                discovered.add(neighbor)
                parent[neighbor] = vertex
                to_visit.append(neighbor)


def is_valid(state):
    goat_eats_cabbage = (state.goat == state.cabbage and state.man != state.goat)
    wolf_eats_goat = (state.wolf == state.goat and state.man != state.wolf)
    invalid = goat_eats_cabbage or wolf_eats_goat

    return not invalid

def next_states(state):
    if state.man == Location.A:
        other_side = Location.B
    else:
        other_side = Location.A

    move = partial(state._replace, man=other_side)

    candidates = [move()]

    for thing in ["cabbage", "goat", "wolf"]:
        if getattr(state, thing) == state.man:
            candidates.append(move(**{thing: other_side}))

    yield from filter(is_valid, candidates)


#------------------OUTPUT------------------#

State = namedtuple("State", ["man", "cabbage", "goat", "wolf"])
Location = Enum("Location", ["A", "B"])

start_state = State(man=Location.A, cabbage=Location.A, goat=Location.A, wolf=Location.A,)
goal_state = State(man=Location.B, cabbage=Location.B, goat=Location.B, wolf=Location.B,)

path = breadth_first_search(start = start_state, is_goal = goal_state.__eq__, get_neighbors = next_states,)

def describe_solution(path):
    for old, new in zip(path, path[1:]):
        boat = [
            thing
            for thing in ["man", "cabbage", "goat", "wolf"]
            if getattr(old, thing) != getattr(new, thing)
        ]
        print(old.man, "to", new.man, boat)

describe_solution(path)
