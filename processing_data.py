import ansible_runner, os, json   
import data_transfer_pg as db

r = ansible_runner.run(private_data_dir=".", playbook="rexx_tso.yml", quiet=True)

datafile = open("mainframe.data")

data = datafile.read()

secondary=json.loads(data[1:-1])

jobs=dict()
tsos=dict()

for job in secondary['content']:
    jobinfo=job.split()
    jobname=jobinfo[0].replace('*','')
    # print(jobname)
    if jobinfo[1]=='STC':
        if jobname not in jobs:
            jobdata=[0,0,0,0]
            jobs[jobname]=jobdata
#    for info in jobinfo:
#        print(info)
        jobs[jobname][0]+=float(jobinfo[2])
        jobs[jobname][1]+=float(jobinfo[3])
        jobs[jobname][2]+=float(jobinfo[4])
        jobs[jobname][3]+=float(jobinfo[5])
    elif jobinfo[1]=='TSU':
        if jobname not in tsos:
            jobdata=[0,0,0,0]
            tsos[jobname]=jobdata
#    for info in jobinfo:
#        print(info)
        tsos[jobname][0]+=float(jobinfo[2])
        tsos[jobname][1]+=float(jobinfo[3])
        tsos[jobname][2]+=float(jobinfo[4])
        tsos[jobname][3]+=float(jobinfo[5])

data = { 'TSU': tsos, 'STC': jobs }
#print(json.dumps(data))
db.import_data(data)