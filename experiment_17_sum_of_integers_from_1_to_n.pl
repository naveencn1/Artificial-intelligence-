% CSA17 - Artificial Intelligence | Experiment 17 (Manual Ex. 2.7): Prolog: Sum of Integers from 1 to n
% Name            : V V Naveen Kumar
% Register Number : 192321018

% sum(N, S): S is 1 + 2 + ... + N
sum(0, 0).
sum(N, S) :-
  N > 0,
  N1 is N - 1,
  sum(N1, S1),
  S is S1 + N.


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- sum(5, S).
S = 15.

?- sum(10, S).
S = 55.

?- sum(100, S).
S = 5050.
*/
