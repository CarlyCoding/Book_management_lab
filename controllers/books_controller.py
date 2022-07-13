from flask import Flask, render_template, Blueprint, request, redirect
from models.author import Author
from models.book import Book
from repositories import author_repository
from repositories import book_repository

books_blueprint = Blueprint("books",__name__)




