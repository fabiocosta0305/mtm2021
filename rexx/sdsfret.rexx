/* REXX */

rc=isfcalls('ON')
if rc <> 0 then exit rc

isfcols="jname jclass jtype ecpupr ecpu ziiptime ziipuse"

Address "SDSF" "ISFEXEC DA"
if rc <> 0 then exit rc

do ix=1 to JNAME.0    /* Loop for all rows returned */
    say jname.ix jclass.ix jtype.ix ecpupr.ix ecpu.ix ziiptime.ix ziipuse.ix
end

rc=isfcalls("OFF")
exit
