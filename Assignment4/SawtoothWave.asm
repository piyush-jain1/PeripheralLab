; Sawtooth Wave
cpu "8085.tbl"
hof "int8"

org 9000H

MVI A, 80H
OUT 43H


MVI A,00H

SAWTOOTH:
	OUT 40H
	OUT 41H
	INR A
	CPI 0FFH
	JNZ SAWTOOTH
	MVI A,00H
	JMP SAWTOOTH
