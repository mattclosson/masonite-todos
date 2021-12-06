"""CreateTodosTable Migration."""

from masoniteorm.migrations import Migration


class CreateTodosTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("todos") as table:
            table.increments("id")
            table.timestamps()
            table.string("subject")
            table.string("details")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("todos")