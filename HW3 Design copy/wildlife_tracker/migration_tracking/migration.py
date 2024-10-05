from typing import Any

class Migration:

    def __init__(self,
                migration_id: int,
                status: str = "Scheduled",
                migration_path: MigrationPath,
                path_id: int
                ) -> None:
        self.migration_id = migration_id
        self.status = status
        self.migration_path = migration_path
        self.path_id = path_id
        # this is Pythonic for
        # if animals is not None:
        #   self.animals = animals
        # else:
        #   self.animals = []
        #self.animals = animals or []