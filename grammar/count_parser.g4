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
    self.counter['name'] = self.counter['name'] if 'name' in self.counter else {};
}

start @after{
print(self.counter); 
with open('counter.json', 'w') as f:
    json.dump(self.counter, f)
    } : template;

template
: 
(Text {self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1} 
| goaction {self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1}) 
(Text {self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1}
| goaction {self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1})* ;
goaction : 
commentaction {self.counter[inspect.stack()[0][3]]['commentaction'] = self.counter[inspect.stack()[0][3]]['commentaction'] + 1 if 'commentaction' in self.counter[inspect.stack()[0][3]] else 1}
| pipelineaction {self.counter[inspect.stack()[0][3]]['pipelineaction'] = self.counter[inspect.stack()[0][3]]['pipelineaction'] + 1 if 'pipelineaction' in self.counter[inspect.stack()[0][3]] else 1}
| ifaction {self.counter[inspect.stack()[0][3]]['ifaction'] = self.counter[inspect.stack()[0][3]]['ifaction'] + 1 if 'ifaction' in self.counter[inspect.stack()[0][3]] else 1}
| rangeaction {self.counter[inspect.stack()[0][3]]['rangeaction'] = self.counter[inspect.stack()[0][3]]['rangeaction'] + 1 if 'rangeaction' in self.counter[inspect.stack()[0][3]] else 1}
| templateaction {self.counter[inspect.stack()[0][3]]['templateaction'] = self.counter[inspect.stack()[0][3]]['templateaction'] + 1 if 'templateaction' in self.counter[inspect.stack()[0][3]] else 1}
| blockAction {self.counter[inspect.stack()[0][3]]['blockAction'] = self.counter[inspect.stack()[0][3]]['blockAction'] + 1 if 'blockAction' in self.counter[inspect.stack()[0][3]] else 1}
| withAction {self.counter[inspect.stack()[0][3]]['withAction'] = self.counter[inspect.stack()[0][3]]['withAction'] + 1 if 'withAction' in self.counter[inspect.stack()[0][3]] else 1};
commentaction : ld CommentBegin Text CommentEnd rd ;
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
templateaction : ld Template name (pipeline)? rd ;
blockAction : ld Block name (pipeline)? rd ;
withAction : ld With pipeline rd template ( ld Else rd template)? end ;
pipeline : 
argument ( Pipe argument )* {self.counter[inspect.stack()[0][3]]['argument'] = self.counter[inspect.stack()[0][3]]['argument'] + 1 if 'argument' in self.counter[inspect.stack()[0][3]] else 1}
| methodcall {self.counter[inspect.stack()[0][3]]['methodcall'] = self.counter[inspect.stack()[0][3]]['methodcall'] + 1 if 'methodcall' in self.counter[inspect.stack()[0][3]] else 1}
| funccall ( argument )* methodcall {self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1};
vardeclarepipeline :  variable (Comma variable)? Assignment pipeline ;
varassignpipeline :  variable Equal pipeline ;
argument : 
Constant {self.counter[inspect.stack()[0][3]]['Constant'] = self.counter[inspect.stack()[0][3]]['Constant'] + 1 if 'Constant' in self.counter[inspect.stack()[0][3]] else 1}
| Nil {self.counter[inspect.stack()[0][3]]['Nil'] = self.counter[inspect.stack()[0][3]]['Nil'] + 1 if 'Nil' in self.counter[inspect.stack()[0][3]] else 1}
| variable {self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1}
| fields {self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1}
| funccall {self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1}
| (LeftParenthesis argument RightParenthesis fields? ) 
{self.counter[inspect.stack()[0][3]]['LeftParenthesis'] = self.counter[inspect.stack()[0][3]]['LeftParenthesis'] + 1 if 'LeftParenthesis' in self.counter[inspect.stack()[0][3]] else 1};
variable : Dollar (name)? ;
fields : (variable)? Dot (name)? ( Dot (name)?)? ;
funccall : name ;
methodcall : ( 
    variable {self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1}
    | fields {self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1}
    ) ( argument )* ;
end : ld End rd ;
ld : BlockStart (Dash)? ;
rd : (Dash)? BlockEnd ;
name : Letter ( 
    Letter {self.counter[inspect.stack()[0][3]]['Letter'] = self.counter[inspect.stack()[0][3]]['Letter'] + 1 if 'Letter' in self.counter[inspect.stack()[0][3]] else 1}
    | Digit {self.counter[inspect.stack()[0][3]]['Digit'] = self.counter[inspect.stack()[0][3]]['Digit'] + 1 if 'Digit' in self.counter[inspect.stack()[0][3]] else 1}
    )* ;
