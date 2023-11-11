"""This module runs the menu and executes the user's choices.
"""
import sys

from notebook import Notebook

sys.dont_write_bytecode = True


class Menu:
    """Displays a menu and responds to choices when run."""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        """Displays the menu."""
        print(
            """
        Notebook Menu

        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """
        )

    def run(self):
        """Displays the menu and responds to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        """Displays all notes."""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_notes(self):
        """Searches notes."""
        filter_notes = input("Search for: ")
        notes = self.notebook.search(filter_notes)
        self.show_notes(notes)

    def add_note(self):
        """Adds a note."""
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """Modifies a note."""
        note_id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(note_id, memo)
        if tags:
            self.notebook.modify_tags(note_id, tags)

    def quit(self):
        """Quits the program."""
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
