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
Myprint : 'print';
Random : 'random_string';
AnyText : 'Comment';

AStart : '<a href="#">';
HrefStart : '<a href="';
HrefEnd : '">abc</a>';
ScriptStart : '<script>';
ScriptEnd : '</script>';
StyleStart : '<style>';
StyleEnd : '</style>';
BrStart : '<br>';
BrEnd : '</br>';
ImgStart : '<img src=xx:';

AEnd : '</a>';

ImgEnd : '>';

StringConstant: '"' /[ a-zA-Z0-9_\-/\\.]*/ '"';

NumberConstant: /[0-9]{1}[0-9.]*/;

Name: /[a-zA-Z]{1}[a-zA-Z0-9_]*/;


WS : [ \r\t\n]+ -> skip;
