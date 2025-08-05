import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import asyncio

from src.queries.base import create_tables


# async def main():
#     create_tables()
    

# if __name__ == '__main__':
#     asyncio.run(main())

create_tables()