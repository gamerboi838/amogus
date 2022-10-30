colors = ['Red','Blue','Green']
states = ['Nagpur','Thane','Pune','Mumbai']
neighbors = {}
neighbors['Nagpur'] = ['Thane','Pune']
neighbors['Thane'] = ['Nagpur','Pune','Mumbai']
neighbors['Pune'] = ['Nagpur','Thane','Mumbai']
neighbors['Mumbai'] = ['Thane','Pune']
 
colors_of_states = {}
 
def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True
 
def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color
 
def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)
 
main()
