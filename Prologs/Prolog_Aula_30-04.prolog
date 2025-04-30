%fatos ou verdades
nasceuEm("Matheus","Pelotas").
nasceuEm("Julian","Santa Maria").
nasceuEm("Odilon","Santa Maria").
nasceuEm("Andrei","Santa Maria").
nasceuEm("Davi","Pelotas").
nasceuEm("Enzo","Pelotas").

%regra recursiva de sobrecarga
nasceuEm(Pessoa, Lugar):- 
    nasceuEm(Pessoa, I),
    estaEm(I, Lugar).

localizadoEm("Pelotas","RS").
localizadoEm("Santa Maria","RS").
localizadoEm("RS","Brasil").


%regra recursiva
estaEm(Lugar, OutroLugar) :-
    localizadoEm(Lugar, OutroLugar).
estaEm(Lugar, OutroLugar) :-
    localizadoEm(Lugar, I),
    estaEm(I, OutroLugar).

progenitor("Odilon","Julian").
progenitor("Odilon","Andrei").
progenitor("Julian","Enzo").
progenitor("Julian","Davi").
progenitor("Julian","Matheus").
progenitor("Andrei","Joao").
progenitor("Andrei","Henrique").

avo(Avo, Neta) :-
    progenitor(Avo, Pai),
    progenitor(Pai, Neta).

irmao(I1, I2) :-
    progenitor(Pai,I1),
    progenitor(Pai,I2),
    I1 \= I2.

tio(Tio,Sobrinho) :-
    irmao(Tio,Pai),
    progenitor(Pai,Sobrinho).
