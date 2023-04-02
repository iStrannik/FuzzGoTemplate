lexer grammar count_lexer;

Text : 'TEXT';
Template : 'template';
Block : 'block';
With : 'with';
CommentBegin : '/*';
CommentEnd : '*/';
If : 'if';
Else : 'else';
Range : 'range';
Pipe : '|';
Comma : ',';
Assignment : ':=';
Equal : '=';
Nil : 'nil';
LeftParenthesis : '(';
RightParenthesis : ')';
Dollar : '$';
Dot : '.';
End : 'end';
BlockStart : '{{';
Dash : '-';
BlockEnd : '}}';
Constant : 'CONSTANT';
Define : 'define';

And : 'and';
Eq : 'eq';
Lt : 'lt';
Le : 'le';
Ne : 'ne';
Gt : 'gt';
Ge : 'ge';
Len : 'len';
Not : 'not';
Or : 'or';
Index : 'index';
Slice : 'slice';
Printf : 'printf';
AnyText : 'Comment';

StringConstant: '"' /[ a-zA-Z0-9_\-/\\.]*/ '"';

NumberConstant: /[0-9]{1}[0-9.]*/;

Name: /[a-zA-Z]{1}[a-zA-Z0-9_]*/;


WS : [ \r\t\n]+ -> skip;
