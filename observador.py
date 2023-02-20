import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess
import os


def on_created(event):
    evento = f"{event.src_path} foi Criado \n"
    print(evento)
    arquivo_log.writelines(evento)
    exec(open("./extrator.py").read())
    exit()
    # cmd = 'python extrator.py'
    # subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
def on_deleted(event):
    evento = f"{event.src_path} foi Deletado \n"
    print(evento)
    arquivo_log.writelines(evento)
def on_modified(event):
    evento = f"{event.src_path} foi Modificado \n"
    print(evento)
    arquivo_log.writelines(evento)
def on_moved(event):
    evento = f"{event.src_path} foi Movido \n"
    print(evento)
    arquivo_log.writelines(evento)

def getquery():
    query = open(f"C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\query.txt", 'r')
    query = query.readlines()
    if len(query) == 0:
        return 'Query vazia'
    else:
        return query

if __name__ == "__main__":
    data = datetime.today().strftime('%d-%m-%Y %H.%M.%S')
    arquivo_log = open(f"C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Log {data}.txt", 'w+')

    
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved
    path = "C:\\Users\\paulo.sanches\\Desktop\\TestePastinha"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
