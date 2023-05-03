parser grammar count_parser;

options { tokenVocab=count_lexer; }

@header {
import inspect
import json
import os

if not os.path.exists('counter.json'):
    with open('counter.json', 'w+') as file:
        file.write('{}')

}

@members {
    with open('counter.json', 'r+') as f:
        self.counter = json.load(f)
    self.counter['template'] = self.counter['template'] if 'template' in self.counter else {};
    self.counter['goaction'] = self.counter['goaction'] if 'goaction' in self.counter else {};
    self.counter['pipelineaction'] = self.counter['pipelineaction'] if 'pipelineaction' in self.counter else {};
    self.counter['rangeaction'] = self.counter['rangeaction'] if 'rangeaction' in self.counter else {};
    self.counter['pipeline'] = self.counter['pipeline'] if 'pipeline' in self.counter else {};
    self.counter['argument'] = self.counter['argument'] if 'argument' in self.counter else {};
    self.counter['methodcall'] = self.counter['methodcall'] if 'methodcall' in self.counter else {};
    self.counter['globalfunctions'] = self.counter['globalfunctions'] if 'globalfunctions' in self.counter else {};
    self.counter['text'] = self.counter['text'] if 'text' in self.counter else {};
    self.counter['href'] = self.counter['href'] if 'href' in self.counter else {};
    self.counter['globalfunctions']['myprint'] = self.counter['globalfunctions'].get('myprint', 0);
    self.counter['globalfunctions']['random'] = self.counter['globalfunctions'].get('random', 0);
}

start @after{
print(self.counter); 
with open('counter.json', 'w') as f:
    json.dump(self.counter, f)
    } : template;

template
: 
(text {self.counter[inspect.stack()[0][3]]['text'] = self.counter[inspect.stack()[0][3]]['text'] + 1 if 'text' in self.counter[inspect.stack()[0][3]] else 1} 
| goaction {self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1}) 
(text {self.counter[inspect.stack()[0][3]]['text'] = self.counter[inspect.stack()[0][3]]['text'] + 1 if 'text' in self.counter[inspect.stack()[0][3]] else 1}
| goaction {self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1})* ;
goaction : 
commentaction {self.counter[inspect.stack()[0][3]]['commentaction'] = self.counter[inspect.stack()[0][3]]['commentaction'] + 1 if 'commentaction' in self.counter[inspect.stack()[0][3]] else 1}
| pipelineaction {self.counter[inspect.stack()[0][3]]['pipelineaction'] = self.counter[inspect.stack()[0][3]]['pipelineaction'] + 1 if 'pipelineaction' in self.counter[inspect.stack()[0][3]] else 1}
| ifaction {self.counter[inspect.stack()[0][3]]['ifaction'] = self.counter[inspect.stack()[0][3]]['ifaction'] + 1 if 'ifaction' in self.counter[inspect.stack()[0][3]] else 1}
| rangeaction {self.counter[inspect.stack()[0][3]]['rangeaction'] = self.counter[inspect.stack()[0][3]]['rangeaction'] + 1 if 'rangeaction' in self.counter[inspect.stack()[0][3]] else 1}
| templateaction {self.counter[inspect.stack()[0][3]]['templateaction'] = self.counter[inspect.stack()[0][3]]['templateaction'] + 1 if 'templateaction' in self.counter[inspect.stack()[0][3]] else 1}
| blockAction {self.counter[inspect.stack()[0][3]]['blockAction'] = self.counter[inspect.stack()[0][3]]['blockAction'] + 1 if 'blockAction' in self.counter[inspect.stack()[0][3]] else 1}
| withAction {self.counter[inspect.stack()[0][3]]['withAction'] = self.counter[inspect.stack()[0][3]]['withAction'] + 1 if 'withAction' in self.counter[inspect.stack()[0][3]] else 1}
| defineAction {self.counter[inspect.stack()[0][3]]['defineAction'] = self.counter[inspect.stack()[0][3]]['defineAction'] + 1 if 'defineAction' in self.counter[inspect.stack()[0][3]] else 1};
commentaction : ld CommentBegin AnyText CommentEnd rd ;
pipelineaction : ld ( 
    pipeline {self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1}
    | vardeclarepipeline {self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1}
    | varassignpipeline {self.counter[inspect.stack()[0][3]]['varassignpipeline'] = self.counter[inspect.stack()[0][3]]['varassignpipeline'] + 1 if 'varassignpipeline' in self.counter[inspect.stack()[0][3]] else 1}
    ) rd ;
ifaction : ld If pipeline rd template ( ld Else (If pipeline)? rd template )? end ;
rangeaction : ld Range ( 
    pipeline {self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1}
    | vardeclarepipeline {self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1}
    ) rd template ( ld Else rd template)? end ;
templateaction : ld Template StringConstant (pipeline)? rd ;
defineAction : ld Define StringConstant rd ;
blockAction : ld Block Name (pipeline)? rd ;
withAction : ld With pipeline rd template ( ld Else rd template)? end ;
pipeline : 
argument ( Pipe argument )* {self.counter[inspect.stack()[0][3]]['argument'] = self.counter[inspect.stack()[0][3]]['argument'] + 1 if 'argument' in self.counter[inspect.stack()[0][3]] else 1}
| methodcall {self.counter[inspect.stack()[0][3]]['methodcall'] = self.counter[inspect.stack()[0][3]]['methodcall'] + 1 if 'methodcall' in self.counter[inspect.stack()[0][3]] else 1}
| funccall {self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1};
vardeclarepipeline :  variable (Comma variable)? Assignment pipeline ;
varassignpipeline :  variable Equal pipeline ;
argument : 
Nil {self.counter[inspect.stack()[0][3]]['Nil'] = self.counter[inspect.stack()[0][3]]['Nil'] + 1 if 'Nil' in self.counter[inspect.stack()[0][3]] else 1}
| StringConstant {self.counter[inspect.stack()[0][3]]['StringConstant'] = self.counter[inspect.stack()[0][3]]['StringConstant'] + 1 if 'StringConstant' in self.counter[inspect.stack()[0][3]] else 1}
| NumberConstant {self.counter[inspect.stack()[0][3]]['NumberConstant'] = self.counter[inspect.stack()[0][3]]['NumberConstant'] + 1 if 'NumberConstant' in self.counter[inspect.stack()[0][3]] else 1}
| variable {self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1}
| fields {self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1}
| funccall {self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1}
| LeftParenthesis argument RightParenthesis
{self.counter[inspect.stack()[0][3]]['LeftParenthesis'] = self.counter[inspect.stack()[0][3]]['LeftParenthesis'] + 1 if 'LeftParenthesis' in self.counter[inspect.stack()[0][3]] else 1};
variable : Dollar (Name)? ;
fields : (variable)? Dot (Name)? ( Dot (Name)?)? ;
funccall : globalfunctions ;
methodcall : ( 
    variable {self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1}
    | fields {self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1}
    ) ( argument )* ;
end : ld End rd ;
ld : BlockStart (Dash)? ;
rd : (Dash)? BlockEnd ;
globalfunctions : (And argument argument) {self.counter[inspect.stack()[0][3]]['And'] = self.counter[inspect.stack()[0][3]]['And'] + 1 if 'And' in self.counter[inspect.stack()[0][3]] else 1}
| Index argument (argument)* {self.counter[inspect.stack()[0][3]]['Index'] = self.counter[inspect.stack()[0][3]]['Index'] + 1 if 'Index' in self.counter[inspect.stack()[0][3]] else 1}
| Slice argument (argument)* {self.counter[inspect.stack()[0][3]]['Slice'] = self.counter[inspect.stack()[0][3]]['Slice'] + 1 if 'Slice' in self.counter[inspect.stack()[0][3]] else 1}
| Len argument {self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1}
| Not argument {self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1}
| Or argument argument {self.counter[inspect.stack()[0][3]]['Or'] = self.counter[inspect.stack()[0][3]]['Or'] + 1 if 'Or' in self.counter[inspect.stack()[0][3]] else 1}
| Printf argument (argument)* {self.counter[inspect.stack()[0][3]]['Printf'] = self.counter[inspect.stack()[0][3]]['Printf'] + 1 if 'Printf' in self.counter[inspect.stack()[0][3]] else 1}
| Eq argument argument {self.counter[inspect.stack()[0][3]]['Eq'] = self.counter[inspect.stack()[0][3]]['Eq'] + 1 if 'Eq' in self.counter[inspect.stack()[0][3]] else 1}
| Ne argument argument {self.counter[inspect.stack()[0][3]]['Ne'] = self.counter[inspect.stack()[0][3]]['Ne'] + 1 if 'Ne' in self.counter[inspect.stack()[0][3]] else 1}
| Lt argument argument {self.counter[inspect.stack()[0][3]]['Lt'] = self.counter[inspect.stack()[0][3]]['Lt'] + 1 if 'Lt' in self.counter[inspect.stack()[0][3]] else 1}
| Le argument argument {self.counter[inspect.stack()[0][3]]['Le'] = self.counter[inspect.stack()[0][3]]['Le'] + 1 if 'Le' in self.counter[inspect.stack()[0][3]] else 1}
| (Gt argument argument) {self.counter[inspect.stack()[0][3]]['Gt'] = self.counter[inspect.stack()[0][3]]['Gt'] + 1 if 'Gt' in self.counter[inspect.stack()[0][3]] else 1}
| Ge argument argument {self.counter[inspect.stack()[0][3]]['Ge'] = self.counter[inspect.stack()[0][3]]['Ge'] + 1 if 'Ge' in self.counter[inspect.stack()[0][3]] else 1}
| Random {self.counter[inspect.stack()[0][3]]['random'] = self.counter[inspect.stack()[0][3]]['random'] + 1 if 'random' in self.counter[inspect.stack()[0][3]] else 1}
| Myprint argument {self.counter[inspect.stack()[0][3]]['myprint'] = self.counter[inspect.stack()[0][3]]['myprint'] + 1 if 'myprint' in self.counter[inspect.stack()[0][3]] else 1};
text :
Text {self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1}
| style {self.counter[inspect.stack()[0][3]]['style'] = self.counter[inspect.stack()[0][3]]['style'] + 1 if 'style' in self.counter[inspect.stack()[0][3]] else 1}
| js {self.counter[inspect.stack()[0][3]]['js'] = self.counter[inspect.stack()[0][3]]['js'] + 1 if 'js' in self.counter[inspect.stack()[0][3]] else 1}
| img {self.counter[inspect.stack()[0][3]]['img'] = self.counter[inspect.stack()[0][3]]['img'] + 1 if 'img' in self.counter[inspect.stack()[0][3]] else 1}
| default {self.counter[inspect.stack()[0][3]]['default'] = self.counter[inspect.stack()[0][3]]['default'] + 1 if 'default' in self.counter[inspect.stack()[0][3]] else 1}
| href {self.counter[inspect.stack()[0][3]]['href'] = self.counter[inspect.stack()[0][3]]['href'] + 1 if 'href' in self.counter[inspect.stack()[0][3]] else 1};

style : StyleStart goaction StyleEnd;
js : ScriptStart goaction ScriptEnd;
img : ImgStart goaction ImgEnd;
default : BrStart goaction BrEnd;
href : 
AStart goaction AEnd {self.counter[inspect.stack()[0][3]]['AStart'] = self.counter[inspect.stack()[0][3]]['AStart'] + 1 if 'AStart' in self.counter[inspect.stack()[0][3]] else 1}
| HrefStart goaction HrefEnd {self.counter[inspect.stack()[0][3]]['HrefStart'] = self.counter[inspect.stack()[0][3]]['HrefStart'] + 1 if 'HrefStart' in self.counter[inspect.stack()[0][3]] else 1};
local : Name;
