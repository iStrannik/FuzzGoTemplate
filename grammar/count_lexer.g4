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
Letter : /[a-zA-Z]/;
Digit : /[0-9]/;

WS : [ \r\t\n]+ -> skip;