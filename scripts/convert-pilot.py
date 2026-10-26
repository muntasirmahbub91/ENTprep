#!/usr/bin/env python3
"""Convert original wrapped TXT pilot question bank into static JSON after validation."""
import json,sys,hashlib,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:sys.exit('Usage: python3 scripts/convert-pilot.py path/to/pilot.txt')
s=pathlib.Path(sys.argv[1]).read_text(encoding='utf8');marker='BEGIN MACHINE-READABLE QUESTION ARRAY'
if marker not in s:sys.exit('Missing pilot JSON marker')
s=s[s.index(marker):];s=s[s.index('['):]
data=json.loads(s);issues=[];seen=set()
for q in data:
 code=q.get('question_code','?');kind=q.get('question_type');labels='ABCDE' if kind=='MTF' else 'ABCD' if kind=='SBA' else ''
 if code in seen:issues.append(code+' duplicate')
 seen.add(code)
 if not labels or len(q.get('options',[]))!=len(labels) or ''.join(o.get('label','') for o in q['options'])!=labels:issues.append(code+' invalid option labels')
 if kind=='MTF' and any(type(o.get('truth_value')) is not bool for o in q['options']):issues.append(code+' invalid truth key')
 if kind=='SBA' and sum(o.get('is_correct') is True for o in q['options'])!=1:issues.append(code+' invalid SBA key')
 for key in ('stem','primary_topic_id','concept_id','variation_group_id','status','version_number'):
  if not q.get(key):issues.append(code+' missing '+key)
report={'total':len(data),'MTF':sum(q.get('question_type')=='MTF' for q in data),'SBA':sum(q.get('question_type')=='SBA' for q in data),'errors':issues}
(root/'content/validation-report.json').write_text(json.dumps(report,indent=2))
if issues:sys.exit('Validation failed; see content/validation-report.json')
p=root/'content/questions.json';p.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
manifest={'schema_version':'1.0','content_release_id':'ent-pilot-2026-10-26','approved_question_count':sum(q['status']=='approved' and q.get('published') is True for q in data),'draft_question_count':sum(q['status']=='draft' for q in data),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'release_notes':'Pilot content; draft questions demonstration-only.'}
(root/'content/manifest.json').write_text(json.dumps(manifest,indent=2));print('Validated',len(data),'questions')
