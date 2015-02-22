#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Config file for https://github.com/gr4viton/gr4pyShotor
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#::TAG LEGEND
# '/shopath'  # where to create shortcuts
# '/shoext'   # shortcut extension (without dot) = lnk
# '/new'      # new shortcut search bundle - and subdirectory in shopath
# '/dir'      # directory where to search for files to create shortcut of
# '/re'       # files regex strings - which files to create shortcut of
# '/ext'      # extension of files searched for to create shortcut of
# '/printit'  # printit level integer (0 - nothing, 5 - default, 100 - max)
# '/ignored'  # ignored filenames (with extension)
# # comment   # text comment - ignored
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#::standard
# where to create subdirs for found shortcuts 
/shopath
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\_ALL\GENERATED
/shoext
lnk
/ignored
update26.exe
DSRDGUI0.exe
#_ATKOSD2.exe
grub.exe
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# this program
/new
Gr4pyShoter
/dir
.
/re
main
/ext
py
/printit
100
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# gdocs and sheets
/new
ACT_SHEET
/dir
E:\GDRIVE\_LISTS
E:\GDRIVE\_PROJECTS
E:\GDRIVE\_BUY
/re
ls.*
p.*
log.*
/ext
gsheet
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# vims
/new
GDRIVE_VIM
/dir
E:\GDRIVE
/re
.*
/ext
vim
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_B_BACKUP
/dir
B:\__BACKUP_win7 - 2015_01_25\PROG
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_B_ESS
/dir
B:\_ESS\PROG
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_B_PROG
/dir
B:\PROG
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_C_PROG
/dir
C:\PROG
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_E_PROG
/dir
E:\PROG
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_F_PROG
/dir
F:\PROG
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_F_PROG_OLD
/dir
F:\PROG_OLD
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_D_DATA
/dir
D:\DATA
/re
.*
/ext
exe
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# PROG
/new
PROG_D_PROG
/dir
D:\PROG
/re
.*
/ext
exe
