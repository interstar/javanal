#! /usr/bin/python

import sys

def one_line(name,xs,shape) :
    #print name, xs
    yield ("style","_%s [shape=%s]"%(name,shape))
    while xs != [] :
        if "{" in xs[0] or "}" in xs[0] :
            xs = xs[1:]
            continue            

        if xs[0] == "extends" or xs[0] == "implements" :
            xs = xs[1:]
            continue

        if xs[0] == "" or xs[0] == '\n' : 
            xs=xs[1:]
            continue
            
        yield ("connect","""_%s -> _%s""" % (xs[0],name))
        xs = xs[1:]

                
def process(lines) :    
    for line in lines :
        items = [x.strip(",") for x in line.split(" ")]
        while (items[0] == 'public' or items[0] == 'abstract') :
            items = items[1:]
        if items[0] == 'class' : 
            for x in one_line(items[1],items[2:],"box") : 
                yield x            
            continue
        if items[0] == 'interface' : 
            for x in one_line(items[1],items[2:],"diamond") : 
                yield x
            continue
        
        raise Exception(("Unknown Line",items))


print """digraph analysis {"""
styles=[]
connects=[]
for p in process( (l for l in sys.stdin) ) :
    if p[0]=="style" : 
        styles.append(p[1])
    else :
        connects.append(p[1])
print "  {"
for s in styles: print s
print "  }"
for c in connects : print c
print """}"""
