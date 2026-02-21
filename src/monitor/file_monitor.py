from .logger import EventLogger
from .threat_detector import ThreatDetector
from .decoy_manager import DecoyManager
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class FileMonitor(FileSystemEventHandler):
    """Monitors file system for changes."""

    def __init__(self):
        super().__init__()
        self.logger = EventLogger()
        self.threat_detector = ThreatDetector()
        self.decoy_manager = DecoyManager()
        self.logger.log_info("FileMonitor initialized with threat detection")

    def on_created(self, event):
        """Called when a file is created."""
        if not event.is_directory:
            self._handle_file_event("created", event.src_path, "File Created")

    def on_modified(self, event):
        """Called when a file is modified."""
        if not event.is_directory:
            self._handle_file_event("modified", event.src_path, "File Modified")

    def on_deleted(self, event):
        """Called when a file is deleted."""
        if not event.is_directory:
            self._handle_file_event("deleted", event.src_path, "File Deleted")

    def _handle_file_event(self, event_type, file_path, event_label):
        """Analyze file events and trigger decoy deployment when needed."""
        self.logger.log_info(f"{event_label}: {file_path}")

        self.threat_detector.add_event(event_type, file_path)
        threat_level = self.threat_detector.get_threat_level()
        threat_score = self.threat_detector.threat_score

        if threat_score >= 31:
            self.logger.log_warning(
                f"Threat Level: {threat_level} (Score: {threat_score}) - File: {file_path}"
            )

        deployed = self.decoy_manager.deploy_for_threat(
            threat_score=threat_score,
            threat_level=threat_level,
            trigger_path=file_path,
        )
        if deployed:
            self.logger.log_warning(
                f"Decoy deployment triggered by {file_path}: {len(deployed)} decoy(s) created"
            )

        self.decoy_manager.track_decoy_access(
            file_path=file_path,
            event_type=event_type,
            threat_level=threat_level,
            threat_score=threat_score,
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
    
