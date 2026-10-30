"""Generate the profile's self-contained SVG artwork. Python standard library only."""

from pathlib import Path
from math import cos, sin, pi
from random import Random

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

def point(cx, cy, radius, angle):
    return f"{cx + radius * cos(angle):.2f},{cy + radius * sin(angle):.2f}"

def polygon(cx, cy, radius, sides, offset=-pi / 2):
    return " ".join(point(cx, cy, radius, offset + i * 2 * pi / sides) for i in range(sides))

rng = Random(1509)
stars = "".join(
    f'<circle cx="{rng.randrange(24, 1176)}" cy="{rng.randrange(20, 355)}" r="{rng.choice([.6, .8, 1, 1.3])}" fill="{rng.choice(["#b7a8ec", "#7cded8", "#ffffff"])}" opacity="{rng.uniform(.15, .6):.2f}"/>'
    for _ in range(95)
)
ticks = "".join(
    f'<path d="M{point(930, 208, 137, i*pi/24)} L{point(930, 208, 145 if i % 4 == 0 else 141, i*pi/24)}"/>'
    for i in range(48)
)
glyphs = "".join(
    f'<g transform="translate({point(930, 208, 118, a)}) rotate({a*180/pi+90})"><path d="M-4 4V-5L4 0L-4 1M0 -7V7"/></g>'
    for a in [i * pi / 4 for i in range(8)]
)

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440" fill="none" role="img" aria-labelledby="title desc">
<title id="title">Mohan Krishna — The Arcane Engineer</title>
<desc id="desc">A midnight violet landscape, circuit traces and a luminous magical sigil. AI agents, voice systems and software.</desc>
<defs>
 <linearGradient id="bg" x2="1200" y2="440" gradientUnits="userSpaceOnUse"><stop stop-color="#11101f"/><stop offset=".6" stop-color="#17132d"/><stop offset="1" stop-color="#0a1926"/></linearGradient>
 <radialGradient id="halo"><stop stop-color="#7961d0" stop-opacity=".25"/><stop offset="1" stop-color="#7961d0" stop-opacity="0"/></radialGradient>
 <linearGradient id="ink" x2="1" y2="1"><stop stop-color="#bda5ff"/><stop offset="1" stop-color="#63e8dd"/></linearGradient>
 <linearGradient id="mountain" x2="0" y2="1"><stop stop-color="#31264c"/><stop offset="1" stop-color="#10131f"/></linearGradient>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" stroke="#9e8cca" stroke-opacity=".045"/></pattern>
</defs>
<rect x=".5" y=".5" width="1199" height="439" rx="16" fill="url(#bg)" stroke="#3a3154"/>
<rect x="1" y="1" width="1198" height="438" rx="16" fill="url(#grid)"/>
<ellipse cx="930" cy="208" rx="270" ry="240" fill="url(#halo)"/>
{stars}
<g stroke="#8b73b8" stroke-opacity=".22" stroke-width="1">
 <path d="M704 1V58L750 104H796M1200 77H1118L1081 114M1200 309H1122L1095 282H1058M745 1V26L776 57H812M1200 348H1136L1112 324"/>
 <path d="M0 331H82L106 307H151M0 346H62L86 322H128"/>
</g>
<g fill="#a38bc6"><circle cx="796" cy="104" r="2.5"/><circle cx="812" cy="57" r="2"/><circle cx="1058" cy="282" r="2.5"/><circle cx="151" cy="307" r="2"/></g>
<g stroke="url(#ink)" stroke-width="1" opacity=".7">
 <circle cx="930" cy="208" r="145" stroke-opacity=".4"/>
 <circle cx="930" cy="208" r="131"/>
 <circle cx="930" cy="208" r="104" stroke-opacity=".55"/>
 {ticks}
 <polygon points="{polygon(930,208,99,3)}"/>
 <polygon points="{polygon(930,208,99,3,pi/2)}" stroke-opacity=".6"/>
 {glyphs}
</g>
<g transform="translate(930 208)">
 <path d="M0 -60 39 0 0 60 -39 0Z" fill="#191c36" stroke="#a995ee" stroke-width="1.5"/>
 <path d="M0 -60V60M-39 0H39" stroke="#a995ee" stroke-opacity=".35"/>
 <path d="m-11 -16-15 16 15 16m22-32 15 16-15 16M5 -24-5 24" stroke="#83f0e3" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cy="-60" r="3" fill="#e4cb8f"/><circle cy="60" r="3" fill="#e4cb8f"/>
</g>
<path d="m696 406 51-58 33 24 63-64 31 23 63-58 54 75 32-29 69 55 38-28 70 64v30H696Z" fill="url(#mountain)" stroke="#655384" stroke-opacity=".35"/>
<path d="m737 440 77-58 49 25 49-56 43 33 52-29 73 55 56-32 64 46v16Z" fill="#10141f"/>
<path d="m912 351 10 24 16 10-26-34m-69-43 6 25 15 9-21-34m94-35 7 32 18 6" stroke="#a58bd2" stroke-opacity=".3"/>
<g font-family="ui-monospace, 'SFMono-Regular', Consolas, monospace">
 <path d="M52 52h20" stroke="#dfbf81" stroke-width="2"/>
 <text x="85" y="57" fill="#dfbf81" font-size="12" letter-spacing="3.2">THE ARCANE ENGINEER</text>
 <text x="52" y="106" fill="#a99dbd" font-size="13" letter-spacing="2">&lt; kirmada1509 /&gt;</text>
</g>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-weight="700" font-size="72" letter-spacing="-2.5" fill="#f2edf9">
 <text x="47" y="193">Mohan</text><text x="47" y="267">Krishna<tspan fill="#80e6da">.</tspan></text>
</g>
<path d="M52 297H107" stroke="#8d76bd"/>
<text x="52" y="332" font-family="ui-monospace, 'SFMono-Regular', Consolas, monospace" font-size="13" letter-spacing="1.2" fill="#a8a0be">AI AGENTS <tspan fill="#5ee0d2">/</tspan> VOICE SYSTEMS <tspan fill="#5ee0d2">/</tspan> SOFTWARE</text>
<g font-family="ui-monospace, 'SFMono-Regular', Consolas, monospace" font-size="10" letter-spacing="1.6">
 <circle cx="56" cy="392" r="3" fill="#81e5c1"/>
 <text x="71" y="396" fill="#bbb0ce">SYSTEM ONLINE</text>
 <text x="297" y="396" fill="#81778f">LOGIC × IMAGINATION</text>
</g>
<path d="M21 38V21h17M1162 21h17v17M21 402v17h17M1162 419h17v-17" stroke="#9d88be" stroke-opacity=".45"/>
</svg>'''
(ASSETS / "arcane-engineer.svg").write_text(hero)

footer = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="146" viewBox="0 0 1200 146" fill="none" role="img" aria-labelledby="title desc">
<title id="title">The next quest</title><desc id="desc">Build something worth shipping. Let's make it real.</desc>
<defs><linearGradient id="bg" x2="1200" y2="146" gradientUnits="userSpaceOnUse"><stop stop-color="#14101f"/><stop offset="1" stop-color="#0e1b26"/></linearGradient></defs>
<rect x=".5" y=".5" width="1199" height="145" rx="12" fill="url(#bg)" stroke="#393249"/>
<g stroke="#82709f" stroke-opacity=".4"><path d="M0 73h153l20-20h78M1200 73h-153l-20 20h-78"/><path d="M0 89h132l20-20h53M1200 57h-132l-20 20h-53"/></g>
<g stroke="#97dcd4" stroke-width="1.2"><path d="m278 65 8 8-8 8-8-8Zm644 0 8 8-8 8-8-8Z"/><path d="M286 73h35m558 0h35" stroke-opacity=".4"/></g>
<text x="600" y="36" text-anchor="middle" font-family="ui-monospace, 'SFMono-Regular', Consolas, monospace" font-size="10" letter-spacing="3" fill="#d6b980">THE NEXT QUEST</text>
<text x="600" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="28" font-weight="600" fill="#ece6f7">Build something worth shipping.</text>
<text x="600" y="113" text-anchor="middle" font-family="ui-monospace, 'SFMono-Regular', Consolas, monospace" font-size="12" fill="#97b9bd">Let's make it real.</text>
</svg>'''
(ASSETS / "questline.svg").write_text(footer)
print("Generated assets/arcane-engineer.svg and assets/questline.svg")
