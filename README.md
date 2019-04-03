# Morse Code decoder

This is a Morse code decoder for a wired electrical telegraph.

An electric telegraph is operated on a 2-wire line with a key that, when
pressed, connects the wires together, which can be detected on a remote station.
The Morse code encodes every character being transmitted as a sequence of "dots"
(short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:
```
"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
```
However, the standard does not specify how long that "time unit" is. And in fact
different operators would transmit at different speed. An amateur person may
need a few seconds to transmit a single character, a skilled professional can
transmit 60 words per minute, and robotic transmitters may go way faster.

For example, the message HEY JUDE, that is `···· · −·−− ·−−− ··− −·· ·` may be
received as follows:
```
1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
```
As you may see, this transmission is perfectly accurate according to the
standard; the hardware sampled the line exactly two times per "dot".

Your task is to implement two functions:

**Function decodeBits(bits)**, that should find out the transmission rate of the
message, correctly decode the message to dots ., dashes - and spaces (one
between characters, three between words) and return those as a string. Note that
some extra 0's may naturally occur at the beginning and the end of a message,
make sure to ignore them. Also if you have trouble discerning if the particular
sequence of 1's is a dot or a dash, assume it's a dot.

**Function decodeMorse(morseCode)**, that would take the output of the previous function and return a human-readable string.


*Inspired by a challenge on CodeWars.com*
