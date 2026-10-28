from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]
files=[p for p in root.rglob('*') if p.is_file() and not any(x in p.relative_to(root).parts for x in ['releases','.openai','.git','node_modules','__pycache__'])]
out=root/'releases/white-meteor-v0.3-full.zip';out.parent.mkdir(exist_ok=True)
with ZipFile(out,'w',ZIP_DEFLATED) as z:
 for p in sorted(files):z.write(p,Path('white-meteor-v0.3')/p.relative_to(root))
with ZipFile(out) as z:assert z.testzip() is None
print(out, out.stat().st_size,'bytes')
