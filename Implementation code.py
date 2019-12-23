#Algorithm 4.6 Computing level components by breadth-first search using a fifo queue.

def LevelComponents(V,E,im):
    for p in D:
        lab[p]=INIT
    curlab=1
    fifo_init(queue)

    for (p in V) and (lab[p]==INIT):
        lab[p]=curlab
        fifo_add(p,queue)
        while not fifo_empty(queue):
            s=fifo_remove(queue)
            for (q in NG) and (im[s]==im[q]):
                if lab[q]==INIT:
                    lab[q]=curlab
                    fifo_add(q,queue)
        curlab+=1
