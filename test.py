from wrotools import scanHSV
from pybricks.tools import run_task
async def main():
    print(await scanHSV())



run_task(main())