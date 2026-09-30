"""
RADMO NAME SPEAKER
-------------------
A simple, colorful, futuristic name-selection app built with Streamlit.

There is NO wheel, NO spinner, NO roulette and NO pie-chart selector.
The entire experience is one big glowing balloon, one POP button, and a
name that briefly appears, speaks itself, and automatically disappears:

    ADD NAMES -> 🎈 BIG BALLOON -> 💥 POP & SPEAK -> 👑 ONE RANDOM NAME
    -> 🔊 VOICE -> name auto-disappears after ~3s -> 🎈 ready again

Run with:
    pip install streamlit
    streamlit run radmoe_name.py
"""

import html
import json
import random

import streamlit as st
import streamlit.components.v1 as components

# =====================================================================
# PAGE CONFIG
# =====================================================================
st.set_page_config(
    page_title="RADMO NAME SPEAKER",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =====================================================================
# SESSION STATE
# =====================================================================
def init_state() -> None:
    """Initialize all session_state keys exactly once, on first load."""
    defaults = {
        "names": [],              # list[str] — the pool of loaded names
        "selected_name": None,    # str | None — the current (temporary) result
        "show_result": False,     # bool — whether a result is currently active
        "animation_id": 0,        # int — bumped on every pop/reset so the VFX
                                   #       component always remounts and replays,
                                   #       even if the same name is picked twice
        "show_add_panel": False,  # bool — whether the Add Name panel is open
        "name_input_key": 0,      # int — used to clear the text_input widget
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()


# =====================================================================
# CORE LOGIC FUNCTIONS
# =====================================================================
def add_name(raw_name: str) -> None:
    """Add a trimmed, de-duplicated name to the pool."""
    name = raw_name.strip()
    if not name:
        return
    existing_lower = {n.lower() for n in st.session_state.names}
    if name.lower() in existing_lower:
        return  # duplicates are prevented
    st.session_state.names.append(name)
    st.session_state.name_input_key += 1  # clears the input box


def remove_name(name: str) -> None:
    """Remove a single name from the pool, if present."""
    if name in st.session_state.names:
        st.session_state.names.remove(name)


def clear_all_names() -> None:
    """Wipe the entire name pool. Does not touch the current result."""
    st.session_state.names = []


def reset_system() -> None:
    """Return the balloon to idle: clears the current result and
    animation state, but leaves the name list untouched."""
    st.session_state.selected_name = None
    st.session_state.show_result = False
    st.session_state.animation_id += 1


def select_random_name():
    """Randomly pick exactly one name from the pool, then REMOVE it from
    the pool so it cannot be picked again. Every remaining name gets its
    turn exactly once; once a name has come up, it will not come up a
    second time until the user adds it again."""
    if not st.session_state.names:
        return None
    chosen = random.choice(st.session_state.names)
    st.session_state.names.remove(chosen)  # take it out of the pool
    st.session_state.selected_name = chosen
    st.session_state.show_result = True
    st.session_state.animation_id += 1
    return chosen


# =====================================================================
# GLOBAL CSS
# =====================================================================
def inject_global_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Baloo+2:wght@600;700;800&display=swap');

        :root{
            --cyan:#00E5FF; --blue:#5B5CFF; --purple:#B84DFF; --pink:#FF4DB8;
            --orange:#FF7A30; --gold:#FFD34E; --text:#EEF0FB; --text-dim:#98A0C0;
        }

        #MainMenu, header[data-testid="stHeader"], footer {visibility:hidden; height:0;}
        .stDeployButton{display:none;}
        section.main > div {padding-top: 0.6rem;}

        html, body, [data-testid="stAppViewContainer"]{
            background:
                radial-gradient(50% 40% at 50% 8%, rgba(0,229,255,0.07) 0%, transparent 60%),
                radial-gradient(55% 45% at 50% 95%, rgba(184,77,255,0.12) 0%, transparent 60%),
                linear-gradient(160deg, #070a18 0%, #0c1130 25%, #171b45 50%, #241a55 75%, #341a4d 100%) !important;
            color: var(--text);
        }
        * { font-family:'Poppins', sans-serif; }

        .radmo-title{
            font-family:'Baloo 2', sans-serif; font-weight:800;
            font-size: clamp(34px, 6vw, 66px); letter-spacing:2px; line-height:1;
            text-align:center; margin:0;
            background: linear-gradient(95deg, var(--cyan) 0%, var(--blue) 40%, var(--purple) 70%, var(--pink) 100%);
            -webkit-background-clip:text; background-clip:text; color:transparent;
            filter: drop-shadow(0 0 18px rgba(91,92,255,.4));
        }
        .radmo-sub{
            font-family:'Baloo 2', sans-serif; font-weight:700; text-align:center;
            font-size: clamp(14px,1.8vw,20px); letter-spacing:3px; color: var(--text);
            margin-top:0px; opacity:.9;
        }
        .radmo-tag{
            text-align:center; font-size:11px; letter-spacing:3px; color: var(--text-dim);
            margin: 4px 0 12px; font-weight:600;
        }

        .center-wrap{ max-width: 560px; margin: 0 auto; }

        .panel{
            background: rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.07);
            border-radius:16px; padding:14px 16px;
            margin-top: 8px;
        }
        .name-row{
            display:flex; align-items:center; justify-content:space-between;
            background: rgba(255,255,255,0.05);
            border-radius:10px; padding:8px 12px; margin-bottom:7px;
            font-weight:600; font-size:14px;
        }
        .name-row.c0{ box-shadow: inset 3px 0 0 var(--cyan); }
        .name-row.c1{ box-shadow: inset 3px 0 0 var(--blue); }
        .name-row.c2{ box-shadow: inset 3px 0 0 var(--purple); }
        .name-row.c3{ box-shadow: inset 3px 0 0 var(--pink); }
        .name-row.c4{ box-shadow: inset 3px 0 0 var(--orange); }
        .empty-hint{ color:var(--text-dim); font-size:13px; padding: 4px 2px; text-align:center; }

        div[data-testid="stButton"] button{
            font-family:'Baloo 2', sans-serif !important; font-weight:700 !important;
            letter-spacing:.5px !important; border-radius:12px !important;
            transition: transform .12s ease, box-shadow .12s ease;
        }
        div[data-testid="stButton"] button:hover{ transform: translateY(-1px); }

        div[data-testid="column"]:has(#pop-anchor) div[data-testid="stButton"] button{
            background: linear-gradient(95deg, var(--cyan), var(--purple) 50%, var(--orange)) !important;
            color:#0a0a14 !important; border:none !important;
            font-size:19px !important; padding: 15px 0 !important;
            box-shadow: 0 0 30px rgba(184,77,255,.5), 0 8px 20px -8px rgba(0,0,0,.6) !important;
        }
        div[data-testid="column"]:has(#pop-anchor) div[data-testid="stButton"] button:hover{
            box-shadow: 0 0 40px rgba(255,77,184,.6), 0 8px 20px -8px rgba(0,0,0,.6) !important;
            transform: translateY(-1px) scale(1.01);
        }

        .small-btn button{
            background: rgba(255,255,255,0.05) !important;
            border:1px solid rgba(255,255,255,0.12) !important;
            color: var(--text-dim) !important;
            font-size:13px !important;
        }

        .error-msg{
            text-align:center; margin-top:8px; color: var(--pink);
            font-size:13px; font-weight:600;
        }

        .footer-note{
            text-align:center; margin-top:22px; font-size:11px; letter-spacing:1.5px;
            color: rgba(152,160,192,.4);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =====================================================================
# HEADER
# =====================================================================
def render_header() -> None:
    st.markdown('<div class="radmo-title">RADMO</div>', unsafe_allow_html=True)
    st.markdown('<div class="radmo-sub">NAME SPEAKER</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="radmo-tag">CLICK &nbsp;•&nbsp; POP &nbsp;•&nbsp; RANDOM &nbsp;•&nbsp; SPEAK</div>',
        unsafe_allow_html=True,
    )


# =====================================================================
# BALLOON + VFX + NAME + VOICE — one synced HTML/JS component
# =====================================================================
def build_stage_html(selected_name, show_result: bool, animation_id: int) -> str:
    has_name = bool(show_result and selected_name)
    safe_name_html = html.escape(selected_name) if selected_name else ""
    js_name = json.dumps(selected_name) if selected_name else "null"

    template = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <!-- run:__RUN_ID__ -->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@700;800&family=Poppins:wght@500;600&display=swap');
        :root{
            --cyan:#00E5FF; --blue:#5B5CFF; --purple:#B84DFF; --pink:#FF4DB8; --orange:#FF7A30; --gold:#FFD34E;
        }
        html,body{ margin:0; padding:0; background:transparent; overflow:hidden;
                   font-family:'Poppins',sans-serif; color:#EEF0FB; }
        .stage{ position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; height:430px; }
        canvas#fx{ position:absolute; inset:0; width:100%; height:100%; pointer-events:none; }

        .orb-zone{ position:relative; width:340px; height:340px; max-width:92%; display:flex; align-items:center; justify-content:center; z-index:2; }
        .balloon{
            width:84%; height:84%; border-radius:50%;
            background: radial-gradient(circle at 32% 28%, rgba(255,255,255,.72), transparent 40%),
                        conic-gradient(from 210deg, var(--cyan), var(--blue), var(--purple), var(--pink), var(--orange), var(--gold), var(--cyan));
            box-shadow: 0 0 46px rgba(91,92,255,.5), 0 0 90px rgba(184,77,255,.25), inset 0 0 28px rgba(255,255,255,.22);
            animation: idleFloat 4s ease-in-out infinite, idlePulse 3s ease-in-out infinite;
            transition: opacity .2s ease, transform .2s ease, box-shadow .2s ease;
        }
        @keyframes idleFloat{ 0%,100%{ margin-top:0px;} 50%{ margin-top:-12px;} }
        @keyframes idlePulse{ 0%,100%{ filter:brightness(1) saturate(1);} 50%{ filter:brightness(1.08) saturate(1.15);} }

        .balloon.charge{
            animation: none;
            filter: brightness(1.35) saturate(1.3);
            box-shadow: 0 0 62px rgba(0,229,255,.7), 0 0 110px rgba(184,77,255,.4), inset 0 0 30px rgba(255,255,255,.3);
        }
        .balloon.build{ transform: scale(1.15); }
        .balloon.shake{ animation: shakeB .1s linear infinite; }
        @keyframes shakeB{
            0%{transform:translate(0,0) scale(1.15);} 25%{transform:translate(-3px,2px) scale(1.15);}
            50%{transform:translate(3px,-2px) scale(1.15);} 75%{transform:translate(-2px,-2px) scale(1.15);}
            100%{transform:translate(0,0) scale(1.15);}
        }
        .balloon.hidden{ opacity:0; transform:scale(1.5); }

        .spark{
            position:absolute; width:4px; height:4px; border-radius:50%;
            background:#fff; box-shadow:0 0 6px 2px rgba(255,255,255,.8);
            opacity:0; z-index:3;
        }
        .spark.show{ animation: sparkPop .5s ease-out forwards; }
        @keyframes sparkPop{ 0%{opacity:0; transform:translate(0,0) scale(.4);} 40%{opacity:1;} 100%{opacity:0; transform: translate(var(--sx), var(--sy)) scale(1);} }

        .flash{
            position:absolute; inset:0; border-radius:50%;
            background: radial-gradient(circle, rgba(255,255,255,.95), rgba(0,229,255,.5) 45%, transparent 70%);
            opacity:0; pointer-events:none; z-index:4;
        }
        .flash.go{ animation: flashPop .13s ease-out; }
        @keyframes flashPop{ 0%{ opacity:0;} 35%{ opacity:1;} 100%{ opacity:0;} }

        .result{
            position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
            text-align:center; z-index:5; opacity:0; pointer-events:none;
            transition: opacity .5s ease;
        }
        .result.show{ opacity:1; }
        .crown{ font-size:30px; opacity:0; transform:translateY(6px) scale(.8); transition: opacity .4s ease, transform .4s ease; }
        .crown.show{ opacity:1; transform:translateY(0) scale(1); }
        .result-name{
            font-family:'Baloo 2', sans-serif; font-weight:800; font-size:54px; letter-spacing:1px;
            background: linear-gradient(95deg, #ffffff 0%, var(--cyan) 30%, var(--purple) 65%, var(--gold) 100%);
            -webkit-background-clip:text; background-clip:text; color:transparent;
            filter: drop-shadow(0 0 18px rgba(91,92,255,.55)) drop-shadow(0 0 28px rgba(255,122,48,.3));
            opacity:0; transform: scale(.6); transition: opacity .45s ease, transform .45s cubic-bezier(.2,1.4,.4,1);
            max-width:340px; word-break:break-word; margin-top:4px;
        }
        .result-name.show{ opacity:1; transform:scale(1); }

        .voice-wave{ display:flex; gap:4px; justify-content:center; align-items:flex-end; height:20px; margin-top:12px; opacity:0; transition: opacity .3s ease; }
        .voice-wave.show{ opacity:1; }
        .voice-wave span{ width:4px; border-radius:2px; background: linear-gradient(180deg, var(--cyan), var(--purple)); opacity:.3; height:4px; }
        .voice-wave.active span{ animation: eqbar 1s ease-in-out infinite; opacity:1; }
        .voice-wave span:nth-child(2n){ animation-delay:.15s; } .voice-wave span:nth-child(3n){ animation-delay:.3s; }
        @keyframes eqbar{ 0%,100%{ height:4px;} 50%{ height:18px;} }
    </style>
    </head>
    <body>
    <div class="stage">
        <canvas id="fx"></canvas>
        <div class="orb-zone" id="orbZone">
            <div class="flash" id="flash"></div>
            <div class="balloon" id="balloon"></div>
        </div>
        <div class="result" id="result">
            <div class="crown" id="crown">&#128081;</div>
            <div class="result-name" id="resultName">__SAFE_NAME__</div>
            <div class="voice-wave" id="voiceWave">
                <span></span><span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
        </div>
    </div>

    <script>
    (function(){
        var hasName = __HAS_NAME__;
        var selectedName = __JS_NAME__;

        var canvas = document.getElementById('fx');
        var ctx = canvas.getContext('2d');
        var dpr = Math.min(window.devicePixelRatio || 1, 2);
        function resize(){
            var w = canvas.parentElement.clientWidth, h = canvas.parentElement.clientHeight;
            canvas.width = w * dpr; canvas.height = h * dpr;
            canvas.style.width = w+'px'; canvas.style.height = h+'px';
            ctx.setTransform(dpr,0,0,dpr,0,0);
        }
        resize();
        window.addEventListener('resize', resize);

        var palette = ['#00E5FF','#5B5CFF','#B84DFF','#FF4DB8','#FF7A30','#FFD34E'];
        var ringColors = ['#00E5FF','#5B5CFF','#B84DFF','#FF4DB8','#FF7A30'];

        function energyPop(cx, cy){
            var particles = [];
            var count = 46;
            for(var i=0;i<count;i++){
                var ang = Math.random()*Math.PI*2;
                var speed = 1.3 + Math.random()*4.2;
                var shapeRoll = Math.random();
                var shape = shapeRoll < 0.65 ? 'circle' : (shapeRoll < 0.85 ? 'confetti' : 'star');
                particles.push({
                    x:cx, y:cy, vx:Math.cos(ang)*speed, vy:Math.sin(ang)*speed,
                    life:1, decay:0.013+Math.random()*0.015,
                    size: shape === 'confetti' ? (3+Math.random()*3) : (1.4+Math.random()*3.0),
                    color: palette[Math.floor(Math.random()*palette.length)],
                    shape: shape, rot: Math.random()*Math.PI*2, rotSpeed: (Math.random()-0.5)*0.3
                });
            }
            var rings = [];
            for(var r=0;r<4;r++){ rings.push({ r:4, alpha:1, color: ringColors[r % ringColors.length], delay: r*3 }); }
            var shock = { r:2, alpha:1 };
            var arcs = [];
            var arcColors = ['#00E5FF','#B84DFF','#ffffff'];
            for(var a=0;a<3;a++){
                var ang2 = Math.random()*Math.PI*2;
                var len = 36 + Math.random()*44;
                var segs = [];
                for(var s=0;s<=5;s++){
                    var t = s/5;
                    var jitter = (Math.random()-0.5)*12;
                    segs.push({ x: cx + Math.cos(ang2)*len*t + Math.cos(ang2+Math.PI/2)*jitter,
                                y: cy + Math.sin(ang2)*len*t + Math.sin(ang2+Math.PI/2)*jitter });
                }
                arcs.push({ segs: segs, life: 1, color: arcColors[a % arcColors.length] });
            }
            var frame = 0;

            function drawStar(x,y,size,rot){
                ctx.save(); ctx.translate(x,y); ctx.rotate(rot);
                ctx.beginPath();
                for(var k=0;k<4;k++){
                    var ang3 = (Math.PI/2)*k;
                    ctx.lineTo(Math.cos(ang3)*size, Math.sin(ang3)*size);
                    ctx.lineTo(Math.cos(ang3+Math.PI/4)*size*0.4, Math.sin(ang3+Math.PI/4)*size*0.4);
                }
                ctx.closePath(); ctx.fill(); ctx.restore();
            }

            function step(){
                var w = canvas.width/dpr, h = canvas.height/dpr;
                ctx.clearRect(0,0,w,h);

                if(shock.alpha > 0){
                    shock.r += 7; shock.alpha -= 0.045;
                    var grad = ctx.createRadialGradient(cx,cy, Math.max(shock.r-10,0), cx,cy, shock.r);
                    grad.addColorStop(0, 'rgba(255,255,255,0)');
                    grad.addColorStop(0.85, 'rgba(0,229,255,'+Math.max(shock.alpha*0.5,0)+')');
                    grad.addColorStop(1, 'rgba(184,77,255,0)');
                    ctx.strokeStyle = grad; ctx.lineWidth = 3;
                    ctx.beginPath(); ctx.arc(cx,cy, shock.r, 0, Math.PI*2); ctx.stroke();
                }

                rings.forEach(function(rg){
                    if(frame < rg.delay) return;
                    rg.r += 5; rg.alpha -= 0.022;
                    if(rg.alpha > 0){
                        ctx.beginPath(); ctx.strokeStyle = rg.color; ctx.globalAlpha = Math.max(rg.alpha,0);
                        ctx.lineWidth = 2.2; ctx.shadowColor = rg.color; ctx.shadowBlur = 12;
                        ctx.arc(cx, cy, rg.r, 0, Math.PI*2); ctx.stroke();
                        ctx.shadowBlur = 0; ctx.globalAlpha = 1;
                    }
                });

                if(frame < 10){
                    arcs.forEach(function(arc){
                        arc.life -= 0.12;
                        if(arc.life <= 0) return;
                        ctx.globalAlpha = Math.max(arc.life,0);
                        ctx.strokeStyle = arc.color; ctx.shadowColor = arc.color; ctx.shadowBlur = 8; ctx.lineWidth = 1.6;
                        ctx.beginPath(); ctx.moveTo(arc.segs[0].x, arc.segs[0].y);
                        for(var si=1; si<arc.segs.length; si++){ ctx.lineTo(arc.segs[si].x, arc.segs[si].y); }
                        ctx.stroke(); ctx.shadowBlur = 0; ctx.globalAlpha = 1;
                    });
                }

                var alive = false;
                particles.forEach(function(p){
                    if(p.life <= 0) return;
                    alive = true;
                    p.x += p.vx; p.y += p.vy; p.vx *= 0.965; p.vy *= 0.965; p.life -= p.decay; p.rot += p.rotSpeed;
                    ctx.globalAlpha = Math.max(p.life,0); ctx.fillStyle = p.color; ctx.shadowColor = p.color; ctx.shadowBlur = 6;
                    if(p.shape === 'circle'){ ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI*2); ctx.fill(); }
                    else if(p.shape === 'confetti'){ ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot); ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size*0.55); ctx.restore(); }
                    else { drawStar(p.x, p.y, p.size*1.4, p.rot); }
                    ctx.shadowBlur = 0; ctx.globalAlpha = 1;
                });

                frame++;
                var ringsAlive = rings.some(function(rg){ return rg.alpha > 0; });
                if(alive || ringsAlive || shock.alpha > 0){ requestAnimationFrame(step); }
                else { ctx.clearRect(0,0,w,h); }
            }
            step();
        }

        var balloon = document.getElementById('balloon');
        var orbZone = document.getElementById('orbZone');
        var flash = document.getElementById('flash');
        var result = document.getElementById('result');
        var crown = document.getElementById('crown');
        var resultName = document.getElementById('resultName');
        var voiceWave = document.getElementById('voiceWave');

        function spawnMiniSparks(){
            for(var i=0;i<8;i++){
                var s = document.createElement('div');
                s.className = 'spark';
                var ang = Math.random()*Math.PI*2;
                var dist = 40 + Math.random()*30;
                s.style.left = '50%'; s.style.top = '50%';
                s.style.setProperty('--sx', (Math.cos(ang)*dist)+'px');
                s.style.setProperty('--sy', (Math.sin(ang)*dist)+'px');
                orbZone.appendChild(s);
                requestAnimationFrame(function(el){ return function(){ el.classList.add('show'); }; }(s));
                setTimeout(function(el){ return function(){ el.remove(); }; }(s), 600);
            }
        }

        if(!hasName){
            return; // idle — balloon floats gently, nothing else to do
        }

        // 0.0s — glow begins
        balloon.classList.add('charge');
        // 0.4s — grows
        setTimeout(function(){ balloon.classList.add('build'); }, 400);
        // 0.6s — shakes
        setTimeout(function(){ balloon.classList.add('shake'); }, 600);
        // 0.8s — small energy particles appear
        setTimeout(function(){ spawnMiniSparks(); }, 800);
        // 1.0s — flash
        setTimeout(function(){ flash.classList.add('go'); }, 1000);
        // 1.05s — POP
        setTimeout(function(){
            balloon.classList.remove('shake');
            balloon.classList.remove('build');
            balloon.classList.add('hidden');
            var rect = orbZone.getBoundingClientRect();
            var parentRect = canvas.parentElement.getBoundingClientRect();
            var cx = rect.left - parentRect.left + rect.width/2;
            var cy = rect.top - parentRect.top + rect.height/2;
            energyPop(cx, cy);
        }, 1050);
        // 1.3s — name begins appearing
        setTimeout(function(){
            result.classList.add('show');
            crown.classList.add('show');
            resultName.textContent = selectedName.toUpperCase();
            resultName.classList.add('show');
        }, 1300);
        // 1.5s — fully visible + voice starts
        setTimeout(function(){
            voiceWave.classList.add('show');
            voiceWave.classList.add('active');
            try{
                if('speechSynthesis' in window){
                    window.speechSynthesis.cancel();
                    var utter = new SpeechSynthesisUtterance('Selected name is ' + selectedName);
                    utter.rate = 0.85; utter.pitch = 1.05; utter.volume = 1.0;
                    utter.onend = function(){ voiceWave.classList.remove('active'); };
                    utter.onerror = function(){ voiceWave.classList.remove('active'); };
                    window.speechSynthesis.speak(utter);
                }
            }catch(e){}
        }, 1500);
        // 4.5s — name automatically disappears, balloon returns to idle
        setTimeout(function(){
            result.classList.remove('show');
            crown.classList.remove('show');
            resultName.classList.remove('show');
            voiceWave.classList.remove('show','active');
            balloon.classList.remove('charge','hidden');
        }, 4500);
    })();
    </script>
    </body>
    </html>
    """

    template = template.replace("__HAS_NAME__", "true" if has_name else "false")
    template = template.replace("__SAFE_NAME__", safe_name_html)
    template = template.replace("__JS_NAME__", js_name)
    template = template.replace("__RUN_ID__", str(animation_id))
    return template


def render_stage() -> None:
    stage_html = build_stage_html(
        st.session_state.selected_name,
        st.session_state.show_result,
        st.session_state.animation_id,
    )
    components.html(stage_html, height=450, scrolling=False)


# =====================================================================
# POP BUTTON
# =====================================================================
def render_pop_button() -> None:
    st.markdown('<span id="pop-anchor"></span>', unsafe_allow_html=True)
    if st.button("🎈 POP & SPEAK", key="pop_btn", use_container_width=True):
        if not st.session_state.names:
            st.session_state["_error"] = "Please add at least one name."
        else:
            st.session_state["_error"] = None
            select_random_name()
        st.rerun()

    if st.session_state.get("_error"):
        st.markdown(
            f"<div class='error-msg'>{html.escape(st.session_state['_error'])}</div>",
            unsafe_allow_html=True,
        )


# =====================================================================
# ADD NAME (collapsible, sits BELOW the balloon/pop button)
# =====================================================================
def render_add_name_panel() -> None:
    """Renders '+ ADD NAME'; when open, shows the input box AND the
    current list of saved names (each with a delete button), plus a
    Clear All Names option."""

    if not st.session_state.show_add_panel:
        if st.button("＋ ADD NAME", key="open_add", use_container_width=True):
            st.session_state.show_add_panel = True
            st.rerun()
        return

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown("<b style='letter-spacing:1px;'>ENTER NAME</b>", unsafe_allow_html=True)
    with top_r:
        st.markdown('<div class="small-btn">', unsafe_allow_html=True)
        if st.button("Close", key="close_add", use_container_width=True):
            st.session_state.show_add_panel = False
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    input_key = f"name_input_{st.session_state.name_input_key}"
    col_in, col_btn = st.columns([3, 1])
    with col_in:
        new_name = st.text_input(
            "Enter a name", key=input_key, placeholder="Enter name...",
            label_visibility="collapsed",
        )
    with col_btn:
        if st.button("ADD", key="add_btn", use_container_width=True):
            add_name(new_name)
            st.rerun()

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    if not st.session_state.names:
        st.markdown(
            "<div class='empty-hint'>No names yet — add one above.</div>",
            unsafe_allow_html=True,
        )
    else:
        for i, n in enumerate(list(st.session_state.names)):
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown(
                    f"<div class='name-row c{i % 5}'>👤&nbsp; {html.escape(n)}</div>",
                    unsafe_allow_html=True,
                )
            with c2:
                if st.button("×", key=f"del_{n}", use_container_width=True):
                    remove_name(n)
                    st.rerun()

    st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="small-btn">', unsafe_allow_html=True)
    if st.button("Clear All Names", key="clear_btn", use_container_width=True):
        clear_all_names()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# RESET
# =====================================================================
def render_reset_button() -> None:
    st.markdown('<div class="small-btn">', unsafe_allow_html=True)
    if st.button("↻ RESET", key="reset_btn", use_container_width=True):
        reset_system()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# MAIN APP LAYOUT
# =====================================================================
def main() -> None:
    inject_global_css()

    left_pad, mid, right_pad = st.columns([1, 2, 1])
    with mid:
        render_header()
        render_stage()
        render_pop_button()
        st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
        render_add_name_panel()
        st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
        render_reset_button()
        st.markdown('<div class="footer-note">RADMO NAME SPEAKER</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()