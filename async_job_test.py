from asynchronous_queues import Job
job1 = Job("http://localhost/")
job2 = Job("https://localhost:8080/")
print(job1 < job2)