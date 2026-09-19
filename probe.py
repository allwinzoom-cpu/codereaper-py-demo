from codereaper import sdk
from pathlib import Path
r = sdk.scan_tier1("/target", output_dir="/out/py")
fs = [f if isinstance(f, dict) else f.model_dump() for f in (getattr(r, "findings", None) or [])]
print(f"findings: {len(fs)}")
for f in sorted(fs, key=lambda x: (x.get("cwe") or "", x["locations"][0]["path"])):
    loc = f["locations"][0]
    print(f"  {f.get('cwe'):9} {loc['path']:28}:{loc.get('start_line'):<4} conf={f.get('confidence')} {f.get('title','')[:44]}")
