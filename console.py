import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author1 = Author("Bill")
author_repository.save(author1)
author2 = Author("Tolkien")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("A Walk in the Woods", author1)
book_repository.save(book1)
book2 = Book("The Hobbit", author2)
book_repository.save(book2)

pdb.set_trace()






