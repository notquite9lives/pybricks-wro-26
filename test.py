from wrotools import scanHSV, db, wait
from pybricks.tools import run_task
async def main():
    while 0 == 0:
        print(await scanHSV())
        await wait(2000)
        
# 36, 71, 10 (35, 71, 24) Y
# 216, 88, 60 (218, 92, 40) B
# 350, 86, 33 (350, 78, 5) R
# (154, 81, 58)

run_task(main())