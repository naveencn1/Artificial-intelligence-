% CSA17 - Artificial Intelligence | Experiment 21 (Manual Ex. 3.1): Prolog: Towers of Hanoi
% Name            : V V Naveen Kumar
% Register Number : 192321018

hanoi(1, From, To, _) :-
  format('Move disk 1 from ~w to ~w~n', [From, To]).
hanoi(N, From, To, Via) :-
  N > 1,
  M is N - 1,
  hanoi(M, From, Via, To),
  format('Move disk ~w from ~w to ~w~n', [N, From, To]),
  hanoi(M, Via, To, From).
