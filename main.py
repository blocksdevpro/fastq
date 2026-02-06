from fastq import FastQ

fastq = FastQ()

@fastq.task
def my_task():
    pass

@fastq.task(timeout=10)
def my_task2():
    pass