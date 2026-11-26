"""Fill the evidence-extraction prompt for one node: fill_ee_prompt.py TEMPLATE NODE_ID CONTEXT_FILE OUT"""
import sys
tpl, nid, ctxf, out = sys.argv[1:5]
ctx = open(ctxf).read().strip()
kb = [l.split(":", 1)[1].strip() for l in ctx.splitlines() if l.startswith("KB_FILE:")][0]
ctx = "\n".join(l for l in ctx.splitlines() if not l.startswith("KB_FILE:"))
s = open(tpl).read()
for k, v in {"{node_id}": nid, "{node_context}": ctx, "{kb_file}": kb,
             "{output_dir}": "research/thalamus/20261126_thalamus_dlgn_survey"}.items():
    s = s.replace(k, v)
open(out, "w").write(s)
