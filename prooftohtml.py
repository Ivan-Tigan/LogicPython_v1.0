
def makeProof(doc, tag, text, proofFile = "proof1.proof"):
    
    prf = open(proofFile,"r", encoding='utf-8')
    prflines = prf.readlines()
    proof = []
    for prfline in prflines:
        curl={
                'lhs' : prfline.replace(" ", "").split(";")[0],
                'mhs' : prfline.replace(" ", "").split(";")[1],
                'rhs' : prfline.replace(" ", "").split(";")[2]
            }
        linedepth = curl.get('lhs').split('.', 1)[1].count('|') + curl.get('lhs').split('.', 1)[1].count('{') + curl.get('lhs').split('.', 1)[1].count('}')
        curldefined = (
            {
            'linenumber' : curl.get('lhs').split('.', 1)[0],
            'depth' : linedepth,
            'type' : curl.get('lhs').split('.', 1)[1][linedepth - 1] if linedepth > 0 else "",
            'formula' : curl.get('lhs').split('.', 1)[1][linedepth:],
            'rule' : curl.get('mhs'),
            'dependencies': curl.get('rhs')
            }  
        ) 
        proof.append(curldefined)

    for line in proof:
        print(line, "\n")


    with tag('table', ('class', 'prf')):
        with tag('tr', ('class', 'prf')):
            for line in proof:
                with tag('td', ('class', 'prf')):
                    text(line['linenumber'] + '. ')
        with tag('tr', ('class', 'prf')):
            for line in proof:
                with tag('td', ('class', 'prf')):
                    with tag('table'):
                        with tag('tr', ('class', 'logicline')):
                            if(line['depth'] > 0):
                                for vline in range(0, line['depth'] - 1):
                                    with tag('td', ('class', 'vl')):
                                        text("\u00A0")
                            if(line['type'] == '|'):
                                with tag('td', ('class', 'vl')):
                                        text("\u00A0")
                                        text("\u00A0")
                            elif(line['type'] == '{'):
                                with tag('td', ('class', 'tvl')):
                                        text("\u00A0")
                                with tag('td', ('class', 'tl')):
                                        text("\u00A0")
                            elif(line['type'] == '}'):
                                with tag('td', ('class', 'bvl')):
                                        text("\u00A0")
                                with tag('td', ('class', 'bl')):
                                        text("\u00A0")
                            with tag('td'):
                                text(line['formula'])
        with tag('tr', ('class', 'prf')):
            for line in proof:
                with tag('td', ('class', 'prf')):
                    text(line['rule'])
                    
        with tag('tr', ('class', 'prf')):
            for line in proof:
                with tag('td', ('class', 'prf')):
                    text(line['dependencies'])

def makeHTML(doc, htmlOutput='index.html'):
    f = open(htmlOutput,"w+", encoding='utf-8')
    f.write(doc.getvalue())
    import webbrowser
    from time import sleep
    sleep(0.05)
    webbrowser.open(htmlOutput)
    
    