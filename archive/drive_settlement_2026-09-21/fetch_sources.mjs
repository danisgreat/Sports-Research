import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const root = new URL('./', import.meta.url);
const list=JSON.parse(await fs.readFile(new URL('source_requests.json',root),'utf8'));
await fs.mkdir(new URL('sources/',root),{recursive:true});
const results=[];let index=0;
function plain(html){return html.replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi,'').replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,'').replace(/<(?:\/p|\/div|br|\/h[1-6]|\/li|\/tr)[^>]*>/gi,'\n').replace(/<[^>]*>/g,' ').replace(/&nbsp;|&#160;/g,' ').replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#39;|&apos;/g,"'").replace(/[ \t]+/g,' ').replace(/\n\s*\n/g,'\n').trim();}
async function worker(){while(index<list.length){const req=list[index++];try{const r=await fetch(req.url,{signal:AbortSignal.timeout(20000)});const html=await r.text();const text=plain(html);const hash=crypto.createHash('sha256').update(html).digest('hex');const out={...req,status:r.status,urlFinal:r.url,retrieved:new Date().toISOString(),hash,chars:text.length};await fs.writeFile(new URL('sources/'+req.key+'.md',root),'# '+req.key+'\n\nURL: '+req.url+'\nHTTP: '+r.status+'\nRetrieved: '+out.retrieved+'\nRaw-response SHA256: '+hash+'\n\n'+text);results.push(out);}catch(e){results.push({...req,error:String(e)});}}}
await Promise.all(Array.from({length:8},worker));
await fs.writeFile(new URL('source_receipts.json',root),JSON.stringify(results,null,2));
console.log(JSON.stringify(results.map(({key,status,chars,error})=>({key,status,chars,error}))));
