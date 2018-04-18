##############################################################################

import prgbar
import time  
lst_Arquivos = ['song.odt', 'want.csv', 'information.js', 'green.gif', 'the.flac', 'audience.tiff', 'single.key', 'culture.csv', 'name.odt', 'patient.bmp', 'fall.flac', 'career.tiff', 'apply.png', 'career.docx', 'court.mp3', 'seek.jpeg', 'violence.docx', 'pretty.odt']

##############################################################################

print "\033c"
obj_ProgressBar = prgbar.progressBar(ind_NewLine = False)
for satr_File in lst_Arquivos:
    for i in range(0, 101, 10):
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
    for i in range(0, 101, 10):
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
    
 