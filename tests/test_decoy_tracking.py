from src.decoy.manager import DecoyManager
from src.monitor.file_monitor import FileMonitor


def test_decoy_manager_tracks_decoy_access(tmp_path):
    manager = DecoyManager(base_decoy_dir=".decoys", threshold=51)
    trigger_file = tmp_path / "suspicious_passwords.txt"

    deployed = manager.deploy_for_threat(
        threat_score=75,
        threat_level="Critical",
        trigger_path=str(trigger_file),
    )
    assert len(deployed) == 4

    tracked = manager.track_decoy_access(
        file_path=deployed[0].file_path,
        event_type="modified",
        threat_level="Critical",
        threat_score=82,
    )

    assert tracked is not None
    assert tracked["file_path"] == deployed[0].file_path
    assert tracked["event_type"] == "modified"
    assert tracked["threat_level"] == "Critical"
    assert tracked["threat_score"] == 82
    assert len(manager.get_decoy_access_events()) == 1


def test_file_monitor_logs_decoy_access_context(tmp_path):
    monitor = FileMonitor()
    monitor.decoy_manager = DecoyManager(base_decoy_dir=".decoys", threshold=51)

    trigger_file = tmp_path / "password_seed.txt"
    deployed = monitor.decoy_manager.deploy_for_threat(
        threat_score=60,
        threat_level="Suspicious",
        trigger_path=str(trigger_file),
    )
    assert len(deployed) == 2

    class MockEvent:
        def __init__(self, src_path: str):
            self.src_path = src_path
            self.is_directory = False

    # Simulate attacker touching a deployed decoy
    monitor.on_modified(MockEvent(deployed[0].file_path))

    events = monitor.decoy_manager.get_decoy_access_events()
    assert len(events) >= 1
    assert events[-1]["file_path"] == deployed[0].file_path
    assert events[-1]["event_type"] == "modified"
