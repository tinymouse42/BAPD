; Title:        Hello World
; Platform:     Bally Astrocade
; Program By:   Adam Trionfo
; Revision:     1.2 (Revision list is at end of the source code)
;
; About this Program
; ------------------
;
; This program displays a short string, "HELLO, WORLD!"
;
; To assemble Z-80 source code using ZMAC:
; zmac -i -m -o hello.bin -x hello.lst hello.asm

INCLUDE "HVGLIB.H"

        ORG    $2000    ; First byte of Cartridge
        DB     "U"      ; User System Sentinel

        DW     MENUST   ; Next menu link
        DW     PRGNAM   ; Address of title for program
        DW     PRGST    ; Jump here if prog is selected

;Main Program
PRGST:  DI
        SYSTEM (INTPC)

        DO     (SETOUT)
        DB     $B0        ; Vertical Blanking Line
        DB     $2C        ; Left/Right Color Boundary
        DB     $08        ; Interrupt Mode

        DO     (COLSET)
        DW     COLTAB     ; Color Table

        DO     (FILL)
        DW     NORMEM     ; Destination
        DW     4000D      ; Bytes to move
        DB     $00        ; Background color

        DO     (STRDIS)
        DB     0          ; X coordinate
        DB     0          ; Y coordinate
        DB     $0C        ; Options
        DW     STRING     ; Address of string to display

        EXIT

LOOP:   NOP
        JP     LOOP       ; Infinite loop

; Color Table #1
COLTAB: DB     $00        ; Color 3 Left  - Black
        DB     $5A        ; Color 2 Left  - Red
        DB     $77        ; Color 1 Left  - Yellow
        DB     $07        ; Color 0 Left  - White
        DB     $00        ; Color 3 Right - Black
        DB     $5A        ; Color 2 Right - Red
        DB     $77        ; Color 1 Right - Yellow
        DB     $07        ; Color 0 Right - White

PRGNAM: DB     "HELLO WORLD!"
        DB     $00        ; End String

STRING: DB     "HELLO, WORLD!"
        DB     $00        ; End string

        ORG    $2FFF

        DB     $00        ; Last byte of 4K Cart

        END

; End of Program

; Revision History:
; -----------------
;
;     Rev. 1.2 (Dec. 11, 2018) by Commander Dave usisolutions13@gmail.com
;        - Added end directive. Anything after it is silently ignored
;        - Added Platform entry in header remarks
;
;     Rev. 1.1 (Sept. 1, 2011), Update by Adam Trionfo
;        - Added Revision History
;        - Added comma and exclamation point to "HELLO, WORLD!" string
;
;     Rev. 1.0 (July 27, 2011), By Adam Trionfo
;        - First release as example on Bally Alley Discussion Group