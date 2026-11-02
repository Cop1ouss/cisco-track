#!/usr/bin/env python3
"""Repo health check run by CI: every JSON file parses, and every local link in
HTML and Markdown files points at a file that exists. Standard library only.
Usage: python3 .github/scripts/check_site.py [ROOT]"""
import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SKIP_DIRS = {".git", "node_modules", "dist", ".venv", "__pycache__", ".claude"}
HTML_REF = re.compile(r'''(?:href|src)\s*=\s*["']([^"'<>]+)["']''', re.I)
MD_REF = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
EXTERNAL = ("http:", "https:", "mailto:", "tel:", "data:", "javascript:", "#", "//", "blob:")

def files(*exts):
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts and not SKIP_DIRS & set(p.relative_to(ROOT).parts):
            yield p

def is_local(ref):
    return ref and not ref.startswith(EXTERNAL) and not any(c in ref for c in "${}`+") and not ref.startswith("{")

errors = []
count = {"json": 0, "links": 0}
for f in files(".json"):
    count["json"] += 1
    try:
        json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"{f.relative_to(ROOT)}: invalid JSON ({e})")

for f in files(".html", ".htm", ".md"):
    text = f.read_text(encoding="utf-8", errors="replace")
    if f.suffix == ".md":
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # code blocks are examples, not links
        refs = MD_REF.findall(text) + HTML_REF.findall(text)
    else:
        text = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.S | re.I)  # JS builds its own URLs
        refs = HTML_REF.findall(text)
    for ref in refs:
        ref = ref.strip()
        if not is_local(ref):
            continue
        path = unquote(urlsplit(ref).path)
        if not path:
            continue
        target = (ROOT / path.lstrip("/")) if path.startswith("/") else (f.parent / path)
        count["links"] += 1
        if not (target.exists() or (target / "index.html").exists()):
            errors.append(f"{f.relative_to(ROOT)}: broken link -> {ref}")

# JavaScript syntax: standalone .js files and inline <script> blocks, via `node --check`.
SCRIPT = re.compile(r"<script\b([^>]*)>(.*?)</script>", re.S | re.I)
count["js"] = 0
if shutil.which("node"):
    def node_check(code, suffix, label):
        with tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False, encoding="utf-8") as tmp:
            tmp.write(code)
        res = subprocess.run(["node", "--check", tmp.name], capture_output=True, text=True)
        count["js"] += 1
        if res.returncode:
            msg = next((l for l in res.stderr.splitlines() if "Error" in l), res.stderr.strip()[:200])
            errors.append(f"{label}: JavaScript syntax error ({msg})")
    for f in files(".js", ".mjs"):
        if "engine" in f.parts or f.name.endswith(".min.js") or f.stat().st_size > 2_000_000:
            continue
        node_check(f.read_text(encoding="utf-8", errors="replace"), f.suffix, f.relative_to(ROOT))
    for f in files(".html", ".htm"):
        for i, (attrs, code) in enumerate(SCRIPT.findall(f.read_text(encoding="utf-8", errors="replace"))):
            a = attrs.lower()
            if "src=" in a or not code.strip() or ("type=" in a and not re.search(r'type=["\']?(text/javascript|module)', a)):
                continue
            node_check(code, ".mjs" if "module" in a else ".js", f"{f.relative_to(ROOT)} <script #{i + 1}>")

print(f"checked {count['json']} JSON files, {count['links']} local links and {count['js']} scripts")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("all good")
