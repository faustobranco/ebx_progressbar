##############################################################################

import ebx_progressbar

import time

lst_Files = ['song.odt', 'want.csv', 'information.js', 'green.gif']

##############################################################################
# Example 1:

print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(ind_NewLine=False)
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Running(i, str_AdditionalText='Logging ', pre_Text='File: ' + satr_File + ' ',
                                      ind_Simple=True)
        time.sleep(1)
    print('\r')


# Example 2:
print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(pos_Line=10, pos_Column=50, ind_NewLine=False)
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Running(i, str_AdditionalText='Logging ', pre_Text='File: ' + satr_File + ' ',
                                      ind_Simple=True)
        time.sleep(1)
    print('\r')


# Example 3:
print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(ind_NewLine=True)
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Running(i, str_AdditionalText='Logging ', pre_Text='File: ' + satr_File + ' ',
                                      ind_Simple=True)
        time.sleep(1)
    print('\r')

# Example 4:
print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(pos_Line=10, pos_Column=50, ind_NewLine=False)
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Running(i, str_AdditionalText='Logging ', pre_Text='File: ' + satr_File + ' ',
                                      ind_Simple=False)
        time.sleep(1)
    print('\r')

##############################################################################
# Example 5:
print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar()
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Bar(i, pre_Text='File: ' + satr_File)
        time.sleep(1)
    print('\r')
    obj_ProgressBar.reset()

##############################################################################
# Example 6:

print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(100, 30, 1, ind_NewLine=False)
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Bar(i, pre_Text='File: ' + satr_File + ' ')
        time.sleep(1)
    print('\r')

# Example 7:
print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(200, 30, 1, ind_NewLine=True)
for satr_File in lst_Files:
    print('File: ' + satr_File + ' ')
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Bar(i)
        time.sleep(1)
    print('\r')

# Example 8:
print("\033c")
obj_ProgressBar = ebx_progressbar.progressBar(ind_NewLine=True)
for satr_File in lst_Files:
    for i in range(0, 101, 10):
        obj_ProgressBar.print_Bar(i, pre_Text='File: ' + satr_File)
        time.sleep(1)
    print('\r')
    obj_ProgressBar.reset()