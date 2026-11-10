"""Validate learner continuity, public samples and starter integrity without network."""
from pathlib import Path
import json,re,zipfile
root=Path(__file__).resolve().parents[1]
docs=root/'docs'
path=json.loads((root/'scripts/learning-path.json').read_text())
practices=0
optional=[]
for day in path:
 folder=docs/'exercises'/day['slug']
 assert (folder/'index.md').exists() and (folder/'summary.md').exists()
 overview=(folder/'index.md').read_text()
 for slot in ['09:30\u201310:30','10:45\u201312:00','13:00\u201314:30','14:45\u201316:00']:
  assert slot in overview,day['slug']
 for j,item in enumerate(day['exercises'],1):
  p=folder/f'exercise-{j:02}.md';s=p.read_text()
  sections=re.split(r'^## Practice ',s,flags=re.M)[1:]
  assert sections,p
  practices+=len(sections)
  for section in sections:
   if '(Optional · macOS)' in section.splitlines()[0]:optional.append(p.relative_to(docs).as_posix())
   assert '**Primary target:**' in section,p
   assert '**Checkpoint:**' in section,p
   assert '### Steps' in section,p
  assert 'next:' in s and 'prev:' in s,p
  if j==4:assert f'/exercises/{day["slug"]}/summary' in s,p
 assert 'summary' in (folder/'exercise-04.md').read_text()
assert len(path)==4 and sum(len(x['exercises']) for x in path)==16
assert practices-len(optional)==40 and len(optional)==1,(practices,optional)
assert optional==['exercises/day-03-flutter/exercise-04.md'],optional
images=json.loads((docs/'.vitepress/theme/practice-images.json').read_text())
used=[]
for p in (docs/'exercises').glob('*/exercise-*.md'):
 s=p.read_text()
 for section in re.split(r'^## Practice ',s,flags=re.M)[1:]:
  match=re.match(r'[^\n]+\n\n<PracticeIllustration asset="([^"]+)"(?: eager)? />',section)
  assert match,f'Missing illustration directly below practice heading: {p}'
  asset=match[1];used.append(asset)
  item=images[asset]
  assert set(item)=={'alt','width','height','sources'},asset
  assert item['alt'] and item['width']>0 and item['height']>0,asset
  for source in item['sources']:
   assert set(source)=={'url','width','height'},asset
   assert source['url'].startswith('/images/practices/'),asset
   file=docs/'public'/source['url'].lstrip('/')
   assert file.is_file() and not file.is_symlink(),file
   assert source['width']<=item['width'] and source['height']<=item['height'],asset
   assert abs(source['height']-item['height']*source['width']/item['width'])<=1,asset
assert len(used)==len(set(used))==len(images)==41
assert set(used)==set(images)
for p in docs.rglob('*.md'):
 s=p.read_text()
 assert '\ufffd' not in s,p
 assert not re.search(r'/[Uu]sers/[^/\s;]+/',s),p
 assert all(not line.endswith((' ','\t')) for line in s.splitlines()),p
public=docs/'public/files'
for p in public.iterdir():
 assert p.is_file() and not p.is_symlink(),p
 assert p.name not in ['.env','AGENTS.md'],p
 if p.suffix=='.pdf':
  with p.open('rb') as pdf:
   assert pdf.read(5)==b'%PDF-',p
 elif p.suffix!='.zip':
  s=p.read_text();assert not re.search(r'/[Uu]sers/[^/\s;]+/',s),p
mapping={
 'docs/project-brief.md':'project-brief.md','docs/api-contract.md':'api-contract.md',
 'data/service-requests.json':'service-requests.json','api/schema.sql':'schema.sql',
 'api/requirements.txt':'requirements.txt','api/.env.example':'api.env.example',
 'docs/agents-template.md':'agents-template.md','docs/review-log.md':'review-log.md',
 '.gitignore':'gitignore.template','.dockerignore':'dockerignore.template',
 'api/Dockerfile':'Dockerfile','docs/deploy-api.yml.example':'deploy-api.yml.example',
 'scripts/check_api.py':'check_api.py','docs/change-request.md':'change-request.md'}
with zipfile.ZipFile(public/'service-desk-starter.zip') as z:
 assert z.testzip() is None
 assert len(z.namelist())==15
 for item in z.namelist():
  assert item.startswith('service-desk-lite/') and '..' not in Path(item).parts,item
  assert '/.git/' not in item and not item.endswith('/.env'),item
  s=z.read(item).decode();assert not re.search(r'/[Uu]sers/[^/\s;]+/',s),item
 for name,sample in mapping.items():
  assert z.read('service-desk-lite/'+name)==(public/sample).read_bytes(),name
print('PASS: 4 days, 16 exercises, 40 core + 1 optional practices, 41 illustrations, daily handoffs and 15 starter entries')
