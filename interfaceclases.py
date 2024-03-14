from abc import ABC, abstractmethod
from termcolor import colored
from prettytable import PrettyTable 

class Bot(ABC):
    
    @abstractmethod
    def return_all_users(self, book):
        pass

    @abstractmethod
    def format_display(self, text):
        pass



class ColorBot(Bot):
    def return_all_users(self, book):
        return colored(book, 'red')
    
    def format_display(self, text):
        return colored(text, 'red')
    

class TableBot(Bot):
    def return_all_users(self, book):
        adress_list = book.data_for_table()
        myTable = PrettyTable(["Contact Name", "Phones", "Birthday"])
        for item in adress_list:
            myTable.add_row(item)
        return myTable 
    
    def format_display(self, text):
        myTable = PrettyTable([text])
        return myTable
    


class StandardBot(Bot):
    def return_all_users(self, book):
        return book
    
    def format_display(self, text):
        return text

