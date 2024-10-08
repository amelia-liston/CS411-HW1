from typing import Any

from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:

    def __init__(self,
                migration_id: int,
                status: str = "Scheduled",
                migration_path: MigrationPath,
                path_id: int,
                current_location: str,
                start_date: str,
                current_date: str
                ) -> None:
        self.migration_id = migration_id
        self.status = status
        self.migration_path = migration_path
        self.path_id = path_id
        self.current_location = current_location
        self.start_date = start_date
        self.current_date = current_date
    

    def get_migration_by_id(migration_id: int) -> Migration:
        pass

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def get_migrations() -> list[Migration]:
        pass

    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass
    
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    