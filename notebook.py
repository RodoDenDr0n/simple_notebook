from termcolor import colored
from datetime import date
import re


class Notebook:
    """Creates a class for Notebook"""
    def __init__(self, notes):
        """
        Creates notebook
        >>> note_1 = Note('lol', 'date', '#kek')
        >>> note_2 = Note('lol', 'date', '#kek')
        >>> note_3 = Note('lol', 'date', '#kek')
        >>> notes = [note_1, note_2, note_3]
        >>> notebook = Notebook(notes)
        """
        self.notes = notes

    def search(self, filter):
        """
        Searches for phrase in notebook
        >>> note_1 = Note('lol', 'date', '#kek')
        >>> notes = [note_1]
        >>> notebook = Notebook(notes)
        >>> notebook.search('lol') #doctest: +ELLIPSIS
        [('Found in memo', 'lol', ...)]
        """
        matches = []
        for i in range(len(self.notes)):
            if self.notes[i].match(filter) is True:
                matches.append(("Found in memo", self.notes[i].memo, self.notes[i]))
            elif self.notes[i].match(filter) is False:
                matches.append(("Found by tags", self.notes[i].tags, self.notes[i]))
        return matches

    def new_note(self, memo, tags=""):
        """
        Creates a new note
        """
        creation_date = date.today()
        note = Note(memo, creation_date, tags)
        self.notes.append(note)

    def modify_memo(self, note_id, memo):
        """
        Modifies memo
        """
        notes = self.notes
        notes[note_id].memo = memo

    def modify_tags(self, note_id, tags):
        """
        Modifies tags
        """
        notes = self.notes
        notes[note_id].tags = tags


class Note:
    """Class representation for Note"""
    def __init__(self, memo, creation_date, tags):
        """
        Creates note
        >>> note = Note('lol', 'date', '#kek')
        >>> note.memo
        'lol'
        >>> note.creation_date
        'date'
        >>> note.tags
        '#kek'
        """
        self.memo = memo
        self.creation_date = creation_date
        self.tags = tags

    def match(self, search_filter):
        """
        Checks if searched phrase matches note memo or tags,
        if match is found returns True, else False
        >>> note = Note('lol', 'date', '#kek')
        >>> note.match('lol')
        True
        """
        if re.search(search_filter, self.memo):
            return True
        if re.search(search_filter, self.tags):
            return False


class Menu:
    """Class representation of Menu"""
    @staticmethod
    def menu(notebook):
        """
        Function that is static and navigates menu
        """
        print(CommandOption())
        user_command = input("\nEnter " + colored("command", "green") + ":" +
                             colored("\n>>> ", "red", attrs=["bold"]))

        if user_command == "change_memo":
            return CommandOption.change_memo(notebook)

        elif user_command == "modify_tags":
            return CommandOption.modify_tags(notebook)

        elif user_command == "new_note":
            return CommandOption.new_note(notebook)

        elif user_command == "search":
            return CommandOption.search(notebook)


class CommandOption:
    @staticmethod
    def get_note_id(notebook):
        """
        Function that is static, gets note id
        """
        notes = notebook.notes
        print(colored("\nAvailable notes to change:", "cyan", attrs=["bold"]))
        for i in range(len(notes)):
            print(colored(f" [{i+1}] ", "green") + colored("memo: ", "red") + f"{notes[i].memo}" +
                  colored("\n     tags: ", "red") + f"{notes[i].tags}")

        note_id = int(input("\nEnter the " + colored("node id", "green", attrs=["bold"]) +
                            " you want to modify:" +
                            colored("\n>>> ", "red", attrs=["bold"])))
        return note_id - 1

    @staticmethod
    def get_memo(new=False):
        """
        Function that is static, gets memo
        """
        new_word = ""
        if new:
            new_word = " new"
        memo = input("\nEnter a" + colored(f"{new_word} memo", "green", attrs=["bold"]) + ":" +
                     colored("\n>>> ", "red", attrs=["bold"]))
        return memo

    @staticmethod
    def get_tags(new=False):
        """
        Function that is static, gets tags
        """
        new_word = ""
        if new:
            new_word = " new"
        tags = input("\nEnter" + colored(f"{new_word} tags", "green", attrs=["bold"]) + " split by " +
                     colored("' #'", "red", attrs=["bold"]) + ":" +
                     colored("\n>>> ", "red", attrs=["bold"]))
        return tags

    @staticmethod
    def get_search_phrase():
        """
        Function that is static, searches phrases
        """
        search_phrase = input("\nEnter a phrase you want to " +
                              colored("search", "green", attrs=["bold"]) +
                              " in notebook:" +
                              colored("\n>>> ", "red", attrs=["bold"]))
        return search_phrase

    @staticmethod
    def show_search_results(matches):
        """
        Function that is static, shows search results
        """
        print(colored("\nFound matches:", "cyan", attrs=["bold"]))
        for match in matches:
            print(colored(" [+] ", "green") + colored(f"{match[0]}: ", "red") + f"{match[1]}")

    @staticmethod
    def change_memo(notebook):
        """
        Function that is static, changes memo
        """
        note_id = CommandOption.get_note_id(notebook)
        old_memo = notebook.notes
        old_memo = old_memo[note_id].memo
        print(colored("\nYour old memo:", "green", attrs=["bold"]), old_memo)
        new_memo = CommandOption.get_memo(True)
        notebook.modify_memo(note_id, new_memo)
        return None

    @staticmethod
    def modify_tags(notebook):
        """
        Function that is static, modifies tags
        """
        note_id = CommandOption.get_note_id(notebook)
        old_tags = notebook.notes
        old_tags = old_tags[note_id].tags
        print(colored("\nYour old tags: ", "green", attrs=["bold"]), old_tags)
        new_tags = CommandOption.get_tags(True)
        notebook.modify_tags(note_id, new_tags)
        return None

    @staticmethod
    def new_note(notebook):
        """
        Function that is static, creates new note
        """
        memo = CommandOption.get_memo()
        tags = CommandOption.get_tags()
        notebook.new_note(memo, tags)
        return None

    @staticmethod
    def search(notebook):
        """
        Function that is static, looks up for a phrase in notebook
        """
        search_phrase = CommandOption.get_search_phrase()
        matches = notebook.search(search_phrase)
        CommandOption.show_search_results(matches)
        return None

    def __str__(self):
        """String representation of class"""
        information = colored("\nCommand Options:", "cyan", attrs=["bold"]) + \
                      colored("\n [+] ", "green") + "change_memo" + \
                      colored("\n [+] ", "green") + "modify_tags" + \
                      colored("\n [+] ", "green") + "new_note" + \
                      colored("\n [+] ", "green") + "search"
        return information


def main():
    """
    Main function that runs the program
    """
    notebook = Notebook(notes=[])
    while True:
        Menu().menu(notebook)


# main()  # in order to use the program uncomment the function
