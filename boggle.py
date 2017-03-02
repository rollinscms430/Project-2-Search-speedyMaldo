board = {0.0 : u, 0.1 : n, 0.2: t, 0.3 : h, 1.0 : g, 1.1 : a, 1.2 : e, 1.3 : s, 2.0 : s, 2.1 : r, 2.2 : t, 2.4 : r, 3.0 : h, 3.1 : m, 3.2 : i, 3.3 : a}
words = {}
with open('words (1).txt') as f:
    line = line.strip()
    words.setdefault().append(line)
    

def finished(self):
    for row in range(len(self.letters)):
        if 1 in self.letters[row]:
            return false
        return true

def already_visited(state, visited):
    if hash(state.letters) in visited:
        return True
    else:
        return False

def add_to_visited(state, visited):
    h = hash(state.letters)
    visited[h] = True

def check_word(position):
    check = [i for i in words.keys() if position(i) = words.keys()]
    return check
    

def search(start_loc):
    first_position = board(i)
    for [i in board if i != visited]:
        check_word
        if word = word(words):
            print word
            if i + .1 = is_valid():
                check_word
            elif: i + 1 = is_valid():
                check_word
            elif: i - .1 = is_valid():
                check_word
            elif i - 1 = is_valid():
                check_word
            else:
                new_loc
                    
    #create tree that has all its neighbors
    #each set of children will have its own children
    #output each word that you encounter
    #breadth first search
    #use handouts to create breadth first search
    #this starts by initializing the first state and a queue of the frontier
def is_valid(s, boggle_board):

        #if s is a real word, then print s's word
        for each of the eight directions:
            #check to see if each of those directions are a valid move
            #create state s, and add a new letter to the copy of s's word and a new position to the copy of s's history
            if the move results in a valid prefix
            #create new state object and add it to the queue
      
if __name__ =='__main__':
    boggle(4)