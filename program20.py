import queue
q1 = queue.Queue()
q1.put(18)
q1.put(9)
q1.put(2002)
q1.put(9)
q1.put(18)
def reverseQueue (q1src, q2srt):
    buffer = q1src.get()
    if (q1src.empty() == False):
        reverseQueue(q1src,q2dest)    #using recursion
    q2dest.put(buffer)
    return q2dest
q2dest = queue.Queue()
qReversed =  reverseQueue(q1,q2dest)
while (qReversed.empty()== False):
    print(qReversed.queue[0],end = " ")
    qReversed.get()