%LindaWorkers=ic-node0375
%NProcShared=8
%Mem=11800mb
%chk=20170630_augccpVTZ_ccsdt_flourohexa135triene.chk
# opt freq ccsd(t)/aug-cc-pvtz geom=connectivity

1flouro-hexene

0 1
 C                 -5.11402447    2.11003528   -0.31090942
 H                 -6.14890846    2.37597250   -0.25440709
 C                 -4.74666376    0.80602320   -0.27676794
 H                 -5.49149760    0.04237591   -0.19330912
 C                 -3.25720441    0.42327252   -0.35808691
 H                 -2.51237070    1.18691972   -0.44154764
 C                 -2.88984343   -0.88073938   -0.32394134
 H                 -3.63467737   -1.64438673   -0.24048404
 C                 -1.40038390   -1.26348993   -0.40525747
 H                 -0.65555015   -0.49984271   -0.48871778
 C                 -1.03302276   -2.56750172   -0.37110951
 H                 -1.77785651   -3.33114894   -0.28764931
 F                 -4.17428100    3.07351538   -0.41621047
 H                  0.00186161   -2.83343869   -0.42760612

 1 2 1.0 3 2.0 13 1.0
 2
 3 4 1.0 5 1.0
 4
 5 6 1.0 7 2.0
 6
 7 8 1.0 9 1.0
 8
 9 10 1.0 11 2.0
 10
 11 12 1.0 14 1.0
 12
 13
 14

