from typing import Optional
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:

    def __init__(self) -> None:
        migrations: dict[int, Migration] = {}
        paths: dict[int, MigrationPath] = {}

    def cancel_migration(migration_id: int) -> None:
        pass
    
    def schedule_migration(migration_path: MigrationPath) -> None:
        pass