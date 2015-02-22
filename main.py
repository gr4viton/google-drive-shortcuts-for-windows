import os, sys, winshell
from win32com.client import Dispatch
import re

shell = Dispatch('WScript.Shell')


def PP():
    print('%'*80)

class C_Shotor:

    all_sho = 0

    def GO_through_list_and_create(q):
        #q.retx = q.retxList[0]
        rex = re.compile(q.retx)
        for root, subFolders, files in os.walk(q.rootdir):
            for file in files:
                r = rex.match(file)
                if r:
                    q.root = root

                    q.name = r.groups()[0]
                    q.key = q.name + "_" + q.root
                    q.d[q.key] = (q.root, q.name)
                # if r2

        
        for (root, name) in q.d.values():
            q.root = root
            q.name = name
            
            #vars = q.GET_variables()
    #        (shortcut_path, target_path, working_directory, icon_path) = vars
            q.GET_variables()
            #print('%s | %s' % (q.root, q.name))
            q.CREATE_shortcut()   

        return q.sum_sho 

    def GET_variables(q):
    #    ext = ".gsheet"
        q.file = q.name + '.' + q.ext
        q.target_path = os.path.join(q.root, q.file)
        q.working_directory = q.root
        q.icon_path = q.target_path

        q.shortcut_name = " ".join([ q.name, q.ext, q.cat + "." + q.shoext ]);
#        os.path.join
        q.shortcut_path = os.path.join(q.shopath, q.cat, q.shortcut_name)

    def DO_createDir(q, path):
        """create directory if non existent"""
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
            if q.print_it > 10:
                print('Created directory: [%s]' % (dir))

    def CREATE_shortcut(q):
        if q.print_it > 10:
            start_line = "_" * 42 +"\nNEW SHORTCUT (%s so far):" % q.sum_sho
            print("%s\n"                % start_line +
                  "shortcut_path:\t%s\n"% q.shortcut_path +
                  "target_path:\t%s\n"  % q.target_path +
                  "working_dir:\t%s\n"  % q.working_directory +
                  "icon_path:\t%s\n"    % q.icon_path )

        q.DO_createDir(q.shortcut_path)
        sho                  = shell.CreateShortCut( q.shortcut_path )
        sho.Targetpath       = q.target_path
        sho.WorkingDirectory = q.working_directory
        sho.IconLocation     = q.icon_path
        
        try:
            work_split = os.path.split(q.target_path)
        except:
            print( "Unexpected error:", sys.exc_info()[0] )
            return

        if work_split[1] not in q.ignored:

            try:
                sho.save()
                q.INC_sho()
                if q.print_it > 10:
                    print('[CREATED]')

            except IOError as e:
                print( 
                    "The shorcut could not been created -"
                    + "Try it yourself manually , but you won't succeed!\n"
                    + "I/O error({0}): {1}".format(e.errno, e.strerror)
                    )
            #except pywintypes_com_error:
            except:
                print( "Unexpected error:", sys.exc_info()[0] )
                            
            

        else:
            if q.print_it > 1:
                print('[IGNORED] %s\%s' % work_split )
            
    def INC_sho(q):
        """ increment shortcut counter """
        q.sum_sho = q.sum_sho + 1
        q.all_sho = q.all_sho + 1
    def FIND_and_create(q):

        q.retx = "(%s)\.%s" % ( '|'.join( q.lsNam ), q.ext )
        for pth in q.pthList:
            q.rootdir = os.path.abspath(pth)
            print( ' '.join([
                '\t[',q.cat ,
                '] Started to search for [', q.retx, 
                '] in dir [', q.rootdir, ']'
                ]) )
            q.GO_through_list_and_create()


    def __init__(q):
        q.INIT_empty()

    def RUN(q):
        q.FIND_and_create() 
        q.PRINT_created()


    def INIT_empty(q):


        q.pthList = []
        q.lsNam = []
        q.ext = ''
        q.cat = ''      # category and subdir
        q.print_it = 5
        q.d = {}
        q.sum_sho = 0   # shortcut counter

        q.shopath = ''
        q.shoext = ''
        q.ignored = ''
        
    def PRINT_created(q):
        q.PRINT_createdWhich(q.sum_sho)
    def PRINT_createdAll(q):
        if q.print_it > 0:
            print( '[%i] shortcuts created alltogether' 
                % (q.sum_all) )
    def PRINT_createdWhich(q, num):
        if q.print_it > 0:
            print( '%i\t[ %s ] category finished (shortcuts created)' 
                % (num,q.cat) )
            PP()

def CREATE_fromConfigs(config_file, syntax):
    lsShotor = []
    shopath = ''
    shoext = ''
    ignored = ''
    status = 'idle'
    commentag = '# %'.split()
    #print(commentag)

    with open(config_file) as f:
        all_lines = f.readlines()

    #print('%'*42)
    #print (all_lines)
    #print('%'*42)

    for line in all_lines:
        line = line.strip()

        if not line:
            continue
        elif line[0] in commentag: # comment
            #print('printing comments:')
            #print(line)
            continue

        elif line in syntax:
            status = line[1:]
        else:
            if status == 'shopath':
                shopath = line
            elif status == 'shoext':
                shoext = line
            elif status == 'ignored':
                ignored = line
            elif status == 'new':
                lsShotor.append( C_Shotor() )
                actShotor = lsShotor[-1]
                actShotor.cat = line
                actShotor.shopath = shopath
                actShotor.shoext = shoext
                actShotor.ignored = ignored
            elif status == 'dir':
                actShotor.pthList.append( line )
            elif status == 're':
                actShotor.lsNam.append( line )
            elif status == 'ext':
                actShotor.ext = line
            elif status == 'printit':
                actShotor.print_it = int(line)
                # actShotor.print_it = 100
    return lsShotor
           
def CREATE_syntax():
    synsign = '/'
    syntags = [
            'shopath'  # where to create shortcuts
            ,'shoext'   # shortcut extension (without dot) = lnk
            ,'new'      # new shortcut search bundle - and subdirectory in shopath
            ,'dir'      # directory where to search for files
            ,'re'       # files regex strings
            ,'ext'      # extension of files
            ,'printit'  # printit level integer
            ,'ignored'   # ignored filenames
            ]
    syntax = [ synsign + syntag for syntag in syntags ]
    return syntax 
 
def SHOTER_execute(lsShotor):
    [shoter.RUN() for shoter in lsShotor]
    lsShotor[0].PRINT_createdAll()


if __name__ == "__main__":
    # init
    PP()
    print('> Gr4pyShoter started')
    PP()
    print('[....] Creating syntax')
    syntax = CREATE_syntax()
    print('[DONE] Syntax created')
    print('[....] Reading config and creating Shotor items')
    lsShotor = CREATE_fromConfigs('conf/config.vim', syntax)

    print('[DONE] %s Shotors loaded' % len(lsShotor) )
    print('[....] Executing Shorters')    
    PP()
    SHOTER_execute(lsShotor)
    print('[DONE] Shotors executed')
    PP()
    print('Program end')
    PP()



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def enum(*sequential, **named):
#    enums = dict(zip(sequential, range(len(sequential)/)), **named)
#    return type('Enum', (), enums)
   

