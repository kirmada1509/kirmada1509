"""Generate profile artwork using the portfolio palette and local feather mark.

Run: python3 scripts/generate-art.py (Python standard library only).
"""

from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)
feather = (ASSETS / "peacock-feather.svg").read_text().replace(
    '<svg xmlns=', '<svg x="890" y="108" width="130" height="130" xmlns=', 1
)

header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="360" viewBox="0 0 1100 360" fill="none" role="img" aria-labelledby="title desc">
<title id="title">Mohan Krishna — Software &amp; AI Engineer</title>
<desc id="desc">A charcoal portfolio header with a peach accent, restrained typography, and a teal and gold peacock feather.</desc>
<rect x=".5" y=".5" width="1099" height="359" rx="8" fill="#101113" stroke="#2a2d33"/>
<path d="M0 60H1100M0 282H1100M550 282V360" stroke="#2a2d33"/>
<g font-family="ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace">
 <text x="38" y="36" fill="#a0a4ad" font-size="11" letter-spacing="1">AI AGENTS / VOICE SYSTEMS / FULL-STACK</text>
 <circle cx="864" cy="32" r="3" fill="#91b89d"/>
 <text x="877" y="36" fill="#b4c7b8" font-size="11">OPEN TO OPPORTUNITIES</text>
</g>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">
 <text x="35" y="164" fill="#ededee" font-size="76" font-weight="600" letter-spacing="-3.5">Mohan Krishna<tspan fill="#ffab76">.</tspan></text>
 <text x="38" y="213" fill="#a0a4ad" font-size="29" letter-spacing="-.6">Software &amp; AI engineer.</text>
</g>
<rect x="866" y="95" width="177" height="156" rx="6" fill="#15171a" stroke="#2a2d33"/>
{feather}
<g font-family="ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace" font-size="10" letter-spacing=".6" fill="#858b96">
 <text x="38" y="309">EDUCATION</text><text x="582" y="309">CORE STACK</text>
</g>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" fill="#c4c7cd">
 <text x="38" y="336">BITS Pilani · Mathematics &amp; Computing</text>
 <text x="582" y="336">Python / TypeScript / LiveKit</text>
</g>
</svg>'''
(ASSETS / "profile-header.svg").write_text(header)

architecture = '''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="266" viewBox="0 0 1100 266" fill="none" role="img" aria-labelledby="title desc">
<title id="title">IntervieHire — voice infrastructure</title>
<desc id="desc">The candidate connects to LiveKit Agents over WebRTC. Deepgram handles speech to text, Fastify orchestrates server-authorized turns, and Cartesia streams speech. Interview state persists in PostgreSQL.</desc>
<defs><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".6" fill="#647288" opacity=".22"/></pattern></defs>
<rect x=".5" y=".5" width="1099" height="265" rx="8" fill="#15191e" stroke="#30333a"/>
<rect x="1" y="42" width="1098" height="180" fill="url(#dots)"/>
<path d="M0 42H1100M0 222H1100" stroke="#2a313a"/>
<g font-family="ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace" font-size="10" letter-spacing=".8">
 <rect x="24" y="18" width="6" height="6" rx="1" stroke="#8aa9d7"/>
 <text x="39" y="26" fill="#becad9">INTERVIEHIRE</text>
 <text x="878" y="26" fill="#929daa">VOICE INFRASTRUCTURE</text>
</g>
<g stroke="#9baabd" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
 <rect x="51" y="94" width="40" height="30" rx="3"/><path d="M71 124v9m-12 0h24"/>
</g>
<g font-family="ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace" fill="#aeb9c8" text-anchor="middle">
 <text x="71" y="157" font-size="12">Candidate</text><text x="167" y="111" font-size="9">WebRTC</text>
</g>
<path d="M112 128H226m-5-4 5 4-5 4" stroke="#6987ac" stroke-width="1.5"/>
<rect x="228" y="65" width="827" height="136" rx="5" fill="#171e27" stroke="#3d4a5b"/>
<path d="M228 105H1055M228 172H1055" stroke="#344252"/>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">
 <text x="251" y="91" fill="#9fc0ff" font-size="17">◇</text>
 <text x="277" y="91" fill="#d2dced" font-size="14" font-weight="500">LiveKit Agents</text>
</g>
<text x="918" y="90" fill="#91a7c4" font-size="9" font-family="ui-monospace, monospace" letter-spacing="1">VOICE RUNTIME</text>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="17" fill="#e1e8f4">
 <text x="254" y="135">Deepgram</text><text x="543" y="135">Fastify</text><text x="827" y="135">Cartesia</text>
</g>
<g font-family="ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace" font-size="10" fill="#92a2ba">
 <text x="254" y="155">Speech → text</text><text x="543" y="155">Turn orchestration</text><text x="827" y="155">Text → speech</text>
 <text x="254" y="191">Server-authorized interview state</text><text x="816" y="191">PostgreSQL persistence</text>
</g>
<path d="M429 135h49m-5-4 5 4-5 4M714 135h49m-5-4 5 4-5 4" stroke="#6987ac" stroke-width="1.5"/>
<g font-family="ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace" font-size="10">
 <text x="24" y="249" fill="#93a5bd">Bidirectional audio · WebSockets · Idempotent turns</text>
 <text x="883" y="249" fill="#c3d3ea">SELF-HOSTED PIPELINE</text>
</g>
</svg>'''
(ASSETS / "voice-architecture.svg").write_text(architecture)
print("Generated profile-header.svg and voice-architecture.svg")
