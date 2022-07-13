from flask import Flask, render_template, Blueprint, request, redirect
from models.task import Task
from repositories import task_repository
from repositories import user_repository

books_blueprint = Blueprint("books",__name__)




