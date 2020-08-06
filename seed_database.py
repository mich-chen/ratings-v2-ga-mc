"""Script to seed database!
Do all the boring work for us. Thanks python <3"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')