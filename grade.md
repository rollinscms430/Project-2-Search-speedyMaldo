# Grade

## Anagrams

Code looks good. I did get an error from the filename: it wanted `words (1).txt` instead of `words.txt`.

## Word Ladder and Boggle

Word Ladder doesn't have much code. It looks like it's reading the dictionary. The next step after building the dictionary would be to
have a search loop that starts with the first word, checks for its neighbor words, and adds them to the search space.

The Boggle problem has something similar going on. The search method is using a loop over the board contents. This needs to be turned
into a loop that uses a queue or stack of states to keep track of all possible word paths through the grid. Review the handouts showing
how to implement the BFS: the structure of your code should look very similar to those.

## Total

60 / 100
