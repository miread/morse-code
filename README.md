# Morse Code decoder

This is a decoder for a wired electrical telegraph.  It takes raw binary data
sampled from the wire and uses k-means clustering to account for variance in
speed and consistency of transmissions sent by human operators.

The main function is **decodeBitsAdvanced(bits)**.  This function finds an
estimate for the transmission rate of the message, taking care for slight speed
variations that may occur in the message, decodes the message to dots, dashes,
and spaces (one between characters, three between words), and returns those as a
string. Extra 0's that naturally occur at the beginning and the end of the
message are ignored.

This string of Morse Code is passed to **decodeMorse(morseCode)**, which
translates the string into the Modern English alphabet.

*Inspired by a challenge on CodeWars.com*
