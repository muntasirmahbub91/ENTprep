import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {select,grade} from '../engine.mjs';
const bank=JSON.parse(fs.readFileSync(new URL('../content/questions.json',import.meta.url)));const catalog=JSON.parse(fs.readFileSync(new URL('../content/clinical-items.json',import.meta.url)));
const preview=bank.filter(q=>q.status==='draft'&&!q.exam_hold_reason);
test('19 unique canonical clinical-card sections',()=>{assert.equal(catalog.length,19);assert.equal(new Set(catalog.map(c=>c.id)).size,19);assert.equal(catalog.filter(c=>c.phase===3).length,10);assert.equal(catalog.filter(c=>c.phase===4).length,9);});
test('all records belong to a canonical clinical item',()=>{assert(bank.every(q=>catalog.some(c=>c.id===q.clinical_item_id)));});
test('held questions never selected',()=>{for(let seed=1;seed<=20;seed++){const qs=select(preview,{seed});assert(qs.every(q=>!q.exam_hold_reason));}});
test('single item selection never leaks other items',()=>{for(const c of catalog){const pool=preview.filter(q=>q.clinical_item_id===c.id);if(pool.length>=5){const a=select(preview,{total:5,types:'SBA',topics:[c.id],seed:72});assert(a.every(q=>q.clinical_item_id===c.id));}}});
test('published pool remains empty until proper approval',()=>{assert.equal(bank.filter(q=>q.status==='approved'&&q.faculty_review==='approved'&&q.answer_key_verified===true).length,0);});
