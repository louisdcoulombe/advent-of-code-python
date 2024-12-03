from invoke.tasks import task
import pathlib as pl
import datetime
import aocd
import shutil
from dotenv import load_dotenv

load_dotenv()


@task
def skeleton(c, year=2024, day=None):
    year_folder = pl.Path(str(year))
    year_folder.mkdir(exist_ok=True)

    if not day:
        day = datetime.datetime.today().day

    day_folder = year_folder / str(day).zfill(2)
    day_folder.mkdir(exist_ok=True)

    fn = day_folder / "input.txt"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(aocd.get_data(day=int(day), year=year))

    for fn in ["./templates/main.py", "./templates/test_challenge.py"]:
        tmpl = pl.Path(fn)
        shutil.copy2(tmpl, day_folder / tmpl.name)

    
