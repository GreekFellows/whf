# whf

the weihang fan proglang

## spec

*	Keywords should follow this format: `(w|h|f)*(a|ei)(n|ng)?`
*	`W[weihangf]*`: integer literals, whose value is the length of the characters following the initial `W`.
*	`han`: evaluates to the next character in the string stream (there is no char vs. string distinction).
*	`hang <L>`: evaluates to the string composed of the next `<L>` characters in the string stream.
 	Thus `han` is equivalent to `hang We`.
*	`ng <EXPR>`: prints the value of `<EXPR>` as a string, followed by a newline.