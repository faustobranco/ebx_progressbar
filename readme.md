# ProgressBar

Python class for creating and print ProgressBar.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Developed and tested in Linux Ubuntu and Python 2.7


### Installing

A step by step series of examples that tell you have to get a development env running

1. Create a folder called "prgbar" inside the folder of your project.
2. Copy the prgbar.py and `__init__.py` files to the prgbar folder
3. Do class import for your project normally.

* If the import is successful, a file called prgbar.pyc must be created, this file (compiled python file) must be maintained.

## Functions

### Creating a object / instance
progressBar(fixed_width = 0, pos_Line = 0, pos_Column = 0, ind_NewLine = False)

Description: Init class with max Size(fixed_width) Line (pos_Line) and Column (pos_Column) to show progress bar, and ind_NewLine that show all status update in same line (False) or in new line (True)

### print_Running

print_Running(int_Progress = 0, str_AdditionalText = '', pre_Text = '', ind_Simple = False)

Description: Progress with running format [|], [/], [-], [\], [|], [/], [-], [-], [|]

**int_Progress**: incremental value to progress 
**str_AdditionalText**: Print text on the end of progressbar
**pre_Text**: Print text on the beginning of progressbar
**ind_Simple**: True shows additional time elapsed: Ex.: [Elapsed Time: 0:00:01]

Call this function adding the value of int_Progress to progress

Return: None

Example of pre_Text and AdditionalText:
pre_Text: [-] AdditionalText
              

### print_Bar

print_Bar(int_Progress = 0, pre_Text = ''):
Description: Progress with common format: pre_Text [Elapsed Time: 0:00:04] [####################################                                                        ] (40%)

**int_Progress**: incremental value to progress until 100 (100%)
**pre_Text**: Print text on the beginning of progressbar

Call this function adding the value of int_Progress to progress

Return: None


## Deployment

Additional notes about how to deploy this on a live system:
Para deploy em ambiente de live:
1) Create a folder called "checkbox" inside the folder of your project.
2) Copy the checklist.pyc and `__init__.pyc` files to the checkbox folder

Note: Unless you really have experience, do not install directly on /usr/local/lib/python2.7/dist-packages

For next versions will be available installation by setup or pip.

## Examples of use

```
import prgbar
import time  
lst_Arquivos = ['song.odt', 'want.csv', 'information.js', 'green.gif', 'the.flac', 'audience.tiff', 'single.key', 'culture.csv', 'name.odt', 'patient.bmp', 'fall.flac', 'career.tiff', 'apply.png', 'career.docx', 'court.mp3', 'seek.jpeg', 'violence.docx', 'pretty.odt']

##############################################################################

print "\033c"
obj_ProgressBar = prgbar.progressBar(ind_NewLine = False)
for satr_File in lst_Arquivos:
    for i in range(0, 101, 1):
        obj_ProgressBar.print_Running(i, str_AdditionalText= 'Logging ', pre_Text = 'Arquivo: ' + satr_File + ' ' , ind_Simple = True)
        time.sleep(1)
    print '\r'


print "\033c"
obj_ProgressBar = prgbar.progressBar(pos_Line = 10, pos_Column = 50, ind_NewLine = False)
for satr_File in lst_Arquivos:
    for i in range(0, 101, 1):
        obj_ProgressBar.print_Running(i, str_AdditionalText= 'Logging ', pre_Text = 'Arquivo: ' + satr_File + ' ' , ind_Simple = True)
        time.sleep(1)
    print '\r'


print "\033c"
obj_ProgressBar = prgbar.progressBar(ind_NewLine = True)
for satr_File in lst_Arquivos:
    for i in range(0, 101, 1):
        obj_ProgressBar.print_Running(i, str_AdditionalText= 'Logging ', pre_Text = 'Arquivo: ' + satr_File + ' ' , ind_Simple = True)
        time.sleep(1)
    print '\r'
    

print "\033c"
obj_ProgressBar = prgbar.progressBar(pos_Line = 10, pos_Column = 50, ind_NewLine = False)
for satr_File in lst_Arquivos:
    for i in range(0, 101, 1):
        obj_ProgressBar.print_Running(i, str_AdditionalText= 'Logging ', pre_Text = 'Arquivo: ' + satr_File + ' ' , ind_Simple = False)
        time.sleep(1)
    print '\r'    
    
##############################################################################


print "\033c"
obj_ProgressBar = prgbar.progressBar()
for satr_File in lst_Arquivos:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Bar(i, pre_Text = 'Arquivo: ' + satr_File)
        time.sleep(1)
    print '\r'
    obj_ProgressBar.reset()

##############################################################################


print "\033c"
obj_ProgressBar = prgbar.progressBar(100, 30, 1, ind_NewLine = False)
for satr_File in lst_Arquivos:
    for i in range(0, 101, 1):
        obj_ProgressBar.print_Bar(i, pre_Text = 'Arquivo: ' + satr_File + ' ')
        time.sleep(1)
    print '\r'  

  
print "\033c"
obj_ProgressBar = prgbar.progressBar(200, 30, 1, ind_NewLine = True)
for satr_File in lst_Arquivos:
    print 'Arquivo: ' + satr_File + ' '
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Bar(i)
        time.sleep(1)
    print '\r'  
    
```
[![](https://github.com/faustobranco/progressbar/blob/master/Capture.PNG)](https://github.com/faustobranco/progressbar/blob/master/Capture.PNG)

## Versioning
```
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## Authors
```
=======================================================================================
== Script Info:		prgbar.py - Class with functions to show progress Bar
==
=======================================================================================
== Create Author:	Fausto Branco
== Create Date:		2018-04-03
== Actual Version:  1.0.0
== Description:		
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## License



