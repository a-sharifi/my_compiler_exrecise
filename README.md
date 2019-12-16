# Simple Compiler
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
  [![Made in MRL](https://img.shields.io/badge/Made%20in-Mechatronic%20Research%20Labratories-red.svg)](https://www.qiau.ac.ir/)

A simple package for compiler practice 

In two **phases**
1. Lexical analyzer
2. Syntax analyzer
---   
## Lexical analyzer
![my simple lexical definite final autonama](https://github.com/amirsharifi74/my_compiler_exrecise/blob/master/lexical_analizer/my_scanner_diagram.png "lexical definite final autonama(DFA)")

### Run

`git clone https://github.com/amirsharifi74/my_compiler_exrecise.git`

`python3 lexical_analizer/scanner.py -i <input_file> -o <output_file>`



| Short_param | Long_param | description                     | default |
| ----------- | ---------- | ------------------------------- | ------- |
| -o          | --output   | path to input source code file  | out.txt |
| -i          | --input    | path to outout source code file | test.pp |

## Syntax analyzer
   Simple grammer to detect array of our custum language(my language name is amir)
   Give output of Lexical analizer(tokens) and get the syntax error in CMD
   the rest of the language grammer is similar to this 

### Grammer
   ```
   type -> simple

   |  id

   | array [simple] of type

   symple -> integer

   | char

   | num dotdot num

   ```

### params
| Short_param | Long_param | description                    | default |
| ----------- | ---------- | ------------------------------ | ------- |
| -i          | --input    | path to input tokens file | out.txt |

### Run

`python3 syntax_analizer/parser.py  -i <your_tokens_file_path>`


--- 
## Impilimentation with antlr4
[Antlr4 Github page](https://github.com/antlr/antlr4 "Antlr's Homepage")

### installation antlr4
[getting start with antlr4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

Dont forget to install `pip install antlr4-python3-runtime`

**caution**: for running my sample code you should generate code for python 

```
cd antlr/
antlr4 -Dlanguage=Python3 Array.g4
```
### Run antlr
First of all write your code in test.pp
```
cd antlr/
python3 ArrayDetector.py
```
