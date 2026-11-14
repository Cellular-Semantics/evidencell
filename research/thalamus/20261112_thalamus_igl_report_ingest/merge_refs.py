import json
from pathlib import Path
from evidencell.references import write_quote_to_refs
D = Path("research/thalamus/20261112_thalamus_igl_report_ingest")
M = {  # author_key: (corpus, title, year, authors, pmid, doi)
"Lewandowski et al., 2004": ("14019540","Slow oscillation circuit of the intergeniculate leaflet.",2004,["M. Lewandowski","T. Błasiak"],"15366259","10.55782/ane-2004-1512"),
"Blasiak et al., 2004": ("27043440","Blockade of GABAA receptors disrupts isoperiodic neuronal oscillations in the intergeniculate leaflet of the rat.",2004,["T. Błasiak","Marian Lewandowski"],"15120585","10.1016/J.BRAINRES.2004.02.045"),
"Chrobok et al., 2016": ("12882742","Two distinct subpopulations of neurons in the thalamic intergeniculate leaflet identified by subthreshold currents.",2016,["L. Chrobok","K. Palus","M. Lewandowski"],"27208616","10.1016/j.neuroscience.2016.05.008"),
"Palus et al., 2015": ("8694896","Electrophysiology of GABAergic transmission of single intergeniculate leaflet neurons in rat.",2015,["K. Palus","Łukasz Chrobok","M. Lewandowski"],"25856520","10.55782/ane-2015-2013"),
"Palus-Chramiec et al., 2019": ("73460105","Orexin A depolarises rat intergeniculate leaflet neurons through non‐selective cation channels",2019,["K. Palus-Chramiec","L. Chrobok","M. Kępczyński","M. Lewandowski"],"30803080","10.1111/ejn.14394"),
"Pu et al., 1996": ("34655061","Ventral lateral geniculate nucleus afferents to the suprachiasmatic nucleus in the cat.",1996,["M. Pu","G. E. Pickard"],"8836531","10.1016/0006-8993(96)00340-X"),
"Chrobok et al., 2017": ("3372643","Disinhibition of the intergeniculate leaflet network in the WAG/Rij rat model of absence epilepsy",2017,["L. Chrobok","K. Palus","J. S. Jeczmien-Lazur","Anna Chrzanowska","M. Kępczyński","M. Lewandowski"],"28041911","10.1016/j.expneurol.2016.12.014"),
"Blasiak et al., 2013": ("25997395","Differential firing pattern and response to lighting conditions of rat intergeniculate leaflet neurons projecting to suprachiasmatic nucleus or contralateral intergeniculate leaflet.",2013,["T. Błasiak","Marian Lewandowski"],"23103793","10.1016/j.neuroscience.2012.10.044"),
"Blasiak et al._1, 2013": ("36406110","Relaxin‐3 innervation of the intergeniculate leaflet of the rat thalamus – neuronal tract‐tracing and in vitro electrophysiological studies",2013,["A. Błasiak","T. Błasiak","Marian Lewandowski","M. A. Hossain","John D. Wade","A. Gundlach"],"23432696","10.1111/ejn.12155"),
"Palus et al., 2017": ("27232578","Enkephalin and neuropeptide-Y interaction in the intergeniculate leaflet network, a part of the mammalian biological clock.",2017,["K. Palus","L. Chrobok","Mariusz Kepczynski","Marian Lewandowski"],"27916729","10.1016/j.neuroscience.2016.11.034"),
"Thankachan et al., 2005": ("9130790","Juxtacellular Recording/Labeling Analysis of Physiological and Anatomical Characteristics of Rat Intergeniculate Leaflet Neurons",2005,["S. Thankachan","B. Rusak"],"16207879","10.1523/JNEUROSCI.2672-05.2005"),
"Chen et al., 1996": ("17317295","Multiple NPY Receptors Coexist in Pre- and Postsynaptic Sites: Inhibition of GABA Release in Isolated Self-Innervating SCN Neurons",1996,["Gong Chen","A. N. van den Pol"],"8922427","10.1523/JNEUROSCI.16-23-07711.1996"),
"Sabbagh et al., 2020": ("219328889","Diverse GABAergic neurons organize into subtype-specific sublaminae in the ventral lateral geniculate nucleus",2020,["Ubadah Sabbagh","G. Govindaiah","R. D. Somaiya","Ryan V. Ha","Jessica C. Wei","W. Guido","Michael A. Fox"],"32497303","10.1111/jnc.15101"),
"Gouwens et al., 2020": ("213931125","Toward an integrated classification of neuronal cell types: morphoelectric and transcriptomic characterization of individual GABAergic cortical neurons",2020,["N. Gouwens","S. Sorensen","Fahimeh Baftizadeh","Agata Budzillo","B. Lee","T. Jarsky","Zhi Zhou","J. Ting","Uygar Sümbül","E. Lein","C. Koch","Z. Yao","Bosiljka Tasic","J. Berg","Gabe J. Murphy","Hongkui Zeng"],None,"10.1101/2020.02.03.932244"),
}
Q = json.load(open(D/"extracted_quotes.json"))
n=0; keys=set(); calls=0
for ak, v in Q.items():
    c,t,y,a,p,d = M[ak]
    meta={"corpus_id":c,"author_keys":[ak],"title":t,"year":y,"authors":a,"doi":d,"resolution_confidence":"HIGH"}
    if p: meta["pmid"]=p
    for q in v["quotes"]:
        k = write_quote_to_refs(Path("references/thalamus"),corpus_id=c,quote_text=q["text"],section=q["section"],source_method="ASTA_REPORT",added_by="20261112_thalamus_igl_report_ingest",paper_meta=meta)
        calls+=1; keys.add(k)
print(calls, len(keys))
