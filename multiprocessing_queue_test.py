from multiprocessing_queue import chunk_indices
for start, stop in chunk_indices(20, 6):
    print(len(r := range(start, stop)), r)
