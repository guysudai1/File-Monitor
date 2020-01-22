import win32api as wa
import win32file as wf
import win32con as wc
import os.path
import os 

ExplorerPATH = "C:\\Users\\USER11\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files\\Low\\IE"
SavePATH     = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images\\")
IMG_EXTENSIONS = [".jpg", ".png"]
def main():
    buf = wf.AllocateReadBuffer(8096)
    
    hDir = wf.CreateFile(ExplorerPATH, 
                        1,
                        wc.FILE_SHARE_READ | wc.FILE_SHARE_DELETE | wc.FILE_SHARE_WRITE,
                        None,
                        wc.OPEN_EXISTING,
                        wc.FILE_FLAG_BACKUP_SEMANTICS,
                        None 
                        )
    while 1:
        changes = wf.ReadDirectoryChangesW(hDir,
                                           8096,
                                           True,
                                           wc.FILE_NOTIFY_CHANGE_FILE_NAME,
                                           None 
                                           )                                   
        for actions, file in changes:
            filename = os.path.join(ExplorerPATH, file)
            copyto   = os.path.join(SavePATH, file)
            print(copyto, SavePATH)
            if (filename[-4:] in IMG_EXTENSIONS):
                os.makedirs(copyto[:len(copyto) - copyto[::-1].find("\\")], exist_ok=True)
                
                with open(copyto, "wb") as newf:
                    with open(filename, "rb") as oldf:
                        content = oldf.read()
                    newf.write(content)
                print("[X] Wrote picture from {} to {}".format(filename, copyto))
            #print(actions, files, type(files))
                                
    
    
if __name__ == "__main__":
    main()