import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.queries.core import create_tables

create_tables()
# insert_data()