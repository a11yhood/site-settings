from pathlib import Path
import shutil

FILE = Path(__file__)
HERE = FILE.parent
ASSETS = HERE / "assets"
INCLUDES = ASSETS / "_includes"
IMAGES = ASSETS / "images"
_404 = ASSETS / "404.html"
CONFIG = ASSETS / "_config.yml"
CWD = Path.cwd()


shutil.copytree(INCLUDES, CWD / INCLUDES.name, dirs_exist_ok=True)
shutil.copytree(IMAGES, CWD / IMAGES.name, dirs_exist_ok=True)
shutil.copyfile(_404, CWD / _404.name)

local_config = CWD / CONFIG.name

configs = [CONFIG]

if local_config.exists():
    configs.append( local_config)

import yaml
data = {}
for config in configs:
    data |= yaml.safe_load(config.read_text())
    
local_config.write_text(yaml.safe_dump(data))

