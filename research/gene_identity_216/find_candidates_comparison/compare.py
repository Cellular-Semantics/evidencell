import json,sys
for n in ['olm_cell_ca1','chrna2_olm_subfamily_chamberland','avpv_kiss1_neuron','bla_glutamatergic_principal_neuron']:
    for r in (0,1):
        b=json.load(open(f'before_{n}_r{r}.json')); a=json.load(open(f'after_{n}_r{r}.json'))
        bl=[(c['node_id'],c.get('score')) for c in b['candidates']]; al=[(c['node_id'],c.get('score')) for c in a['candidates']]
        same=bl==al
        print(f"\n== {n} rank {r}: {'IDENTICAL' if same else 'DIFFERS'}  unscored(before)={b.get('unscored_protein_alias_markers')} not_measured before={b.get('not_measured_genes')} after={a.get('not_measured_genes')}")
        if not same:
            lab={c['node_id']:c['label'] for c in b['candidates']+a['candidates']}
            for i in range(max(len(bl),len(al))):
                x=bl[i] if i<len(bl) else None; y=al[i] if i<len(al) else None
                mark='' if x==y else '  <--'
                print(f"  {i+1:2} {str(x and (lab[x[0]][:24],x[1])):40} {str(y and (lab[y[0]][:24],y[1])):40}{mark}")
