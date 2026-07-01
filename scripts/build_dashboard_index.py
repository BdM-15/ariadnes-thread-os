#!/usr/bin/env python3
"""Build index.html from KomputerMechanic template for Ariadne Agent OS live dashboard."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "hermes-dashboard-inspiration" / "KomputerMechanic-Hermes-Dashboard-Template.html"
OUT = ROOT / "index.html"

PARTY_JS = """
    const PARTY_ORDER=['hermes','iris','clio','odysseus','hephaestus'];
    const ACCENTS={hermes:'#A78BFA',iris:'#7DD3FC',clio:'#F472B6',odysseus:'#E879F9',hephaestus:'#FBBF24'};
    const AGENT_META={
      hermes:{code:'HER',name:'Hermes',platform:'Profile',role:'Guildmaster / Orchestrator'},
      iris:{code:'IRIS',name:'Iris',platform:'Profile',role:'Scout / Intel Researcher'},
      clio:{code:'CLIO',name:'Clio',platform:'Profile',role:'Packet Filler / Scribe'},
      odysseus:{code:'ODY',name:'Odysseus',platform:'Profile',role:'Knight / Strategist'},
      hephaestus:{code:'HEP',name:'Hephaestus',platform:'Profile',role:'Artificer / Builder'},
    };
    const DONUT_COLORS={hermes:'#A78BFA',iris:'#7DD3FC',clio:'#F472B6',odysseus:'#E879F9',hephaestus:'#FBBF24'};
    const CONTENT_AGENTS=PARTY_ORDER;
""".strip()

LIVE_API_JS = r"""
    async function apiJson(url,opts={}){
      const headers={'Accept':'application/json',...(opts.headers||{})};
      if(opts.body&&!(opts.body instanceof FormData))headers['Content-Type']='application/json';
      const r=await fetch(url,{...opts,headers});
      if(!r.ok)throw new Error(`${r.status} ${r.statusText}`);
      return r.json();
    }
    function ensureSnapshotCompat(d){
      d.stats=d.stats||{total:0,completed:0,failed:0};
      d.vps=d.vps||{cpu_pct:0,mem_pct:0,disk_pct:0,mem_used_mb:0,mem_total_mb:0,disk_used_gb:0,disk_total_gb:0,db_size_mb:0};
      d.sessions=d.sessions||{count:5,totals:{messages:0,input_tokens:0,cache_read_tokens:0}};
      d.kanban=d.kanban||{total:(d.board?.total||0)};
      if(!d.crons?.length)d.crons=(d.cron?.jobs||[]);
      return d;
    }
    async function loadBoard(){
      try{
        const data=await apiJson('/api/board');
        boardTasks=normBoardPayload(data);
      }catch(e){
        console.warn('board load',e);
        boardTasks=normBoardPayload(snapshot?.board||{});
      }
      renderBoard();
    }
    async function updateBoardTask(id,payload){
      await apiJson(`/api/board/update?id=${encodeURIComponent(id)}`,{method:'POST',body:JSON.stringify(payload)});
      await loadBoard();
    }
    async function deleteBoardTask(id){
      await apiJson(`/api/board/delete?id=${encodeURIComponent(id)}`,{method:'POST',body:'{}'});
      await loadBoard();
    }
    async function createBoardTask(){
      const title=$('taskTitleInput')?.value.trim();
      if(!title)return;
      await apiJson('/api/board',{method:'POST',body:JSON.stringify({
        title,priority:$('taskPriorityInput').value,status:$('taskStatusInput').value,notes:''
      })});
      $('taskTitleInput').value='';
      $('addTaskPanel').classList.remove('open');
      await loadBoard();
    }
    function applySnapshot(d){
      ensureSnapshotCompat(d);
      snapshot=d;
      render(d);
      if(d.board?.tasks?.length){
        boardTasks=normBoardPayload(d.board);
        renderBoard();
      }
      if(document.querySelector('[data-panel="content"].active'))loadContentDocs();
    }
    function poll(){
      apiJson('/api/snapshot').then(applySnapshot).catch(e=>console.warn('snapshot',e));
    }
    function connectSSE(){
      try{
        const es=new EventSource('/events');
        es.addEventListener('snapshot',ev=>{
          try{applySnapshot(JSON.parse(ev.data));}catch(_){}
        });
        es.onerror=()=>{};
      }catch(e){console.warn('sse',e);}
      poll();
      if(pollTimer)clearInterval(pollTimer);
      pollTimer=setInterval(poll,15000);
    }
""".strip()


def strip_static_blocks(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    skip_prefixes = (
        "    const STATIC_EXPORT=",
        "    const STATIC_SNAPSHOT=",
        "    const STATIC_BOARD_TASKS=",
        "    const EMBEDDED_CONTENT_DOCS=",
    )
    for line in lines:
        if any(line.startswith(p) for p in skip_prefixes):
            continue
        out.append(line)
    return "".join(out)


def main() -> None:
    text = TEMPLATE.read_text(encoding="utf-8")
    text = strip_static_blocks(text)

    replacements = [
        (
            "<title>Hermes / Orchestrator Mission Control — Hardcoded Static Export</title>",
            "<title>Ariadne's Thread / Agent OS Mission Control</title>",
        ),
        (
            '<a class="brand" aria-label="Hermes Orchestrator" href="#overview">',
            '<a class="brand" aria-label="Ariadne Agent OS" href="#overview">',
        ),
        (
            '<span class="brand-title">Hermes</span><span class="brand-meta"><span class="mono">/ Orchestrator</span><span class="version-badge">v2.5 static</span>',
            "<span class=\"brand-title\">Ariadne's Thread</span><span class=\"brand-meta\"><span class=\"mono\">/ Agent OS Mission Control</span><span class=\"version-badge\">live</span>",
        ),
        (
            '<span class="mono">Hermes Orchestrator</span>',
            '<span class="mono">Ariadne Agent OS</span>',
        ),
        (
            '<div class="label">VPS Health</div>',
            '<div class="label">Host Health</div>',
        ),
        (
            '<span class="label">Hermes DBs</span>',
            '<span class="label">Activity DB</span>',
        ),
        (
            "async function apiJson(url,opts={}){throw new Error('Static hardcoded export: network APIs disabled')}",
            LIVE_API_JS,
        ),
        (
            "async function loadBoard(){boardTasks=STATIC_BOARD_TASKS.map(t=>({...t}));renderBoard()}",
            "",
        ),
        (
            "async function updateBoardTask(id,payload){boardTasks=boardTasks.map(t=>String(t.id)===String(id)?{...t,...payload,updated_at:new Date().toISOString()}:t);renderBoard()}",
            "",
        ),
        (
            "async function deleteBoardTask(id){boardTasks=boardTasks.filter(t=>String(t.id)!==String(id));renderBoard()}",
            "",
        ),
        (
            "async function createBoardTask(){const title=$('taskTitleInput')?.value.trim();if(!title)return;const payload={id:'static-'+Date.now(),title,priority:$('taskPriorityInput').value,status:$('taskStatusInput').value,assignee:'operator',notes:'Static local-only demo task',created_at:new Date().toISOString(),updated_at:new Date().toISOString()};boardTasks.unshift(payload);$('taskTitleInput').value='';$('addTaskPanel').classList.remove('open');renderBoard()}",
            "",
        ),
        (
            "function poll(){render(STATIC_SNAPSHOT)}",
            "",
        ),
        (
            "function connectSSE(){render(STATIC_SNAPSHOT)}",
            "",
        ),
        (
            "render(STATIC_SNAPSHOT);loadBoard();",
            "connectSSE();loadBoard();",
        ),
        (
            "const ACCENTS={orchestrator:'#A78BFA',scout:'#7DD3FC',scribe:'#F472B6',reach:'#E879F9',dev:'#A78BFA'},AGENT_META={orchestrator:{code:'ORCH',name:'Orchestrator',platform:'Telegram',role:'Top-level operational coordinator routing work across Scout, Scribe, Reach, and Dev.'},scout:{code:'SCNT',name:'Scout',platform:'Discord',role:'Research, sourcing, trend intelligence, and reconnaissance briefs.'},scribe:{code:'SCRB',name:'Scribe',platform:'Discord',role:'Writing, content shaping, scripts, summaries, and editorial polish.'},reach:{code:'RECH',name:'Reach',platform:'Discord',role:'Marketing, growth, campaigns, distribution, and audience development.'},dev:{code:'DEV',name:'Dev',platform:'Discord',role:'Development, automation, integrations, and technical systems.'}};",
            PARTY_JS + ";",
        ),
        (
            "function normAgents(){const arr=(snapshot?.agents||[]).map(a=>({name:agentName(a),total:n(a.total),completed:n(a.completed),failed:n(a.failed),last_task:a.last_task||'',last_status:a.last_status||a.status||'unknown',model:a.model||'',last_seen:a.last_seen||''}));['orchestrator','scout','scribe','reach','dev'].forEach(x=>{if(!arr.find(a=>a.name.toLowerCase()===x))arr.push({name:x,total:0,completed:0,failed:0,last_status:'idle',last_task:'idle'})});return arr}",
            "function normAgents(){const arr=(snapshot?.agents||[]).map(a=>({name:agentName(a),total:n(a.total||a.responses),completed:n(a.completed),failed:n(a.failed),last_task:a.last_task||'',last_status:a.last_status||a.status||'unknown',model:a.model||'',last_seen:a.last_seen||''}));PARTY_ORDER.forEach(x=>{if(!arr.find(a=>agentKey(a.name)===x))arr.push({name:x,total:0,completed:0,failed:0,last_status:'idle',last_task:'idle'})});return arr.sort((a,b)=>PARTY_ORDER.indexOf(agentKey(a.name))-PARTY_ORDER.indexOf(agentKey(b.name)))}",
        ),
        (
            "function agentKey(v){const s=String(v||'').toLowerCase();return s.includes('orchestrator')?'orchestrator':s.includes('scout')?'scout':s.includes('scribe')?'scribe':s.includes('reach')?'reach':s.includes('dev')?'dev':s||'agent'}",
            "function agentKey(v){const s=String(v||'').toLowerCase();if(PARTY_ORDER.includes(s))return s;if(s.includes('hermes'))return'hermes';if(s.includes('iris'))return'iris';if(s.includes('clio'))return'clio';if(s.includes('odysseus'))return'odysseus';if(s.includes('hephaestus'))return'hephaestus';return s||'agent'}",
        ),
        (
            "const order=['orchestrator','scout','scribe','reach','dev'],agents=normAgents().sort((a,b)=>order.indexOf(agentKey(a.name))-order.indexOf(agentKey(b.name)))",
            "const order=PARTY_ORDER,agents=normAgents()",
        ),
        (
            "const DONUT_COLORS={orchestrator:'#A78BFA',scout:'#7DD3FC',scribe:'#F472B6',reach:'#FBBF24',dev:'#E879F9'};",
            "",
        ),
        (
            "drawAgentDonut(normAgents().sort((a,b)=>['orchestrator','scout','scribe','reach','dev'].indexOf(agentKey(a.name))-['orchestrator','scout','scribe','reach','dev'].indexOf(agentKey(b.name))))",
            "drawAgentDonut(normAgents())",
        ),
        (
            "const codes=['all','orchestrator','scout','scribe','reach','dev'];",
            "const codes=['all',...PARTY_ORDER];",
        ),
        (
            "const CONTENT_AGENTS=['orchestrator','scout','scribe','reach','dev'];",
            "",
        ),
        (
            "const embeddedDocMeta=()=>EMBEDDED_CONTENT_DOCS.map(doc=>({agent:doc.agent,filename:doc.filename,title:doc.title,modified_at:doc.modified_at}));",
            "const embeddedDocMeta=()=>[];",
        ),
        (
            "const embeddedDocText=d=>(EMBEDDED_CONTENT_DOCS.find(x=>x.agent===d.agent&&x.filename===d.filename)?.text||'');",
            "const embeddedDocText=d=>d.preview||'';",
        ),
        (
            "const shouldUseEmbeddedContent=()=>true;",
            "const shouldUseEmbeddedContent=()=>false;",
        ),
        (
            "async function loadContentDocs(){try{let data=embeddedDocMeta();contentDocs=Array.isArray(data)?data:Array.isArray(data?.docs)?data.docs:Array.isArray(data?.items)?data.items:[];",
            "async function loadContentDocs(){try{let data=snapshot?.content?.docs||[];if(!data.length){const snap=await apiJson('/api/snapshot');data=snap?.content?.docs||[]}contentDocs=Array.isArray(data)?data:[];",
        ),
        (
            "async function selectContentDoc(key){const d=contentDocs.find(x=>docKey(x)===key);if(!d)return;selectedDoc=d;renderContentList();selectedText=embeddedDocText(d)||'';renderContentReader()}",
            "async function selectContentDoc(key){const d=contentDocs.find(x=>docKey(x)===key);if(!d)return;selectedDoc=d;renderContentList();if(d.path){try{const r=await apiJson('/api/content?path='+encodeURIComponent(d.path));selectedText=r.text||d.preview||'';}catch(_){selectedText=d.preview||'';}}else selectedText=d.preview||embeddedDocText(d)||'';renderContentReader()}",
        ),
        (
            "$('overviewVersion').textContent=`v2.5 static · ${new Date(d.generated_at||Date.now()).toLocaleTimeString([],{hour12:false})}`;",
            "$('overviewVersion').textContent=`Agent OS · ${new Date(d.generated_at||Date.now()).toLocaleTimeString([],{hour12:false})}`;",
        ),
        (
            "const seed=({orchestrator:18,scout:24,scribe:21,reach:16,dev:28}[key]||17);",
            "const seed=({hermes:18,iris:24,clio:21,odysseus:16,hephaestus:28}[key]||17);",
        ),
        (
            '<select class="content-select" id="newDocAgent"><option value="orchestrator">Orchestrator</option><option value="scout">Scout</option><option value="scribe">Scribe</option><option value="reach">Reach</option><option value="dev">Dev</option></select>',
            '<select class="content-select" id="newDocAgent"><option value="hermes">Hermes</option><option value="iris">Iris</option><option value="clio">Clio</option><option value="odysseus">Odysseus</option><option value="hephaestus">Hephaestus</option></select>',
        ),
    ]

    for old, new in replacements:
        if old not in text:
            print("WARN missing:", old[:80])
        text = text.replace(old, new)

    text = text.replace(
        "meta=AGENT_META[key]||{code:key.slice(0,4).toUpperCase(),name:a.name,platform:'Discord',role:'Specialist agent.'}",
        "meta=(()=>{const r=(snapshot?.agents_roster||[]).find(x=>agentKey(x.name||x.display)===key);return{code:AGENT_META[key]?.code||key.slice(0,4).toUpperCase(),name:AGENT_META[key]?.name||a.name,platform:'Profile',role:r?.role||AGENT_META[key]?.role||'Party agent.'};})()",
    )

    OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()