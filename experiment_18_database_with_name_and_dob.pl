% CSA17 - Artificial Intelligence | Experiment 18 (Manual Ex. 2.8): Prolog: Database with Name and DOB
% Name            : V V Naveen Kumar
% Register Number : 192321018

% person(Name, date(Day, Month, Year))
person(arun, date(12, 3, 2004)).
person(bala, date(25, 7, 2003)).
person(chitra, date(5, 11, 2004)).
person(divya, date(18, 3, 2005)).
person(elango, date(30, 1, 2003)).

dob(Name, D/M/Y) :- person(Name, date(D, M, Y)).
born_in_year(Name, Year) :- person(Name, date(_, _, Year)).
born_in_month(Name, Month) :- person(Name, date(_, Month, _)).
older(P1, P2) :-
  person(P1, date(D1, M1, Y1)),
  person(P2, date(D2, M2, Y2)),
  P1 \= P2,
  ( Y1 < Y2 ; Y1 =:= Y2, M1 < M2 ; Y1 =:= Y2, M1 =:= M2, D1 < D2 ).


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- dob(chitra, X).
X = 5/11/2004.

?- born_in_year(N, 2004).
N = arun ;
N = chitra.

?- born_in_month(N, 3).
N = arun ;
N = divya.

?- older(bala, arun).
true.

?- person(Name, date(_, _, 2003)).
Name = bala ;
Name = elango.
*/
