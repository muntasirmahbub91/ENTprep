#!/usr/bin/env python3
"""Convert ENT_QBank_Revised_v2.0.zip to frontend demo JSON content."""
import sys,zipfile,json,collections,hashlib,pathlib
if len(sys.argv)!=2:sys.exit('Usage: python3 scripts/convert-revised-v2.py ENT_QBank_Revised_v2.0.zip')
z=zipfile.ZipFile(sys.argv[1]);data=json.loads(z.read('candidate_questions_draft.json'));excluded=json.loads(z.read('quarantined_questions.json'))
assert len(data)==1191 and len(excluded)==309
codes=set()
for q in data:
 c=q['question_code'];assert c not in codes,c;codes.add(c)
 k=q['question_type'];lab='ABCDE' if k=='MTF' else 'ABCD' if k=='SBA' else None;assert lab
 assert ''.join(o['label'] for o in q['options'])==lab,c
 assert q['status']=='draft',c
 assert all(isinstance(o.get('truth_value'),bool) for o in q['options']) if k=='MTF' else sum(o.get('is_correct') is True for o in q['options'])==1
root=pathlib.Path(__file__).resolve().parents[1]/'content';p=root/'questions.json';p.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
(root/'quarantined-questions.json').write_text(json.dumps(excluded,ensure_ascii=False,separators=(',',':')))
m=json.loads((root/'manifest.json').read_text());m['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();(root/'manifest.json').write_text(json.dumps(m,indent=2));print('Validated',len(data),'draft candidates and',len(excluded),'quarantined records')
