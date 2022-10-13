from Schedule_class import FileSchelude
from watchdog.observers import Observer

path_to_file = "./Folder"
event_handler = FileSchelude(path_to_file)
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()
    
try:
    while True:
        pass
finally:
    observer.stop()
    observer.join()