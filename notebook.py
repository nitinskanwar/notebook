"""
This module contains the Notebook and Note classes. Notebook is a 
collection of notes that can be tagged, modified and searched. Note 
is a note in a Notebook. It matches against a string in searches and 
stores tags for each note."""

import sys
import datetime

sys.dont_write_bytecode = True

"""
This is a module level variable
Store the next available id for all new notes
"""
last_id = 0


class Note:
    """This class represents a Note in a Notebook. Match against a string in searches and store tags for each note."""

    def __init__(self, memo, tags="") -> None:
        """Initialize a note with memo and tags. Automatically set the note's creation date and a unique id.

        Parameters
        ----------
        memo : string
            Memo to be written within the note
        tags : str, optional
            Helps search for the note using the tag, by default ''
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter: str) -> bool:
        """Searches for a filter string to match the memo or tags. Returns True if matches else False.
        Search is case sensitive and matches both memo and tags.

        Parameters
        ----------
        filter : str
            Contains the search string

        Returns
        -------
        bool
            Returns True or False
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represents a collection of notes that can be tagged, modified and searched."""

    def __init__(self) -> None:
        """Initializes a notebook with an empty list of notes."""
        self.notes = []

    def new_note(self, memo: str, tags: str = "") -> None:
        """Creates a new note and adds it to the list of notes.

        Parameters
        ----------
        memo : str
            Memo to be written within the note
        tags : str, optional
            Helps search for the note using the tag, by default ''
        """
        self.notes.append(memo, tags)

    def modify_memo(self, note_id: int, memo: str) -> None:
        """Finds the note with the given id and changes its memo to the given value.

        Parameters
        ----------
        note_id : int
            Unique id of the note
        memo : str
            New memo to be written within the note
        """
        note = self._find_note_by_id(note_id)
        if note:
            note.memo = memo

    def modify_tags(self, note_id: int, tags: str) -> None:
        """Finds the note with the given id and changes its tags to the given value.

        Parameters
        ----------
        note_id : int
            Unique id of the note
        tags : str
            New tags to be written within the note
        """
        note = self._find_note_by_id(note_id)
        if note:
            note.tags = tags

    def search(self, filter: str) -> list:
        """Finds all notes that match the given filter string.

        Parameters
        ----------
        filter : str
            Contains the search string

        Returns
        -------
        list
            Returns a list of notes that match the filter string
        """
        return [note for note in self.notes if note.match(filter)]

    def _find_note_by_id(self, note_id: int) -> Note:
        """Locate the note with the given id.

        Parameters
        ----------
        note_id : int
            Unique id of the note

        Returns
        -------
        Note
            Returns the note with the given id
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
