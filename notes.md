# 2015 day 7

Different ideas for solving this problem:

 - mine: classic parsing & execution of the language by recursively compute dependency the tree, starting from the goal 
 - use regex to reformat and sort the code (?!), then run eval
 - use regex to write a large recursive solver: https://gist.github.com/mgiuffrida/f275912b9bd92a3f403e
 - use Z3 to solve the tree https://mobeigi.com/blog/capture-the-flag/advent-of-code/advent-of-code-day-7/