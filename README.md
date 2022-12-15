# Stacks-Queues-and-Priority-Queues
a DSA activity

**Src:** https://realpython.com/queue-in-python/ <br>
**NOTE: "realpython_mat" contains all the source code. The main reason of this extraction is to get "roadmap.dot" for data examination. All of this is solely for educational purposes.**<br><br>
In this repository you will find several python files. Files with "_test.py" on its filename indicates class testers.<br><br>
To give summary:<br>
**"queues.py" has the following testers:**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *Queue_test.py*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *Stack_test.py*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.** *Priority_test.py*<br>

**"graph.py" has the following testers:**<br>
*"cities_n_roads_rep.py"* is a NetworkX and Graphviz tester. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *graph_test.py* --> general tester<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *BFSxFIFO_test.py* --> Breadth-First Search Using a FIFO Queue<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.** *SPxBFT_test.py* --> Shortest Path Using Breadth-First Traversal<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**4.** *DFSxLIFO_test.py* --> Depth-First Search Using a LIFO Queue<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.** *Dijkstra’sAlgxPriority_test.py* --> Dijkstra’s Algorithm Using a Priority Queue<br>

**Using Thread-Safe Queues py files**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *thread_safe_queues.py* --> where FIFO, LIFO and Priority Queues can be tested.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NOTE: thread_safe_queues.py can be accessed in the terminal using**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1. python thread_safe_queues.py  ---producers 1  --consumers 2  --producer-speed 1  --consumer-speed 1  --queue fifo/lifo/heap] or simply [python thread_safe_queues.py  --queue fifo/lifo/heap]**<br> 

**Using Asynchronous Queues py files**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *asynchronous_queues.py*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *async_job_test.py*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NOTE: Asynchronous Queues can be run using script. In my case the, here's the cmd/script/s I used**<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1. python -m http.server**<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2. python asynchronous_queues.py http://localhost:8000 --max-depth=4**<br> 

**Using multiprocessing.Queue for Interprocess Communication (IPC) py files**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *multiprocessing_queue.py*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *multiprocessing_queue_test.py*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NOTE: multiprocessing_queue.py can be run using script together with the MD5 hash. Here's the cmd/script/s I used**<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1. python multiprocessing_queue.py a9d1cbf71942327e98b40cf5ef38a960**<br> 