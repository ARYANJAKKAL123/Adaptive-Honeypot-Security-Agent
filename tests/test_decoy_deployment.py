from pathlib import Path

from src.decoy.manager import DecoyManager
from src.monitor.file_monitor import FileMonitor


def test_decoy_manager_deploys_for_suspicious_threat(tmp_path):
    manager = DecoyManager(base_decoy_dir=".decoys", threshold=51)
    trigger_file = tmp_path / "notes.txt"

    deployed = manager.deploy_for_threat(
        threat_score=60,
        threat_level="Suspicious",
        trigger_path=str(trigger_file),
    )

    assert len(deployed) == 2
    assert all(Path(decoy.file_path).exists() for decoy in deployed)
    assert all(str(tmp_path / ".decoys") in decoy.file_path for decoy in deployed)


def test_decoy_manager_tracks_and_deduplicates_deployments(tmp_path):
    manager = DecoyManager(base_decoy_dir=".decoys", threshold=51)
    trigger_file = tmp_path / "passwords.txt"

    first = manager.deploy_for_threat(
        threat_score=75,
        threat_level="Critical",
        trigger_path=str(trigger_file),
    )
    second = manager.deploy_for_threat(
        threat_score=80,
        threat_level="Critical",
        trigger_path=str(trigger_file),
    )

    assert len(first) == 4
    assert second == []
    assert len(manager.get_deployed_decoys()) == 4
    assert manager.is_decoy_file(first[0].file_path) is True


def test_file_monitor_deploys_decoys_when_threat_crosses_threshold(tmp_path):
    monitor = FileMonitor()
    monitor.decoy_manager = DecoyManager(base_decoy_dir=".decoys", threshold=51)

    class MockEvent:
        def __init__(self, src_path: str):
            self.src_path = src_path
            self.is_directory = False

    for i in range(5):
        event = MockEvent(str(tmp_path / f"password_file_{i}.txt"))
        monitor.on_created(event)

    deployed = monitor.decoy_manager.get_deployed_decoys()
    assert len(deployed) >= 2
