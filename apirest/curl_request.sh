curl -X POST -H "Content-Type:application/json" -d\
'{"time_sys":"-37.054167","active":"0","reassignment_count":"0","reopen_count":"0","sys_mod_count":"4","made_sla":"1","impact":"2","urgency":"2","priority":"2","knowledge":"1"}'
http://localhost:8000/prediction/predict/ > response.html

