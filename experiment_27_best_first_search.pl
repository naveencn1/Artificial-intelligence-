% CSA17 - Artificial Intelligence | Experiment 27 (Manual Ex. 3.7): Prolog: Best First Search
% Name            : V V Naveen Kumar
% Register Number : 192321018

edge(a, b). edge(a, c).
edge(b, d). edge(b, e).
edge(c, f).
edge(e, g). edge(f, g).

h(a, 7). h(b, 5). h(c, 4). h(d, 6). h(e, 2). h(f, 3). h(g, 0).

best_first(Start, Goal, Path) :-
  bf([[Start]], Goal, RevPath),
  reverse(RevPath, Path).

bf([[Goal|Rest]|_], Goal, [Goal|Rest]) :- !.
bf([[N|Rest]|Others], Goal, Path) :-
  findall([M, N|Rest],
      ( edge(N, M), \+ member(M, [N|Rest]) ),
      Children),
  append(Others, Children, All),
  sort_by_h(All, Sorted),
  bf(Sorted, Goal, Path).

sort_by_h(Paths, Sorted) :-
  map_list_to_pairs(path_h, Paths, Pairs),
  keysort(Pairs, SortedPairs),
  pairs_values(SortedPairs, Sorted).

path_h([N|_], H) :- h(N, H).
