const SHELL="shell-v7", AUDIO="audio-v1";
const ARCHIVOS=["./","index.html","manifest.json","episodios.json","ejercicios.json","nube.js","fb.js","firebase-config.js","icons/icon-192.png","icons/icon-512.png","icons/apple-touch-icon.png"];

self.addEventListener("install",e=>{
  e.waitUntil(caches.open(SHELL).then(c=>c.addAll(ARCHIVOS)).then(()=>self.skipWaiting()));
});
self.addEventListener("activate",e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==SHELL&&k!==AUDIO).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));
});

// Safari exige respuestas 206 (Range) para el audio: si el MP3 está guardado, se sirve por trozos.
async function audioDesdeCache(req,resp){
  const rango=req.headers.get("range");
  if(!rango)return resp;
  const buf=await resp.arrayBuffer();
  const m=/bytes=(\d*)-(\d*)/.exec(rango);
  let ini=m[1]?parseInt(m[1],10):0;
  let fin=m[2]?parseInt(m[2],10):buf.byteLength-1;
  fin=Math.min(fin,buf.byteLength-1);
  return new Response(buf.slice(ini,fin+1),{status:206,statusText:"Partial Content",headers:{
    "Content-Type":resp.headers.get("Content-Type")||"audio/mpeg",
    "Content-Range":`bytes ${ini}-${fin}/${buf.byteLength}`,
    "Content-Length":String(fin-ini+1),
    "Accept-Ranges":"bytes"}});
}

self.addEventListener("fetch",e=>{
  const req=e.request;
  if(req.method!=="GET")return;
  const url=new URL(req.url);
  if(url.hostname==="www.gstatic.com"&&url.pathname.startsWith("/firebasejs/")){
    e.respondWith(caches.open(SHELL).then(async c=>{const hit=await c.match(req);if(hit)return hit;
      try{const r=await fetch(req);if(r.ok)c.put(req,r.clone());return r}catch(err){return hit||Response.error()}}));
    return;
  }
  if(url.origin!==location.origin)return;
  if(url.pathname.endsWith(".mp3")){
    e.respondWith((async()=>{
      const c=await caches.open(AUDIO);
      const hit=await c.match(req.url,{ignoreSearch:true});
      if(hit)return audioDesdeCache(req,hit);
      return fetch(req);
    })());
    return;
  }
  // Resto: red primero (para ver episodios nuevos), caché si no hay conexión.
  e.respondWith(fetch(req,{cache:"no-store"}).then(r=>{
    if(r.ok){const copia=r.clone();caches.open(SHELL).then(c=>c.put(req,copia))}
    return r;
  }).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>r||caches.match("index.html"))));
});
