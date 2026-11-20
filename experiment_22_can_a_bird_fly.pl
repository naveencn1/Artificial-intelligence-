% CSA17 - Artificial Intelligence | Experiment 22 (Manual Ex. 3.2): Prolog: Can a Bird Fly?
% Name            : V V Naveen Kumar
% Register Number : 192321018

bird(sparrow).
bird(eagle).
bird(crow).
bird(parrot).
bird(penguin).
bird(ostrich).
bird(kiwi).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

can_fly(B) :- bird(B), \+ cannot_fly(B).

check(B) :-
  ( can_fly(B) -> format('~w can fly~n', [B])
  ; bird(B) -> format('~w cannot fly~n', [B])
  ; format('~w is not in the knowledge base~n', [B])
  ).


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- can_fly(sparrow).
true.

?- can_fly(penguin).
false.

?- check(ostrich).
ostrich cannot fly
true.

?- check(dog).
dog is not in the knowledge base
true.

?- can_fly(B).
B = sparrow ;
B = eagle ;
B = crow ;
B = parrot.
*/
