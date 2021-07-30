
select 
nue.text_description ,nu.unit_title,nu.unit_code 
from 
noc_unit_example nue
left join noc_unit nu  on nue.unit_code  = nu.unit_code 



select
md.text_description ,nu.unit_title,nu.unit_code 
from public.noc_unit_main_duties md
left join noc_unit nu  on md.unit_code  = nu.unit_code 


-- Main dataset for recommendation using duties as query and titel as collaborate filter

select 
md.text_description job_duties, nue.text_description job_title , nu.unit_title noc_name,nu.unit_code noc 
from public.noc_unit_main_duties md
left join noc_unit nu  on md.unit_code  = nu.unit_code
left join noc_unit_example nue on md.unit_code  = nue.unit_code 

