; Astrocade Z-80 Demo Cartridge source file
;
; Revisions:
;    * January 25, 2005 - 1.0
;           - Assembles to exactly cartridge binary
;    * January 24, 2004 - .11
;           - Finished retyping the source code
;           - Assembled with no errors
;    * January 18, 2004 - .01
;           - Finished typing in graphics
;
;  To assemble this Z-80 source code using ZMAC:
;
;  zmac -d -o <outfile> -x <listfile> <filename>
;
;  For example, assemble this Astrocade Z-80 ROM file:
;
;  zmac -i -m -o democart.bin -x democart.lst democart.asm
;
;
;
;
;
;
;
;
;                                   XX
;                                  XXXX
;              XXXXXXX            XX XX
;            XX     XXXX          XX X   X
;          XX        XXX         XX  X  X X
;        XXX     X    XXX       XX  X  XX X
;       XX     XX    XXX        XX  X  XX X
;      XXX    XX     XXX        XX  X XX XX     XX
;     XXX     XX    XXXX       XX  X  XX XX XX  XX
;     XX     XX    XXXX        XX  X XX  X  XX  XX
;    XXX     XX   XXX          XX XX XX XX XXX XX
;   XXX     XXX  XXX    XXXXX XX  X  X  X  XX  XX
;   XX      XX  X      XXX    XX X  XX X   XX XXX
;  XXX      XX XXX    XXX  X  XX X  XXXX  XXX XXX
;  XX      XXX  XXX   XX  XX  XXX   XXX   XXX XX
;  XX      XXX   XXX XXX  XX  XX    X    XXXXXXX
; XXX      XX     XX XX  XXX  XX    XXXXX XX XXX
; XX      XXX    XXX XX  XX  X XXXXX XXX     XX
; XX      XXX    XX  XX XXXXXX XXX           XX
; XX      XX XX XXX   XXX XXX                XX
; XX     XXX XXXXX                          XX
; XX     XX                                 XX
;  XX   XX                                  XX
;   XXXXX
;
; DEMO CASSETTE 10/29/79
;
        INCLUDE "HVGLIB.H"
EJECT
L0000   EQU    0000H
L0013   EQU    0013H
L4C08   EQU    NORMEM+BYTEPL*77
L4C2D   EQU    4C2DH
L4C49   EQU    4C49H
L4C55   EQU    4C55H
L4D2D   EQU    4D2DH
L4D41   EQU    4D41H
L4D4B   EQU    4D4BH
L4E01   EQU    4E01H
L4E41   EQU    4E41H
L4E45   EQU    4E45H
L4E49   EQU    4E49H
L4E4F   EQU    4E4FH
L4E55   EQU    4E55H
L4F49   EQU    4F49H
L4F4C   EQU    4F4CH
L4F4D   EQU    4F4DH
L4FB4   EQU    4FB4H
L4FB5   EQU    4FB5H
L4FBF   EQU    4FBFH
;
; User Subroutine Equates
;
SR00    EQU    80H
SR02    EQU    82H
SR04    EQU    84H
SR06    EQU    86H
SR08    EQU    88H
SR10    EQU    8AH
SR12    EQU    8CH
SR14    EQU    8EH
;
        ORG    2000H
;
        JP     L241E
;
L2003   DW     MENUST     ; My menu stuff
        DW     L23F7
        DW     L2440
;
; Filler bytes to match exactly with Demo Cart 6001 ROM
;
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
;
        ORG    2019H      ; Player input vector
;
        JP     L2443
EJECT
;       "PROFESSIONAL" IN 3 X 5 CHARACTERS
;
; XXX.XXX.XXX.XXX.XXX.XXX.XXX.X.XXX.XXX.XXX.X.....
; X.X.X.X.X.X.X...X...X...X...X.X.X.X.X.X.X.X.....
; XXX.XXX.X.X.XX..XX..XXX.XXX.X.X.X.X.X.XXX.X.....
; X...XX..X.X.X...X.....X...X.X.X.X.X.X.X.X.X.....
; X...X.X.XXX.X...XXX.XXX.XXX.X.XXX.X.X.X.X.XXX...
;
L201C   DB     6,5        ; 6 bytes x 5 rows
        DB     0EEH,0EEH,0EEH,0EBH,0BBH,0A0H
        DB     0AAH,0A8H,088H,08AH,0AAH,0A0H
        DB     0EEH,0ACH,0CEH,0EAH,0ABH,0A0H
        DB     08CH,0A8H,082H,02AH,0AAH,0A0H
        DB     08AH,0E8H,0EEH,0EBH,0AAH,0B8H
;
; "the" in 5 X 7 characters
;
; ..X...X.........
; XXXXX.X.........
; ..X...XXXX.XXXX.
; ..X...X..X.XXXX.
; ..X...X..X.X....
; ..X...X..X.XXXX.
;
L203C   DB     2,7        ; 2 bytes X 7 rows
        DB     22H,0
        DB     22H,0
        DB     0FAH,0
        DB     23H,0DEH
        DB     22H,5EH
        DB     22H,50H
        DB     22H,5EH
EJECT
; "PRESENT" in modified 5 X 7 characters
;
; XXXX..XXXX..XXXXX..XXX..XXXXX.X...X.XXXX
; X..XX.X..XX.X.....X...X.X.....XX..X...X.
; X..XX.X..XX.X.....X.....X.....X.X.X...X.
; XXXX..XXXX..XXX....XXX..XXX...X..XX...X.
; X.....X.X...X.........X.X.....X...X...X.
; X.....X..X..X.....X...X.X.....X...X...X.
; X.....X...X.XXXXX..XXX..XXXXX.X...X...X.
;
L204C   DB     5,7              ; 5 BYTES X 7 ROWS
        DB     0F3H,0CFH,09CH,0FAH,02FH
        DB     09AH,068H,022H,083H,022H
        DB     09AH,068H,020H,082H,0A2H
        DB     0F3H,0CEH,01CH,0E2H,062H
        DB     082H,088H,002H,082H,022H
        DB     082H,048H,022H,082H,022H
        DB     082H,02FH,09CH,0FAH,022H
;
; "ING" in modified 5 X 7 characters
;
; X.XXX.X...X..XXX................
; ...X..XX..X.X...X...............
; ...X..X.X.X.X...................
; ...X..X..XX.X...................
; ...X..X...X.X..XX...............
; ...X..X...X.X...X...............
; ..XXX.X...X..XXX...X..X..X..X...
;
L2071   DB     4,7              ; 4 bytes X 7 rows
        DB     0BAH,027H,000H,000H
        DB     013H,028H,080H,000H
        DB     012H,0A8H,000H,000H
        DB     012H,068H,000H,000H
        DB     012H,029H,080H,000H
        DB     012H,028H,080H,000H
        DB     03AH,027H,012H,048H
EJECT
; "arca" in special block characters
;
; ................................................
; ................................................
; ................................................
; ................................................
; ......XXXXX...........XXXX............XXXX......
; .....XXXXXXX.........XXXXXX..........XXXXX......
; ....XXXXXXXXX.......XXXXXXXX........XXXXXX.....X
; ...XXXXXXXXXXX.....XXXXXXXXXX......XXXXXXX....XX
; ..XXXXXXXXXXXXX...XXXXXXXXXXXX....XXXXXXXX...XXX
; .XXXXXXXXXXXXXXX.XXXXXXXXXXXXXX..XXXXXXXXX..XXXX
; XXXXXXX...XXXXXX.XXXXX....XXXXX.XXXXXXX....XXXXX
; XXXXXX.....XXXXX.XXXXX....XXXXX.XXXXXX.....XXXXX
; XXXXX......XXXXX.XXXXX....XXXXX.XXXXX......XXXXX
; XXXXX......XXXXX.XXXXX...XXXXXX.XXXXX......XXXXX
; XXXXX......XXXXX.XXXXX..XXXXXX..XXXXX......XXXXX
; XXXXX......XXXXX.XXXXX.XXXXXX...XXXXX......XXXXX
; XXXXX......XXXXX.XXXXX.XXXXX....XXXXX......XXXXX
; XXXXX......XXXXX.XXXXX.XXXXX....XXXXXX.....XXXXX
; XXXXXX.....XXXXX.XXXXX.XXXXX....XXXXXXX....XXXXX
; .XXXXXX....XXXXX.XXXXX..XXXXX....XXXXXXXXX..XXXX
; ..XXXXXXXX.XXXXX.XXXXX..XXXXX.....XXXXXXXX...XXX
; ...XXXXXXX.XXXXX.XXXXX...XXXXX.....XXXXXXX....XX
; ....XXXXXX.XXXXX.XXXXX...XXXXX......XXXXXX.....X
; .....XXXXX.XXXXX.XXXXX....XXXXX......XXXXX......
; ......XXXX.XXXXX.XXXXX....XXXXX.......XXXX......
;
L208F   DB     6,25            ; 6 bytes X 25 rows
        DB     000H,000H,000H,000H,000H,000H
        DB     000H,000H,000H,000H,000H,000H
        DB     000H,000H,000H,000H,000H,000H
        DB     000H,000H,000H,000H,000H,000H
        DB     003H,0E0H,003H,0C0H,003H,0C0H
        DB     007H,0F0H,007H,0E0H,007H,0C0H
        DB     00FH,0F8H,00FH,0F0H,00FH,0C1H
        DB     01FH,0FCH,01FH,0F8H,01FH,0C3H
        DB     03FH,0FEH,03FH,0FCH,03FH,0C7H
        DB     07FH,0FFH,07FH,0FEH,07FH,0CFH
        DB     0FEH,03FH,07CH,03EH,0FEH,01FH
        DB     0FCH,01FH,07CH,03EH,0FCH,01FH
        DB     0F8H,01FH,07CH,03EH,0F8H,01FH
        DB     0F8H,01FH,07CH,07EH,0F8H,01FH
        DB     0F8H,01FH,07CH,0FCH,0F8H,01FH
        DB     0F8H,01FH,07DH,0F8H,0F8H,01FH
        DB     0F8H,01FH,07DH,0F0H,0F8H,01FH
        DB     0F8H,01FH,07DH,0F0H,0FCH,01FH
        DB     0FCH,01FH,07DH,0F0H,0FEH,01FH
        DB     07EH,01FH,07CH,0F8H,07FH,0CFH
        DB     03FH,0DFH,07CH,0F8H,03FH,0C7H
        DB     01FH,0DFH,07CH,07CH,01FH,0C3H
        DB     00FH,0DFH,07CH,07CH,00FH,0C1H
        DB     007H,0DFH,07CH,03EH,007H,0C0H
        DB     003H,0DFH,07CH,03EH,003H,0C0H
EJECT
; "de" in special block letters
; .......................XXXXX............
; .......................XXXXX............
; .......................XXXXX............
; .......................XXXXX............
; .XXXX.............XXXX.XXXXX.......XXXXX
; XXXXXX...........XXXXX.XXXXX......XXXXXX
; XXXXXXX.........XXXXXX.XXXXX.....XXXXXXX
; XXXXXXXX.......XXXXXXX.XXXXX....XXXXXXXX
; XXXXXXXXX.....XXXXXXXX.XXXXX...XXXXXXXXX
; XXXXXXXXXX...XXXXXXX...XXXXX..XXXXXX....
; XX...XXXXXX.XXXXXXX....XXXXX.XXXXXX.....
; X.....XXXXX.XXXXXX.....XXXXX.XXXXX......
; X.....XXXXX.XXXXXX.....XXXXX.XXXXX......
; ......XXXXX.XXXXX......XXXXX.XXXXXXXXXXX
; ......XXXXX.XXXXX......XXXXX.XXXXXXXXXXX
; ......XXXXX.XXXXX......XXXXX.XXXXXXXXXXX
; ......XXXXX.XXXXX......XXXXX.XXXXXXXXXXX
; X.....XXXXX.XXXXXX.....XXXXX.XXXXX......
; XX....XXXXX.XXXXXXX....XXXXX.XXXXXX.....
; XXX...XXXXX..XXXXXXX..XXXXXX.XXXXXXX....
; XXXXX.XXXXX...XXXXXXXXXXXXX...XXXXXXXXXX
; XXXXX.XXXXX....XXXXXXXXXXX.....XXXXXXXXX
; XXXXX.XXXXX.....XXXXXXXXX.......XXXXXXXX
; XXXXX.XXXXX......XXXXXXX.........XXXXXXX
; .XXXX.XXXXX.......XXXXX...........XXXXXX
;
L2127   DB     5,25            ; 5 bytes X 25 rows
        DB     000H,000H,001H,0F0H,000H
        DB     000H,000H,001H,0F0H,000H
        DB     000H,000H,001H,0F0H,000H
        DB     000H,000H,001H,0F0H,000H
        DB     078H,000H,03DH,0F0H,01FH
        DB     0FCH,000H,07DH,0F0H,03FH
        DB     0FEH,000H,0FDH,0F0H,07FH
        DB     0FFH,001H,0FDH,0F0H,0FFH
        DB     0FFH,083H,0FDH,0F1H,0FFH
        DB     0FFH,0C7H,0F1H,0F3H,0F0H
        DB     0C7H,0EFH,0E1H,0F7H,0E0H
        DB     083H,0EFH,0C1H,0F7H,0C0H
        DB     003H,0EFH,081H,0F7H,0FFH
        DB     003H,0EFH,081H,0F7H,0FFH
        DB     003H,0EFH,081H,0F7H,0FFH
        DB     003H,0EFH,081H,0F7H,0FFH
        DB     003H,0EFH,081H,0F7H,0FFH
        DB     083H,0EFH,0C1H,0F7H,0C0H
        DB     0C3H,0EFH,0E1H,0F7H,0E0H
        DB     0E3H,0E7H,0F3H,0F3H,0F0H
        DB     0FBH,0E3H,0FFH,0E1H,0FFH
        DB     0FBH,0E1H,0FFH,0C0H,0FFH
        DB     0FBH,0E0H,0FFH,080H,07FH
        DB     0FBH,0E0H,07FH,000H,03FH
        DB     07BH,0E0H,03EH,000H,01FH
EJECT
;                                   XX
;                                  XXXX
;              XXXXXXX            XX XX
;            XX     XXXX          XX X   X
;          XX        XXX         XX  X  X X
;        XXX     X    XXX       XX  X  XX X
;       XX     XX    XXX        XX  X  XX X
;      XXX    XX     XXX        XX  X XX XX     XX
;     XXX     XX    XXXX       XX  X  XX XX XX  XX
;     XX     XX    XXXX        XX  X XX  X  XX  XX
;    XXX     XX   XXX          XX XX XX XX XXX XX
;   XXX     XXX  XXX    XXXXX XX  X  X  X  XX  XX
;   XX      XX  X      XXX    XX X  XX X   XX XXX
;  XXX      XX XXX    XXX  X  XX X  XXXX  XXX XXX
;  XX      XXX  XXX   XX  XX  XXX   XXX   XXX XX
;  XX      XXX   XXX XXX  XX  XX    X    XXXXXXX
; XXX      XX     XX XX  XXX  XX    XXXXX XX XXX
; XX      XXX    XXX XX  XX  X XXXXX XXX     XX
; XX      XXX    XX  XX XXXXXX XXX           XX
; XX      XX XX XXX   XXX XXX                XX
; XX     XXX XXXXX                          XX
; XX     XX                                 XX
;  XX   XX                                  XX
;   XXXXX
;
L21A6   DB     6,24            ; 6 bytes X 24 rows
        DB     000H,000H,000H,000H,030H,000H
        DB     000H,000H,000H,000H,078H,000H
        DB     000H,007H,0F0H,000H,0D8H,000H
        DB     000H,018H,03CH,000H,0D1H,000H
        DB     000H,060H,01CH,001H,092H,080H
        DB     001H,0C1H,00EH,003H,026H,080H
        DB     003H,006H,01CH,003H,026H,080H
        DB     007H,00CH,01CH,003H,02DH,083H
        DB     00EH,00CH,03CH,006H,04DH,0B3H
        DB     00CH,018H,078H,006H,059H,033H
        DB     01CH,018H,0E0H,006H,0DBH,076H
        DB     038H,039H,0C3H,0ECH,092H,066H
        DB     030H,032H,007H,00DH,034H,06EH
        DB     070H,037H,00EH,04DH,03CH,0EEH
        DB     060H,073H,08CH,0CEH,038H,0ECH
        DB     060H,071H,0DCH,0CCH,021H,0FCH
        DB     0E0H,060H,0D9H,0CCH,03EH,0DCH
        DB     0C0H,0E1H,0D9H,097H,0DCH,018H
        DB     0C0H,0E1H,09BH,0F7H,000H,018H
        DB     0C0H,0DBH,08EH,0E0H,000H,018H
        DB     0C1H,0DFH,000H,000H,000H,030H
        DB     0C1H,080H,000H,000H,000H,030H
        DB     063H,000H,000H,000H,000H,030H
        DB     03EH,000H,000H,000H,000H,000H
EJECT
; "MAKES THE GAMES PEOPLE PLAY" in special 3 X 5 characters
;
; X.X.XXX.X.X.XXX.XXX...XXX.X.X.XXX...XXX.XXX.X.X.XXX.XXX....
; XXX.X.X.X.X.X...X......X..X.X.X.....X...X.X.XXX.X...X......
; XXX.X.X.XX..X...X......X..X.X.X.....X...X.X.XXX.X...X......
; X.X.XXX.X.X.XX..XXX....X..XXX.XX....X.X.XXX.X.X.XX..XXX....
; X.X.X.X.X.X.X.....X....X..X.X.X.....X.X.X.X.X.X.X.....X....
; X.X.X.X.X.X.X.....X....X..X.X.X.....X.X.X.X.X.X.X.....X....
; X.X.X.X.X.X.XXX.XXX....X..X.X.XXX...XXX.X.X.X.X.XXX.XXX....
;
; XXX.XXX.XXX.XXX.X...XXX...XXX.X...XXX.X.X....
; X.X.X...X.X.X.X.X...X.....X.X.X...X.X.X.X....
; XXX.X...X.X.XXX.X...X.....XXX.X...X.X.X.X....
; X...XXX.X.X.X...X...XXX...X...X...XXX..X.....
; X...X...X.X.X...X...X.....X...X...X.X..X.....
; X...X...X.X.X...X...X.....X...X...X.X..X.....
; X...XXX.XXX.X...XXX.XXX...X...XXX.X.X..X.....
;
L2238   DB     13,7            ; 13 bytes X 7 rows
        DB     0AEH,0AEH,0E3H,0ABH,08EH,0EAH,0EEH
        DB     01DH,0DDH,0D1H,0C7H,047H,050H
        DB     0EAH,0A8H,081H,02AH,008H,0AEH,088H
        DB     015H,015H,051H,005H,045H,050H
        DB     0EAH,0C8H,081H,02AH,008H,0AEH,088H
        DB     01DH,015H,0D1H,007H,045H,050H
        DB     0AEH,0ACH,0E1H,03BH,00AH,0EAH,0CEH
        DB     011H,095H,011H,084H,047H,020H
        DB     0AAH,0A8H,021H,02AH,00AH,0AAH,082H
        DB     011H,015H,011H,004H,045H,020H
        DB     0AAH,0A8H,021H,02AH,00AH,0AAH,082H
        DB     011H,015H,011H,004H,045H,020H
        DB     0AAH,0AEH,0E1H,02BH,08EH,0AAH,0EEH
        DB     011H,0DDH,01DH,0C4H,075H,020H
EJECT
; "VIDEOCADES" in large block letters
;
L2295   DB     16,22             ; 16 bytes X 22 rows
; |Byte 1||Byte 2||Byte 3||Byte 4||Byte 5||Byte 6||Byte 7||Byte 8|
; .............................XXXX...............................
; .............................XXXX...............................
; .............................XXXX...............................
; .............................XXXX...............................
; XXXX....XXXX....X.......XXXX.XXXX.......XXXX.......XXX..........
; XXXX....XXXX...XX......XXXXX.XXXX......XXXXX......XXXXX.........
; XXXX....XXXX..XXX.....XXXXXX.XXXX.....XXXXXX.....XXXXXXX........
; XXXX....XXXX.XXXX....XXXXXXX.XXXX....XXXXXXX....XXXXXXXXX.......
; XXXX....XXXX.XXXX...XXXXXXXX.XXXX...XXXXX......XXXXXXXXXXX.....X
; XXXX....XXXX.XXXX..XXXXX.....XXXX..XXXXX......XXXXX...XXXXX...XX
; XXXX....XXXX.XXXX.XXXXX......XXXX.XXXXX......XXXXX.....XXXXX.XXX
; XXXX....XXXX.XXXX.XXXX.......XXXX.XXXXXXXXXX.XXXX.......XXXX.XXX
; XXXX....XXXX.XXXX.XXXX.......XXXX.XXXXXXXXXX.XXXX.......XXXX.XXX
; XXXX....XXXX.XXXX.XXXX.......XXXX.XXXXXXXXXX.XXXX.......XXXX.XXX
; XXXX...XXXXX.XXXX.XXXX.......XXXX.XXXXXXXXXX.XXXX.......XXXX.XXX
; XXXX..XXXXXX.XXXX.XXXXX......XXXX.XXXXX......XXXXX.....XXXXX.XXX
; XXXX XXXXXXX.XXXX..XXXXX....XXXXX..XXXX.......XXXXX...XXXXX...XX
; XXXXXXXXXX...XXXX...XXXXXXXXXXXX....XXXX.......XXXXXXXXXXX.....X
; XXXXXXXXX....XXXX....XXXXXXXXXX......XXXXXXX....XXXXXXXXX.......
; XXXXXXXX.....XXX......XXXXXXXX........XXXXXX.....XXXXXXX........
; XXXXXXX......XX........XXXXXX..........XXXXX......XXXXX.........
; XXXXXX.......X..........XXXX............XXXX.......XXX..........
;
; |Byte 9||Byte10||Byte11||Byte12||Byte13||Byte14||Byte15||Byte16|
; ..................................XXXX..........................
; ..................................XXXX..........................
; ..................................XXXX..........................
; ..................................XXXX..........................
; ...XXXX......XXXX............XXXX.XXXX.......XXXX....XXXXXX.....
; ..XXXXX.....XXXXXX..........XXXXX.XXXX......XXXXX...XXXXXXXX....
; .XXXXXX....XXXXXXXX........XXXXXX.XXXX.....XXXXXX..XXXXXXXXXX...
; XXXXXXX...XXXXXXXXXX......XXXXXXX.XXXX....XXXXXXX.XXXXXXXXXXXX..
; XXXX.....XXXXXXXXXXXX....XXXXXXXX.XXXX...XXXXX....XXXX..........
; XXX.....XXXXXX...XXXXX..XXXXX.....XXXX..XXXXX.....XXXX..........
; XX.....XXXXXX.....XXXX.XXXXX......XXXX.XXXXX......XXXX..........
; XX.....XXXXX......XXXX.XXXX.......XXXX.XXXXXXXXXX.XXXXXXXXX.....
; XX.....XXXXX......XXXX.XXXX.......XXXX.XXXXXXXXXX..XXXXXXXXX....
; XX.....XXXXX......XXXX.XXXX.......XXXX.XXXXXXXXXX...XXXXXXXXX...
; XX.....XXXXX......XXXX.XXXX.......XXXX.XXXXXXXXXX....XXXXXXXXX..
; XX.....XXXXXX.....XXXX.XXXXX......XXXX.XXXXX..............XXXX..
; XXX.....XXXXXX....XXXX..XXXXX....XXXXX..XXXXX.............XXXX..
; XXXX.....XXXXXXXX.XXXX...XXXXXXXXXXXX....XXXXX............XXXX..
; XXXXXXX...XXXXXXX.XXXX....XXXXXXXXXX......XXXXXXX.XXXXXXXXXXXX..
; .XXXXXX....XXXXXX.XXXX.....XXXXXXXX........XXXXXX..XXXXXXXXXX...
; ..XXXXX.....XXXXX.XXXX......XXXXXX..........XXXXX...XXXXXXXX....
; ...XXXX......XXXX.XXXX.......XXXX............XXXX....XXXXXX.....

; Row 1
        DB     000H,000H,000H,007H,080H,000H,000H,000H
        DB     000H,000H,000H,000H,03CH,000H,000H,000H
; Row 2
        DB     000H,000H,000H,007H,080H,000H,000H,000H
        DB     000H,000H,000H,000H,03CH,000H,000H,000H
; Row 3
        DB     000H,000H,000H,007H,080H,000H,000H,000H
        DB     000H,000H,000H,000H,03CH,000H,000H,000H
; Row 4
        DB     000H,000H,000H,007H,080H,000H,000H,000H
        DB     000H,000H,000H,000H,03CH,000H,000H,000H
; Row 5
        DB     0F0H,0F0H,080H,0F7H,080H,0F0H,01CH,000H
        DB     01EH,007H,080H,007H,0BCH,007H,087H,0E0H
; Row 6
        DB     0F0H,0F1H,081H,0F7H,081H,0F0H,03EH,000H
        DB     03EH,00FH,0C0H,00FH,0BCH,00FH,08FH,0F0H
; Row 7
        DB     0F0H,0F3H,083H,0F7H,083H,0F0H,07FH,000H
        DB     07EH,01FH,0E0H,01FH,0BCH,01FH,09FH,0F8H
; Row 8
        DB     0F0H,0F7H,087H,0F7H,087H,0F0H,0FFH,080H
        DB     0FEH,03FH,0F0H,03FH,0BCH,03FH,0BFH,0FCH
; Row 9
        DB     0F0H,0F7H,08FH,0F7H,08FH,081H,0FFH,0C1H
        DB     0F0H,07FH,0F8H,07FH,0BCH,07CH,03CH,000H
; Row 10
        DB     0F0H,0F7H,09FH,007H,09FH,003H,0E3H,0E3H
        DB     0E0H,0FCH,07CH,0F8H,03CH,0F8H,03CH,000H
; Row 11
        DB     0F0H,0F7H,0BEH,007H,0BEH,007H,0C1H,0F7H
        DB     0C1H,0F8H,03DH,0F0H,03DH,0F0H,03CH,000H
; Row 12
        DB     0F0H,0F7H,0BCH,007H,0BFH,0F7H,080H,0F7H
        DB     0C1H,0F0H,03DH,0E0H,03DH,0FFH,0BFH,0E0H
; Row 13
        DB     0F0H,0F7H,0BCH,007H,0BFH,0F7H,080H,0F7H
        DB     0C1H,0F0H,03DH,0E0H,03DH,0FFH,09FH,0F0H
; Row 14
        DB     0F0H,0F7H,0BCH,007H,0BFH,0F7H,080H,0F7H
        DB     0C1H,0F0H,03DH,0E0H,03DH,0FFH,08FH,0F8H
; Row 15
        DB     0F1H,0F7H,0BCH,007H,0BFH,0F7H,080H,0F7H
        DB     0C1H,0F0H,03DH,0E0H,03DH,0FFH,087H,0FCH
; Row 16
        DB     0F3H,0F7H,0BEH,007H,0BEH,007H,0C1H,0F7H
        DB     0C1H,0F8H,03DH,0F0H,03DH,0F0H,000H,03CH
; Row 17
        DB     0F7H,0E7H,09FH,00FH,09FH,003H,0E3H,0E3H
        DB     0E0H,0FCH,03CH,0F8H,07CH,0F8H,000H,03CH
; Row 18
        DB     0FFH,0C7H,08FH,0FFH,00FH,081H,0FFH,0C1H
        DB     0F0H,07FH,0BCH,07FH,0F8H,07CH,000H,03CH
; Row 19
        DB     0FFH,087H,087H,0FEH,007H,0F0H,0FFH,080H
        DB     0FEH,03FH,0BCH,03FH,0F0H,03FH,0BFH,0FCH
; Row 20
        DB     0FFH,007H,003H,0FCH,003H,0F0H,07FH,000H
        DB     07EH,01FH,0BCH,01FH,0E0H,01FH,09FH,0F8H
; Row 21
        DB     0FEH,006H,001H,0F8H,001H,0F0H,03EH,000H
        DB     03EH,00FH,0BCH,00FH,0C0H,00FH,08FH,0F0H
; Row 22
        DB     0FCH,004H,000H,0F0H,000H,0F0H,01CH,000H
        DB     01EH,007H,0BCH,007H,080H,007H,087H,0E0H
EJECT
L23F7   DB     'DEMO',0
;
L23FC   DB     'PLAY A GAME'
        DB     67H             ; Load DE, C
        DB     8,88            ; DE = Column 8, Row 88
        DB     00001101B       ; C = Display Control
        DB     '(C) BALLY MFG 1977',0
EJECT
; ********************************************************
; *                                                      *
; *                COLD START ENTRACE                    *
; *                                                      *
; *       Entered upon ARCADE power-up or RESET          *
; *                                                      *
; ********************************************************
;
L241E   LD     SP,MUZPC
        SYSTEM INTPC
        DO     SETB
        DB     0FFH
        DW     TIMOUT          ; Reset timeout value
;
        DO     SETB
        DB     0AAH
        DW     SENFLG          ; Sentry calls to me
        DO     SETW
        DW     0FF00H
        DW     USERTB
;
        DO     EMUSIC          ; Kill music
;
        DO     SETOUT
        DB     191             ; Vertical Update register
        DB     00101001B       ; Border Color, Left scrn size
        DB     8               ; Only line interrupts
;
        DO     COLSET
        DW     L0013           ; Use on-board Color Table
;
        DO     ACTINT          ; Do some interrupts
;
        EXIT                   ; Done interrupting
;
        SYSSUK MENU            ; Do come menu stuff
        DW     L23FC           ; "PLAY A GAME"
        DW     L2003           ; My menu start
;
EJECT
; Menu selection vector
;
L2440   JP     L2446
;
; SENTRY vector when DEMO cassette in control
;
L2443   JP     L29AB           ; Player input vector
;
; Here starts the presentation
;       Entered upon MENU selection
;
L2446   LD     SP,L4FB4
        CALL   L2955
        SYSTEM INTPC           ; Start interpreter
;
        DO     EMUSIC          ; Stop music
;
        DO     ACTINT          ; Start interrupts
;
; We shall begin the demonstration with a musical selection by
; Bach.  The selection is a Fugue with 2 major melodies and
; will be the background music while advertising the features
; of the BALLY ARCADE
;
L2450   DO     BMUSIC          ; Start background music
        DW     L4FBF           ; Work area
        DB     0C0H            ; One note
        DW     L2C01           ; Music start
;
        DO     SR02            ; My SR 02
        DW     L2A84           ; New color info
;
; Now present the first screen
;
        DO     SR08            ; Display "BALLY" in script
        DB     32,32           ; H/V dot number
        DB     8,8
        DW     L21A6
;
        DO     SR08            ; Display "PROFESSIONAL" in 3x5
        DB     52,59           ; H/V dot number
        DB     4,8
        DW     L201C
;
        DO     SR08            ; Display "arca" in large block
        DB     52,61           ; Position
        DB     0CH,18H
        DW     L208F
;
        DO     SR08            ; Display "DE" in large block
        DB     100,61          ; Position
        DB     0CH,08H
        DW     L2127
;
        DO     SR08            ; Display "PRESENT" in 5x7 char
        DB     4,4             ; Position
        DB     0CH,08H
        DW     L204C
;
        DO     SR08             ; Display "ING...." in 5x7 char
        DB     44,4             ; Position
        DB     0CH,08H
        DW     L2071
;
        DO     SR08             ; Display "the" in 5x7 char
        DB     15,23            ; Position
        DB     04H,08H
        DW     L203C
;
; The first screen is completed.  We will display it and pause
; for 2 seconds before generating the 2nd display.
;
        DO     SR12            ; New left screen size
        DB     41
;
        DONT   SR06            ; 2 second display
;
; We are ready to generate the second screen.  First we kill the
; display update register so our actions are hidden.
;
        DO     SR04            ; New Vertical Update Register
        DB     0               ; Display nothing
;
        DO     SR12            ; New left screen size
        DB     41
;
        DO     SR08            ; Display "BALLY" in script
        DB     10,1            ; Position
        DB     08H,08H
        DW     L21A6
;
        DO     SR08            ; Display "PROFESSIONAL" in 3x5
        DB     66,1            ; Position
        DB     04H,08H
        DW     L201C
;
        DO     SR08            ; Display "arca" in large block
        DB     66,3            ; Position
        DB     0CH,18H
        DW     L208F
;
        DO     SR08            ; Display "de" in large block
        DB     114,3           ; Position
        DB     0CH,18H
        DW     L2127
;
        DO     RECTAN          ; Display solid color
        DB     0,30            ; V, H position
        DB     160,2           ; 2 high x 160 wide
        DB     55H             ; Pixel pattern
;
; All the graphics for the second screen have been generated.
; The display in the upper portion of the screen will remain
; while the messages are displayed and scrolled up in the
; lower part of the screen.  Now we will generate the first
; 3 messages, display the upper screen and 1st message by
; changing the vertical update register, pause 1 1/2 seconds
; and display the 2nd message followed by another pause
; before the 3rd message.  After the pause from the 3rd
; message, all others are scrolled up.
;
        DO    SR00             ; String display
        DB    1,34             ; DE=
        DB    18H              ; C=
        DW    L24BC            ; HL=
;
        DO    MJUMP            ; Macro jump
        DW    L24CC
;
L24BC   DB    '* 1-TO-4 PLAYER',0
;
L24CC   DO    SR00             ; String display
        DB    13,42
        DB    18H
        DW    L24D5
;
        DO    MJUMP            ; Macro jump
        DW    L24E7
;
L24D5   DB    'PROGRAMMABLE UNIT',0
;
L24E7   DO    SR00             ; String display
        DB    1,54
        DB    14H
        DW    L24EE
;
        DO    MJUMP            ; Macro jump
        DW    L2507
;
L24EE   DB    '* EXCLUSIVE 5-FUNCTION',0
;
L2507   DO    SR00             ; String display
        DB    13,62
        DB    14H
        DW    L2510
;
        DO    MJUMP            ; Macro jump
        DW    L2525
;
L2510   DB    '10-MEMORY CALCULATOR',0
;
L2525   DO    SR00             ; String display
        DB    1,74
        DB    1CH
        DW    L252E
;
        DO    MJUMP            ; Macro jump
        DW    L2546
;
L252E   DB    '* ON-SCREEN INSTRUCTION',0
;
L2546   DO    SR00             ; String display
        DB    13,82
        DB    1CH
        DW    L254F
;
        DO    MJUMP            ; Macro jump
        DW    L255B
;
L254F   DB    'AND SCORING',0
;
; Now display the upper screen with the 1st message and pause
; before displaying the other 2 messages.
;
L255B   DO    SR04             ; Vertical update register
        DB    106
;
        DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR04             ; Vertical Update Register
        DB    146
;
        DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR04             ; Vertical Update Register
        DB    196
;
        DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR10             ; Scroll screen up
        DB    40               ; # lines to scroll
;
        DO    SR00             ; Display
        DB    1,54
        DB    14H
        DW    L2572
;
        DO    MJUMP            ; Macro jump
        DW    L2589
;
L2572   DB    '* GUNFIGHT, CHECKMATE,',0
;
L2589   DO    SR00             ; String display
        DB    13,62
        DB    14H
        DW    L2592
;
        DO    MJUMP            ; Macro jump
        DW    L25A7
;
L2592   DB    'AND SCRIBBLING GAMES',0
;
L25A7   DO    SR00             ; String display
        DB    13,70
        DB    14H
        DW    L25B0
;
        DO    MJUMP            ; Macro jump
        DW    L25B9
;
L25B0   DB    'BUILT IN',0
;
L25B9   DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR00             ; String display
        DB    1,82
        DB    18H
        DW    L25C4
;
        DO    MJUMP            ; Macro jump
        DW    L25DA
;
L25C4   DB    '* 360  PLAYER CONTROL',0
;
L25DA   DO    SR08             ; Display degrees symbol
        DB    32,82
        DB    8,18H
        DW    L2AB5
;
        DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR10             ; scroll screen up
        DB    20               ; # of lines to scroll
;
        DO    SR00             ; String display
        DB    1,74
        DB    1CH
        DW    L25EE
;
        DO    MJUMP            ; Macro jump
        DW    L2606
;
L25EE   DB    '* 256 OBTAINABLE COLORS',0
;
L2606   DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR10             ; Scroll up
        DB    28               ; # of lines to scroll
;
        DO    SR00             ; String display
        DB    1,58
        DB    18H
        DW    L2613
;
        DO    MJUMP            ; Macro jump
        DW    L262A
;
L2613   DB    '* LIFE-LIKE CHARACTERS',0
;
L262A   DO    SR00             ; String display
        DB    013,66
        DB    18H
        DW    L2633
;
        DO    MJUMP            ; Macro jump
        DW    L2641
;
L2633   DB    'AND ANIMATION',0
;
L2641   DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR00             ; String display
        DB    1,78
        DB    14H
        DW    L264C
;
        DO    MJUMP            ; Macro jump
        DW    L2663
;
L264C   DB    '* UNIQUE TONES & TUNES',0
;
L2663   DO    PAWS             ; Pause
        DB    90               ; 1 1/2 seconds
;
        DO    SR10             ; Scroll screen up
        DB    12               ; # of lines to scroll
;
        DO    SR00             ; String display
        DB    1,78
        DB    18H
        DW    L2670
;
        DO    MJUMP            ; Macro jump
        DW    L2686
;
L2670   DB    '* OPTIONAL VIDEOCADES',0
;
L2686   DO    SR00             ; String display
        DB    13,86
        DB    18H
        DW    L268F
;
        DO    MJUMP            ; Macro jump
        DW    L2699
;
L268F   DB    'AVAILABLE',0
;
; Now we give spectators 2 seconds to absorb the screen
; before starting the demo of the built-in features.
;
L2699   DONT  SR06             ; wait 2 seconds
;
        DO    SR02             ; New colors
        DW    L2A94
;
        DO    SR00             ; String display
        DB    32,40
        DB    5CH
        DW    L26A6
;
        DO    MJUMP            ; Macro jump
        DW    L26AF
;
L26A6   DB    'GUNFIGHT',0
;
L26AF   DO    SR12             ; New left screen size
        DB    41
;
        DO    SR14
        DB    0
        DW    L2ABA            ; Gunfight SENTRY table
;
; GUNFIGHT returns here so we may demonstrate the
; next built-in game.
;
L26B5   DO    SR02             ; New colors
        DW    L2A94
;
        DO    SR00             ; String display
        DB    24,40
        DB    5CH
        DW    L26C1
;
        DO    MJUMP            ; Macro jump
        DW    L26CB
;
L26C1   DB    'CHECKMATE',0
;
L26CB   DO    SR12             ; New left screen size
        DB    41
;
        DO    SR14
        DB    1
        DW    L2AF6            ; Checkmate SENTRY table
;
; Checkmate returns here so we can demonstrate
; the next on-board game
;
L26D1   DO    SR02             ; New colors
        DW    L2A94
;
        DO    SR00             ; String display
        DB    16,40
        DB    5CH
        DW    L26DD
;
        DO    MJUMP            ; Macro jump
        DW    L26E8
;
L26DD   DB    'SCRIBBLING',0
;
L26E8   DO    SR12             ; New left screen size
        DB    41
;
        DO    SR14
        DB    3
        DW    L2BEC            ; Scribbling SENTRY table
;
; Scribbling returns here so we may demonstrate the
; next built-in game
;
L26EE   DO    SR02             ; New colors
        DW    L2A94
;
        DO    SR00             ; String display
        DB    4,40
        DB    1CH
        DW    L26FA
;
        DO    MJUMP            ; Macro jump
        DW    L2708
;
L26FA   DB    '* 5-FUNCTION,',0
;
L2708   DO    SR00             ; String display
        DB    16,48
        DB    1CH
        DW    L2711
;
        DO    MJUMP            ; Macro jump
        DW    L2726
;
L2711   DB    '10-MEMORY CALCULATOR',0
;
L2726   DO    SR00             ; String display
        DB    16,56
        DB    1CH
        DW    L272F
;
        DO    MJUMP            ; Macro jump
        DW    L2738
;
L272F   DB    'BUILT-IN',0
;
L2738   DO    SR12             ; New Left screen size
        DB    41
;
        DO    SR14
        DB    2
        DW    L2B08            ; Calculator SENTRY table
;
; Calculator returns here so we may wind up the
; demonstration
;
L273E   DO    SR02             ; New colors
        DW    L2A88
;
        DO    SR08
        DB    20,2
        DB    4,8
        DW    L2295
;
        DO    RECTAN
        DB    134,2            ; H/V dot number
        DB    14,22            ; # H/V dots
        DB    0                ; Data
;
        DO    SR00             ; String display
        DB    24,45
        DB    1CH
        DW    L2757
;
        DO    MJUMP            ; Macro jump
        DW    L276A
;
L2757   DB    'ELECTRONIC PROGRAM',0
;
L276A   DO    SR00             ; String display
        DB    24,70
        DB    1CH
        DW    L2773
;
        DO    MJUMP            ; Macro jump
        DW    L277D
;
L2773   DB    'CASSETTES',0
;
L277D   DO    SR12             ; New left screen size
        DB    41
;
        DONT  SR06
;
        DO    SR02             ; New colors
        DW    L2A80
;
        DO    SR08
        DB    12,2
        DB    4,8
        DW    L2295
;
        DO    SR12             ; New left screen size
        DB    41
;
        DO    SR00             ; String display
        DB    12,30
        DB    18H
        DW    L2795
;
        DO    MJUMP            ; Macro Jump
        DW    L27A2
;
L2795   DB    'SPORT SERIES',0
;
L27A2   DO    SR00             ; String display
        DB    12,40
        DB    1CH
        DW    L27AB
;
        DO    MJUMP            ; Macro jump
        DW    L27B6
;
L27AB   DB    '* BASEBALL',0
;
L27B6   DO    SR00             ; String display
        DB    12,50
        DB    1CH
        DW    L27BF
;
        DO    MJUMP            ; Macro jump
        DW    L27C8
;
L27BF   DB    '* TENNIS',0
;
L27C8   DO    SR00             ; String display
        DB    12,60
        DB    1CH
        DW    L27D1
;
        DO    MJUMP            ; Macro jump
        DW    L27DA
;
L27D1   DB    '* HOCKEY',0
;
L27DA   DO    SR00             ; String display
        DB    12,70
        DB    1CH
        DW    L27E3
;
        DO    MJUMP            ; Macro jump
        DW    L27EE
;
L27E3   DB    '* HANDBALL',0
;
L27EE   DO    PAWS             ; Pause
        DB    200              ; 1 minute, 40 seconds
;
        DO    MCALL            ; Call interpreter subroutine
        DW    L2AAE
;
        DO    SR00             ; String display
        DB    12,30
        DB    18H
        DW    L27FC
;
        DO    MJUMP            ; Macro jump
        DW    L280F
;
L27FC   DB    'EDUCATIONAL SERIES',0
;
L280F   DO    SR00             ; String display
        DB    12,40
        DB    1CH
        DW    L2818
;
        DO    MJUMP            ; Macro jump
        DW    L2825
;
L2818   DB    '* SPEED MATH',0
;
L2825   DO    SR00             ; String display
        DB    12,50
        DB    1CH
        DW    L282E
;
        DO    MJUMP            ; Macro jump
        DW    L283B
;
L282E   DB    '* BINGO MATH',0
;
L283B   DO    SR00             ; String display
        DB    12,60
        DB    1CH
        DW    L2844
;
        DO    MJUMP            ; Macro Jump
        DW    L284F
;
L2844   DB    '* SCRAMBLE',0
;
L284F   DO    SR00             ; String display
        DB    12,70
        DB    1CH
        DW    L2858
;
        DO    MJUMP            ; Macro jump
        DW    L2864
;
L2858   DB    '* WORD HUNT',0
;
L2864   DO    SR00             ; String display
        DB    12,80
        DB    1CH
        DW    L286D
;
        DO    MJUMP            ; Macro jump
        DW    L287C
;
L286D   DB    '* LETTER MATCH',0
;
L287C   DO    PAWS             ; Pause
        DB    225              ; 3 3/4 seconds
;
        DO    MCALL            ; Call interpreter subroutine
        DW    L2AAE
;
        DO    SR00             ; String display
        DB    12,30
        DB    18H
        DW    L288A
;
        DO    MJUMP            ; Macro jump
        DW    L289E
;
L288A   DB    'ACTION/SKILL SERIES',0
;
L289E   DO    SR00             ; String display
        DB    12,40
        DB    1CH
        DW    L28A7
;
        DO    MJUMP            ; Macro jump
        DW    L28B1
;
L28A7   DB    '* SEAWOLF',0
;
L28B1   DO    SR00             ; String display
        DB    12,50
        DB    1CH
        DW    L28BA
;
        DO    MJUMP            ; Macro jump
        DW    L28C7
;
L28BA   DB    '* BOMBARDIER',0
;
L28C7   DO    SR00             ; String display
        DB    12,60
        DB    1CH
        DW    L28D0
;
        DO    MJUMP            ; Macro jump
        DW    L28E0
;
L28D0   DB    '* PANZER ATTACK',0
;
L28E0   DO    SR00             ; String display
        DB    12,70
        DB    1CH
        DW    L28E9
;
        DO    MJUMP            ; Macro jump
        DW    L28F5
;
L28E9   DB    '* RED BARON',0
;
L28F5   DO    PAWS             ; Paws
        DB    200              ; 3 1/3 seconds
;
        DO    MCALL            ; Call interpreter subroutine
        DW    L2AAE
;
        DO    SR00             ; String display
        DB    12,30
        DB    18H
        DW    L2903
;
        DO    MJUMP            ; Macro jump
        DW    L2913
;
L2903   DB    'STRATEGY SERIES',0
;
L2913   DO    SR00             ; String display
        DB    12,40
        DB    1CH
        DW    L291C
;
        DO    MJUMP            ; Macro jump
        DW    L2928
;
L291C   DB    '* BLACKJACK',0
;
L2928   DO    SR00             ; String display
        DB    12,50
        DB    1CH
        DW    L2931
;
        DO    MJUMP            ; Macro jump
        DW    L2939
;
L2931   DB    '* POKER',0
;
L2939   DO    SR00             ; String display
        DB    12,60
        DB    1CH
        DW    L2942
;
        DO    MJUMP            ; Macro jump
        DW    L2950
;
L2942   DB    '* ACEY-DEUCEY',0
;
; End of demonstration
; Wait 2 seconds then system reset
;
L2950   DONT  SR06
;
        EXIT                   ; Finally done!!!!!
;
L2952   JP    L0000
EJECT
L2955   LD    A,95*2+1         ; Vertical size
        OUT   (VERBL),A        ; Vertical Update Register
        XOR   A
        OUT   (HORCB),A        ; Horizontal Color boundary
        LD    BC,BYTEPL*98
        LD    DE,NORMEM
        SYSTEM FILL
        LD    DE,L4FB4
        LD    HL,FNTSYS
        LD    BC,7             ; 7 byte table
        LDIR
        LD    A,6
        LD    (L4FB5),A        ; 6 pixels wide
        LD    A,160
        LD    (L4FB4),A        ; Change offset value
        LD    HL,L298C-128
        LD    (USERTB),HL      ; Initialize SR table
        LD    HL,L299C-64
        LD    (UMARGT),HL      ; Initialize SR load table
        RET
;
SR004   OUT   (VERBL),A        ; Update Vertical blanking
        RET
;
SR012   OUT   (HORCB),A        ; Horizontal Color boundary
        RET
;
L298C   DW    SR000            ; SR00 - String display
        DW    SR002            ; SR02 - Set new color values
        DW    SR004            ; SR04 - Set vertical update
        DW    SR006            ; SR06 - 2 second delay
        DW    SR008            ; SR08 - Display CRT data
        DW    SR010            ; SR10 - Scroll Screen up
        DW    SR012            ; SR12 - New left screen size
        DW    SR014            ; SR14 -
;
L299C   DB    11000111B        ; SR00 - E,D,C,L,H
        DB    11000000B        ; SR02 - L,H
        DB    00100000B        ; SR04 - A
        DB    00000000B        ; SR06 - none
        DB    11001111B        ; SR08 - E,D,C,B,L,H
        DB    00001000B        ; SR10 - B
        DB    00100000B        ; SR12 - A
        DB    11100000B        ; SR14 - A,L,H
;
SR008   LD    A,C
        OUT   (XPAND),A        ; Expander port
;
; Bits 0 & 1 define the expansion of a 0 on the data bus.
; Bits 1 & 2 define the expansion of a 1 on the data bus.
;
        LD    A,B
        SYSTEM WRITP           ; Write w/pattern size lookup
        RET
;
; User Player input routine
;
L29AB   LD    HL,USERTB
        LD    A,(HL)
        OR    A
        INC   HL
        JR    Z,L29BD
        LD    A,(HL)
        OR    A
        JR    Z,L29DE
        DEC   (HL)
        LD    (IY+CBA),1
        RET
;
L29BD   XOR   A               ; Allow SENTRY to process
        LD    (SENFLG),A
        SYSTEM SENTRY
        LD    C,A
        LD    A,0AAH           ; Reset switch for me
        LD    (SENFLG),A
        LD    A,(HL)
        CP    0F1H
        JP    C,L2446
        LD    A,C
        CP    SKYD             ; Key down
        JR    C,L29F5
        CP    SP0
        JR    NC,L29F5
        LD    A,0FFH
        LD    (HL),A
        LD    A,C
        JR    L29F5
;
L29DE   LD    DE,(UMARGT)      ; Get argument pointer
        LD    A,(DE)
        OR    A
        JR    Z,L2A04
        CP    0FEH
        JR    NZ,L29EB
        DI
L29EB   LD    (HL),A           ; Save @ USERTB+1
        EX    DE,HL
        INC   HL
        LD    A,(HL)           ; Arg 1 Device #
        INC   HL
        LD    B,(HL)           ; Arg 2 Value
        INC   HL
        LD    (UMARGT),HL      ; Save new argument pointer
L29F5   CP    SSEC
        JR    NZ,L29FD
        LD    HL,USERTB+1
        DEC   (HL)
L29FD   LD    (IY+CBB),B       ; Return device value
        LD    (IY+CBA),A       ; Return device code
        RET
;
L2A04   DI
        XOR   A
        LD    (SENFLG),A       ; Allow SENTRY to work
        LD    SP,L4FB4
        INC   DE
        EX    DE,HL
        LD    E,(HL)
        INC   HL
        LD    H,(HL)
        LD    L,E
        EXX
        CALL  L2955
        EXX
        SYSTEM INTPC
;
        DO    EMUSIC
;
        DO    ACTINT           ; Start interrupts
;
        DONT  MJUMP            ; Macro jump
;
SR014   LD    (UMARGT),HL      ; Save Arg table pointer
        LD    HL,MENUST        ; Get on-board menu start
L2A22   OR    A
        JR    Z,L2A2C          ; Zero means we're there
L2A25   LD    D,(HL)           ; Get link to next menu
L2A26   INC   HL
L2A27   LD    H,(HL)
        LD    L,D
        DEC   A                ; Decrement Menu pointer
        JR    L2A22
;
L2A2C   INC   HL
        INC   HL
        LD    E,(HL)           ; Get adrs of menu literal
        INC   HL               ;  to DE
        LD    D,(HL)
        INC   HL
        LD    B,(HL)           ; Get Game start adrs
        INC   HL               ; to HL
        LD    H,(HL)
        LD    L,B
        PUSH  HL               ; Save Game Start adrs
        PUSH  DE               ; Save Menu literal
        SYSTEM INTPC
;
        DO    PAWS             ; Pause
        DB    150              ; 2 1/2 seconds
;
        DO    FILL             ; Fill memory with constant
        DW    MUZPC
        DW    32               ; Number of bytes
        DB    0                ; Fill character
;
        DO    COLSET           ; Set colors
        DW    L0013            ; System colors
;
        DO    SETOUT           ; Set outputs
        DB    191              ; Vertical Update Register
        DB    00101001B        ; Border color, left screen
        DB    8                ; Line interrupts only
;
        DO    ACTINT           ; Do an interrupt
;
        DO    SETB             ; Set byte
        DB    60
        DW    USERTB
;
        EXIT
;
        POP   DE               ; Get Menu literal address
        POP   HL               ; Get Game start address
        LD    SP,MUZPC
        LD    A,0AAH
        LD    (SENFLG),A       ; Disable SENTRY
        JP    (HL)             ; Go to game
;
SR002   LD    A,(HL)
        INC   HL
        OUT   (COL0R),A
        OUT   (COL1R),A
        OUT   (COL2R),A
        OUT   (COL3R),A
        OUT   (COL0L),A
        LD    A,(HL)
        INC   HL
        OUT   (COL1L),A
        LD    A,(HL)
        INC   HL
        OUT   (COL2L),A
        LD    A,(HL)
        OUT   (COL3L),A
        RET
;
SR000   LD    IX,L4FB4
SR000A  LD    A,(HL)
        INC   HL
        AND   A                ; See if EOS
        RET   Z
        OR    80H
        SYSTEM CHRDIS
        JR    SR000A
;
L2A80   DB    0
        DB    6CH
        DB    0FBH
        DB    7
;
L2A84   DB    7
        DB    0FCH
        DB    6CH
        DB    0
;
L2A88   DB    7
        DB    0
        DB    6CH
        DB    0FCH
;
L2A8C   DB    7
        DB    0FCH
        DB    6AH
        DB    0
;
L2A90   DB    0FBH
        DB    0DBH
        DB    77H
        DB    0
;
L2A94   DB    0
        DB    2
        DB    4
        DB    0FBH
;
SR006   SYSSUK PAWS            ; Pause
        DB    120              ; 2 second delay
        JP    L2955
;
SR010   PUSH  BC               ; Save line counter
        LD    BC,BYTEPL*63     ; Number of bytes to move
        LD    DE,NORMEM+BYTEPL*34
        LD    HL,NORMEM+BYTEPL*35
        LDIR
        POP   BC
        DJNZ  SR010
        RET
;
L2AAE   DO    FILL
        DW    NORMEM+BYTEPL*30
        DW    BYTEPL*65
        DB    0
        DONT  MRET
;
; Degrees symbol
;
; ..*.....
; .*.*....
; ..*.....
;
L2AB5   DB    1,3              ; 1 byte x 3 rows
        DB    20H
        DB    50H
        DB    20H
;
; Gunfight SENTRY table;
L2ABA   DB    10,SKYD,18          ; Key 2
        DB    100,SKYD,24         ; Key =
        DB    70,ST1,00010000B    ; Trigger 1
        DB    31,SP1,0            ; Pot 1
        DB    20,SJ0,5            ; Joystick 0
        DB    2,ST0,00010000B     ; Trigger 0
        DB    100,ST0,00001010B   ; Trigger 0
        DB    20,SF0,0            ; Flag Bit 0
        DB    10,SJ1,00001010B    ; Joystick 1
        DB    20,SJ0,1            ; Joystick 0
        DB    20,SP0,0            ; Pot 0
        DB    20,SP1,0D0H         ; Pot 1
        DB    10,ST0,00001010B    ; Trigger 0
        DB    10,SP0,64           ; Pot 0
        DB    30,ST1,00001010B    ; Trigger 1
        DB    10,ST0,00001010B    ; Trigger 0
        DB    40,ST1,00001010B    ; Trigger 1
        DB    20,SJ0,00000110B    ; Joystick 0
        DB    100,ST1,00001010B   ; Trigger 1
        DB    0                   ; Finished
        DW    L26B5
;
; Checkmate SENTRY table
;
L2AF6   DB    50,SKYD,14       ; Key 5
        DB    20,SKYD,24       ; Key =
        DB    20,SKYD,22       ; Key 0
        DB    255,SNUL,0       ; Nothing
        DB    100,SNUL,0       ; Nothing
        DB    0                ; Finished
        DW    L26D1
;
; Calculator SENTRY table
;
L2B08   DB    15,SKYD,18       ; Key 2
        DB    30,SKYD,16       ; Key -
        DB    15,SKYD,19       ; Key 3
        DB    30,SKYD,24       ; Key =
        DB    15,SKYD,20       ; Key +
        DB    15,SKYD,9        ; Key 7
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,20       ; Key +
        DB    15,SKYD,19       ; Key 3
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,12       ; Key X
        DB    15,SKYD,17       ; Key 1
        DB    15,SKYD,18       ; Key 2
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,8        ; Key divide
        DB    15,SKYD,11       ; Key 9
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,12       ; Key X
        DB    15,SKYD,11       ; Key 9
        DB    15,SKYD,11       ; Key 9
        DB    15,SKYD,11       ; Key 9
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,20       ; Key +
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,20       ; Key +
        DB    15,SKYD,17       ; Key 1
        DB    15,SKYD,4        ; Key %
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,6        ; Key MS
        DB    90,SKYD,13       ; Key 4
        DB    8,SKYD,19        ; Key 3
        DB    8,SKYD,23        ; Key .
        DB    8,SKYD,17        ; Key 1
        DB    8,SKYD,13        ; Key 4
        DB    8,SKYD,17        ; Key 1
        DB    8,SKYD,14        ; Key 5
        DB    8,SKYD,11        ; Key 9
        DB    8,SKYD,18        ; Key 2
        DB    8,SKYD,15        ; Key 6
        DB    8,SKYD,14        ; Key 5
        DB    8,SKYD,13        ; Key 4
        DB    8,SKYD,20        ; Key +
        DB    15,SKYD,17       ; Key 1
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,16       ; Key -
        DB    15,SKYD,17       ; Key 1
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,22       ; Key 0
        DB    15,SKYD,24       ; Key =
        DB    15,SKYD,5        ; Key MR
        DB    180,SKYD,13      ; Key 4
        DB    8,SKYD,3         ; Key Down
        DB    8,SKYD,3         ; Key Down
        DB    8,SKYD,3         ; Key Down
        DB    8,SKYD,3         ; Key Down
        DB    8,SKYD,3         ; Key Down
        DB    8,SKYD,3         ; Key Down
        DB    8,SKYD,3         ; Key Down
        DB    180,SKYD,3       ; Key Down
        DB    0                ; Finished
        DW    L273E
;
; Scribbling SENTRY table
;
L2BEC   DB    5,SKYD,22        ; Key 0
        DB    254,SCT0,0       ; DI, Counter-timer 0
        DB    255,SCT0,0       ; Counter-timer 0
        DB    255,SCT0,0       ; Counter-timer 0
        DB    255,SCT0,0       ; Counter-timer 0
        DB    200,SCT0,0       ; Counter-timer 0
        DB    0                ; Finished
        DW    L26EE
EJECT
; Music Parameter String
;
L2C01   MASTER  OA3
        VOLUME  7,0
        NOTE1   10,F3
;
        VOICEM  11110000B      ; Two note music
        VOLUME  77H,0
        LEGSTA                 ; Two notes merges together
        NOTE2   10,AS0,F3
        NOTE2   10,AS0,D3
        NOTE2   10,AS0,AS2
        NOTE2   10,AS0,A2
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,AS2
        NOTE1   10,D3
        NOTE1   10,F2
        NOTE1   10,AS2
        NOTE1   10,D2
        NOTE1   10,F2
        NOTE1   10,AS1
        NOTE1   10,D2
        NOTE1   10,F2
        NOTE1   10,GS2
        NOTE1   10,D3
        NOTE1   10,F3
;
        VOLUME  77H,0
        VOICEM  11110000B      ; Two note music
        NOTE2   10,AS0,G3
        NOTE2   10,AS0,DS3
        NOTE2   10,AS0,AS2
        NOTE2   10,AS0,A2
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,AS2
        NOTE1   10,DS3
        NOTE1   10,G2
        NOTE1   10,AS2
        NOTE1   10,DS2
        NOTE1   10,G2
        NOTE1   10,AS1
        NOTE1   10,DS2
        NOTE1   10,G2
        NOTE1   10,AS2
        NOTE1   10,DS3
        NOTE1   10,G3
;
        VOLUME  77H,0
        VOICEM  11110000B      ; Two voice music
        NOTE2   10,AS0,A3
        NOTE2   10,AS0,DS3
        NOTE2   10,AS0,C3
        NOTE2   10,AS0,AS2
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,C3
        NOTE1   10,DS3
        NOTE1   10,A2
        NOTE1   10,C3
        NOTE1   10,DS2
        NOTE1   10,A2
        NOTE1   10,C2
        NOTE1   10,DS2
        NOTE1   10,A2
        NOTE1   10,C3
        NOTE1   10,DS3
        NOTE1   10,A3
;
        VOICEM  11110000B      ; Two note music
        VOLUME  77H,0
        NOTE2   10,AS0,AS3
        NOTE2   10,AS0,F3
        NOTE2   10,AS0,D3
        NOTE2   10,AS0,C3
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,D3
        NOTE1   10,F3
        NOTE1   10,AS2
        NOTE1   10,D3
        NOTE1   10,F2
        NOTE1   10,AS2
        NOTE1   10,D2
        NOTE1   10,F2
        NOTE1   10,AS1
        NOTE1   10,G2
        NOTE1   10,A1
        NOTE1   10,F2
;
        VOICEM  11111100B      ; Three note music
        VOLUME  77H,6
        NOTE3   10,AS0,G1,G1
        NOTE3   10,AS0,G1,C3
        NOTE3   10,AS0,G1,E2
        NOTE3   10,AS0,G1,D2
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,E2
        NOTE1   10,G2
        NOTE1   10,C2
        NOTE1   10,E2
;
        VOICEM  11111100B      ; Three note music
        VOLUME  77H,7
        NOTE3   10,A0,FS1,FS1
        NOTE3   10,A0,FS1,A1
        NOTE3   10,A0,FS1,C2
        NOTE3   10,A0,FS1,DS2
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,D2
        NOTE1   10,C2
        NOTE1   10,C3
        NOTE1   10,D2
;
        VOICEM  11111100B      ; Three note music
        VOLUME  77H,6
        NOTE3   10,G0,G1,DS2
        NOTE3   10,G0,G1,G2
        NOTE3   10,G0,G1,C3
        NOTE3   10,G0,G1,B2
;
        VOICEM  11000000B      ; One note music
        VOLUME  0CH,0
        NOTE1   10,C3
        NOTE1   10,DS3
        NOTE1   10,A2
        NOTE1   10,C3
        NOTE1   10,FS2
        NOTE1   10,A2
        NOTE1   10,C3
        NOTE1   10,DS3
        NOTE1   10,D3
        NOTE1   10,C3
        NOTE1   10,A3
        NOTE1   10,C3
;
        VOICEM  11110000B      ; Two note music
        VOLUME  0AAH,0
        NOTE2   10,G0,G0
        NOTE2   10,G0,C3
        NOTE2   10,G1,AS2
        NOTE2   10,G1,A2
        NOTE2   10,G1,AS2
        NOTE2   10,G1,D3
        NOTE2   10,F1,E3
        NOTE2   10,F1,F3
        NOTE2   10,E1,G3
        NOTE2   10,E1,C3
        NOTE2   10,E2,AS2
        NOTE2   10,E2,A2
        NOTE2   10,E2,AS2
        NOTE2   10,E2,G3
        NOTE2   10,D2,AS2
        NOTE2   10,D2,F3
        NOTE2   10,C2,AS2
        NOTE2   10,C2,F3
        NOTE2   10,C1,E3
        NOTE2   10,C1,D3
        NOTE2   10,C1,E3
        NOTE2   10,C1,G3
        NOTE2   10,AS0,A3
        NOTE2   10,AS0,AS3
        NOTE2   10,A0,C4
        NOTE2   10,A0,F3
        NOTE2   10,A1,E3
        NOTE2   10,A1,D3
        NOTE2   10,A1,E3
        NOTE2   10,A1,C4
        NOTE2   10,G1,E3
        NOTE2   10,G1,AS3
        VOLUME  55H,0
        NOTE2   10,F1,E3
        NOTE2   10,F1,AS3
        NOTE2   10,F2,A3
        NOTE2   10,F2,G3
        NOTE2   10,A2,F3
        NOTE2   10,A2,A3
        NOTE2   10,C3,E3
        NOTE2   10,C3,A3
        NOTE2   10,AS2,D3
        NOTE2   10,AS2,A3
        NOTE2   10,AS1,D3
        NOTE2   10,AS1,C3
        NOTE2   10,D2,AS2
        NOTE2   10,D2,D3
        NOTE2   10,F2,A2
        NOTE2   10,F2,D3
        QUIET
;
; Filler bytes to match exactly with Demo Cart 6001 ROM
;
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH
        DB      0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH,0FFH

        ; END
