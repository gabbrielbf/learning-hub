from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def view(self):
        pass
    
    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def calculate(self):
        pass


class DocumentPDF:

    def load(self):
        pass

    def view(self):
        pass


class DocumentTXT:

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def format(self):
        pass


class DocumentEXCEL:

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def calculate(self):
        pass