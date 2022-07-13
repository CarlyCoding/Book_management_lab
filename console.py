import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository


author1 = Author("Bill")
author_repository.save(author1)

