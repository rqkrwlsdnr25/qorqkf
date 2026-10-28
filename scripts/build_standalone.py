from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
dist=root/'dist'
parts=[]
for name in ['engine','story-manager','game']:
    code=(dist/'js'/f'{name}.js').read_text()
    code=re.sub(r'^import[^\n]+\n','',code,flags=re.M)
    code=re.sub(r'\bexport ', '',code)
    if name=='game':
        line=code.splitlines()[0]
        code=code.replace(line,'const world='+ (dist/'data/world.json').read_text()+';\nconst plots='+ (dist/'data/plots.json').read_text()+';',1)
    parts.append(code)
css=re.sub(r'@import[^;]+;','',(dist/'css/game.css').read_text())
html=(dist/'index.html').read_text().replace('<link rel="stylesheet" href="css/game.css">','<style>'+css+'</style>')
html=html.replace('<script type="module" src="js/game.js"></script>','<script type="module">'+('\n'.join(parts)).replace('</script','<\\/script')+'</script>')
(root/'PLAY.html').write_text(html)
print('Built PLAY.html:',len(html),'characters')
