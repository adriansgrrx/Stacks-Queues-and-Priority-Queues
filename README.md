# Stacks-Queues-and-Priority-Queues
a DSA activity

**Src:** https://realpython.com/queue-in-python/ <br>
**NOTE: "realpython_mat" contains all the source code. The main reason of this extraction is to get "roadmap.dot" for data examination. All of this is solely for educational purposes.**<br><br>
In this repository you will find several python files. Files with "_test.py" on its filename indicates class testers.<br><br>
To give summary:<br>
**"queues.py" has the following testers:**<br>
    -> Queue_test.py<br>
    -> Stack_test.py<br>
    -> Priority_test.py<br>

**"graph.py" has the following testers:**<br>
"cities_n_roads_rep.py" is a NetworkX and Graphviz tester. <br>
    -> graph_test.py --> general tester<br>
    -> BFSxFIFO_test.py --> Breadth-First Search Using a FIFO Queue<br>
    -> SPxBFT_test.py --> Shortest Path Using Breadth-First Traversal<br>
    -> DFSxLIFO_test.py --> Depth-First Search Using a LIFO Queue<br>
    -> Dijkstra’sAlgxPriority_test.py --> Dijkstra’s Algorithm Using a Priority Queue<br>

**Using Thread-Safe Queues**<br>
    -> thread_safe_queues.py --> where FIFO, LIFO and Priority Queues can be tested.<br> 
    **(NOTE: can be accessed in the terminal using [python thread_safe_queues.py  ---producers 1  --consumers 2  --producer-speed 1  --consumer-speed 1  --queue fifo/lifo/heap] or simply [python thread_safe_queues.py  --queue fifo/lifo/heap])**<br> 