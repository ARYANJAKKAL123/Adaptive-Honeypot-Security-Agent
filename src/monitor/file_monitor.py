from .logger import EventLogger
from .threat_detector import ThreatDetector
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FileMonitor(FileSystemEventHandler):
    """Monitors file system for changes """
    
    def __init__(self):
        super().__init__()
        self.logger = EventLogger()
        self.threat_detector = ThreatDetector()
        self.logger.log_info("FileMonitor initialized with threat detection")
    
    def on_created(self, event):
        """Called when a file is created """
        if not event.is_directory:
            self.logger.log_info(f"File Created: {event.src_path}")

            # Add event to threat detector
            self.threat_detector.add_event("created", event.src_path)

            # Check threat level
            threat_level = self.threat_detector.get_threat_level()
            threat_score = self.threat_detector.threat_score

            # Log if threat is elevated or higher
            if threat_score >= 31:
                self.logger.log_warning(
                    f"Threat Level: {threat_level} (Score: {threat_score}) - "
                    f"File: {event.src_path}"
                )    
    
    def on_modified(self, event):
        """Called when a file is modifed"""
        if not event.is_directory:
            self.logger.log_info(f"File Modified: {event.src_path}")

            # Add event to threat detector
            self.threat_detector.add_event("modified", event.src_path)  # ← "modified" not "created"
        
            # Check threat level
            threat_level = self.threat_detector.get_threat_level()
            threat_score = self.threat_detector.threat_score
        
            # Log if threat is elevated or higher
            if threat_score >= 31:
                self.logger.log_warning(
                    f"Threat Level: {threat_level} (Score: {threat_score}) - "
                    f"File: {event.src_path}"
                )
    
    def on_deleted(self, event):
        """Called when a file is deleted"""
        if not event.is_directory:
            self.logger.log_info(f"File Deleted: {event.src_path}")

            # Add event to threat detector
            self.threat_detector.add_event("deleted", event.src_path)

            # Check threat level
            threat_level = self.threat_detector.get_threat_level()
            threat_score = self.threat_detector.threat_score

            # Log if threat is elevated or higher
            if threat_score >= 31:
                self.logger.log_warning(
                    f"Threat Level: {threat_level} (Score: {threat_score}) - "
                    f"File: {event.src_path}"
                )

def start_monitoring(path_to_watch):
    """ Start monitoring a directory"""
    print(f"Starting to monitor:{path_to_watch}")
    
    event_handler = FileMonitor()
    
    observer = Observer()
    
    observer.schedule(event_handler,path_to_watch, recursive = True)
    
    observer.start()
    print("Monitoring Started! Press Ctrl+C to stop..")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring Stopped")
    
    observer.join()  
    
    
if __name__ =="__main__":
    import os;
    
    
    test_folder = "test_monitor"
    if not os.path.exists(test_folder):
        os.mkdir(test_folder)
        print(f"Created test folder:{test_folder}")
        
    start_monitoring(test_folder)
    
