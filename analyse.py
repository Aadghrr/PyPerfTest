with open('log','r') as f:
    rawlog=f.read()

rawlog=rawlog.split('\n')
log=[]

#https://man7.org/linux/man-pages/man5/proc.5.html

PROCSTAT_SCHEMA = ['pid','comm','state','ppid','pgrp','sid','tty_nr',
    'tpgid','flags','minflt','cminflt','majflt','cmajflt', 'utime',
    'ctime','cstime','priority','nice','numthreads','itrealvalue',
    'starttime','vsize','rss','rsslim','startcode','endcode','startstack',
    'kstkesp','signal','blocked','sigignore','sigcatch','wchan','nswap',
    'cnswap','exitsignal','processor','rtpriority','policy','delayacct_blkio_ticks',
    'guest_time','cguest_time','start_data','end_data','start_brk','arg_start',
    'arg_end','env_start','env_end','exit_code']


data = {k:[] for k in PROCSTAT_SCHEMA}

for line in rawlog:
    for k,v in zip(data,line.split(' ')):
       data[k].append(v)
