# whf

the weihang fan proglang

## impl

a repl.

## spec

everything should be an expression.

### keywords

simple keywords should match this pattern: `((w|h|f)*(a|ei)*(n|ng)?)`

considering the limited number of keywords that could be generated with the above pattern, complex keywords may be formed according to this pattern: `(KW)(-(KW))+` where `(KW)` stands for a simple keyword.

*	`W[weihangf]*`
 	*	evaluates to a integer literal whose value is the length of the characters following the initial `W`.
*	`h <SEQ>`
 	*	evaluates to a string whose `n`th character has the ascii of the `n`th integer in `<SEQ>`.
*	`ng <SEQ>`
 	*	evaluates to `<SEQ>`.
 	*	prints each value in `<SEQ>` as a string, followed by a newline.

### non-keywords and syntax stuff

keep non-keyword terminals to a minimum.

*	`( <EXPR> )`: evaluates to the value of `<EXPR>`.
*	`( <SEQ> )`: evaluates to the value of `<SEQ>`.
*	`<EXPR>`s separated by whitespace creates a sequence. a sequence needs not be homogenous in type.

### precs

### in the future

sequences may contain sequences. `ng Ww (Wwe Wwei)` would be equivalent to `(ng Ww) (ng Wwe Wwei)`, which would be equivalent to `(ng Ww) ((ng Wwe) (ng Wwei))`.