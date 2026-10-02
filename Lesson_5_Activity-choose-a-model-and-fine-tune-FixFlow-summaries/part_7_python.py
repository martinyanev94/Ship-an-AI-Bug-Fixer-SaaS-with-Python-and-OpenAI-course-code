import time

file = client.files.create(

    file=open("train_data_prepared.jsonl", "rb"),

    purpose="fine-tune",

)

job = client.fine_tuning.jobs.create(

    training_file=file.id,

    model="gpt-3.5-turbo",

)

while True:

    job = client.fine_tuning.jobs.retrieve(job.id)

    if job.status in ("succeeded", "failed", "cancelled"):

        break

    time.sleep(10)

if job.status == "succeeded":

    ft_id = job.fine_tuned_model

    print(ft_id)

else:

    print(job.status)
