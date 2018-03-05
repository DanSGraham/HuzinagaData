%LindaWorkers=ic-node0237
%Mem=11800mb
%NProcShared=8
%chk=dimer.chk
# Opt=(Z-mat,maxcycle=200) m06/def2svp Integral=SuperFineGrid

C12H24

0 1
C  
C   1 B1
H   1 B2 2 A2
H   1 B3 2 A3 3 D3
H   1 B4 2 A4 3 D4
C   2 B5 1 A5 3 D5
H   2 B6 1 A6 3 D6
H   2 B7 1 A7 3 D7
C   6 B8 2 A8 1 D8
H   6 B9 2 A9 1 D9
H   6 B10 2 A10 1 D10
C   9 B11 6 A11 2 D11
H   9 B12 6 A12 2 D12
H   9 B13 6 A13 2 D13
C   12 B14 9 A14 6 D14
H   12 B15 9 A15 6 D15
H   12 B16 9 A16 6 D16
C   15 B17 12 A17 9 D17
H   15 B18 12 A18 9 D18
H   15 B19 12 A19 9 D19
C   18 B20 15 A20 12 D20
H   18 B21 15 A21 12 D21
H   18 B22 15 A22 12 D22
C   21 B23 18 A23 15 D23
H   21 B24 18 A24 15 D24
H   21 B25 18 A25 15 D25
C   24 B26 21 A26 18 D26
H   24 B27 21 A27 18 D27
H   24 B28 21 A28 18 D28
C   27 B29 24 A29 21 D29
H   27 B30 24 A30 21 D30
H   27 B31 24 A31 21 D31
C   30 B32 27 A32 24 D32
H   33 B33 30 A33 27 D33
H   33 B34 30 A34 27 D34
H   30 B35 27 A35 24 D35
Variables:
B1        1.52037
B2        1.09449
A2      110.26150
B3        1.09469
A3      110.99941
D3      240.26220
B4        1.09468
A4      111.00291
D4      119.74267
B5        1.52846
A5      111.49348
D5      180.02355
B6        1.09622
A6      109.14402
D6       58.46600
B7        1.09622
A7      109.14651
D7      301.57536
B8        1.52957
A8      111.33085
D8      180.06732
B9        1.09685
A9      109.56808
D9       58.69294
B10        1.09685
A10      109.56982
D10      301.43153
B11        1.52959
A11      111.32932
D11      180.04950
B12        1.09682
A12      109.56214
D12       58.69169
B13        1.09682
A13      109.57144
D13      301.40424
B14        1.52958
A14      111.33412
D14      180.11548
B15        1.09681
A15      109.56324
D15       58.75236
B16        1.09681
A16      109.56894
D16      301.46680
B17        1.52958
A17      111.32441
D17      180.06818
B18        1.09681
A18      109.56207
D18       58.71257
B19        1.09681
A19      109.57415
D19      301.42268
B20        1.52960
A20      111.33392
D20      180.12584
B21        1.09681
A21      109.56096
D21       58.76319
B22        1.09681
A22      109.57002
D22      301.47796
B23        1.53006
A23      111.33208
D23      180.06793
B24        1.09681
A24      109.55355
D24       58.71484
B25        1.09681
A25      109.57481
D25      301.41764
B26        1.52997
A26      111.27387
D26      180.07455
B27        1.09745
A27      109.45602
D27       58.51678
B28        1.09744
A28      109.49820
D28      301.54273
B29        1.50175
A29      111.29171
D29      180.59371
B30        1.09690
A30      109.65896
D30       57.82495
B31        1.09657
A31      109.82846
D31      300.67130
B32        1.33889
A32      124.10415
D32      241.95558
B33        1.08555
A33      121.75919
B34        1.08571
A34      120.74880
B35        1.08828
A35      116.90896
D35       62.58421

D33      135.00000
D34      315.00000

