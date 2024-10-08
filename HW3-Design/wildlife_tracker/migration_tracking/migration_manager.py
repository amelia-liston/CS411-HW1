from typing import Optional
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:

    def __init__(self) -> None:
        migrations: dict[int, Migration] = {}
        paths: dict[int, MigrationPath] = {}

    def cancel_migration(self, migration_id: int) -> None:
        pass
    
    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass