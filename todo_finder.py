from textual.app import App
from textual.widgets import Tree
from textual.scroll_view import ScrollView
import os
import re

class TodoScanner:
    def __init__(self, src_path='src', docsrc_path='docsrc'):
        self.src_path = src_path
        self.docsrc_path = docsrc_path
        self.todo_items = []

    def scan_files(self):
        # Implement scanning logic here
        pass

    def open_in_vim(self, file_path, line_number):
        os.system(f"vim +{line_number} {file_path}")


class TodoApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit", "Quit")

    async def on_mount(self):
        self.scanner = TodoScanner()
        self.scanner.scan_files()

        # Create and add the TreeControl to the layout
        self.tree = TreeControl("Files with TODOs")
        # Add files to the tree here
        await self.view.dock(self.tree)

    # Add other event handling methods here


if __name__ == "__main__":
    app = TodoApp()
    app.run()

