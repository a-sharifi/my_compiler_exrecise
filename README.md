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
![my simple lexical definite final autonama](Lexical_analizer/my_scanner_diagram.png "lexical definite final autonama(DFA)")

### run


`python3 lexical_analizer/scanner.py -i <input_file> -o <output_file>`



| Short_param | Long_param | description                     | default |
| ----------- | ---------- | ------------------------------- | ------- |
| -o          | --output   | path to input source code file  | out.txt |
| -i          | --input    | path to outout source code file | test.pp |

## Syntax analyzer
   Simple grammer to detect array of pascal language
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

### run

`python3 syntax_analizer/parser.py  -i <your_tokens_file_path>`

