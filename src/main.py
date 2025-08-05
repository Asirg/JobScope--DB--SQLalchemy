import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import asyncio

from queries.orm import *


async def main():
    create_tables()
    await insert_user()
    # await select_all_users()
    # await update_users()
    await insert_resumes()
    # await select_resumes_avg_compensation()
    # await get_avg_diff_compensation()
    # select_users_with_lazy_relationship()
    select_users_with_selectin_relationship()

if __name__ == '__main__':
    asyncio.run(main())