
import pandas as pd
import numpy as np
from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

noc_structure = pd.read_csv("https://www.statcan.gc.ca/eng/statistical-programs/document/noc-cnp-2016-structure-v4-eng.csv")
noc_elements = pd.read_csv("https://www.statcan.gc.ca/eng/statistical-programs/document/noc-cnp-2016-element-v4-eng.csv")

noc_elements = noc_elements.dropna(1)

noc_structure.columns = ["level","hierarchical_structure","code","title","definition"]

##### GROUP NOC
tierOne = noc_structure[noc_structure.level == 1][["code","title","definition"]]
tierOne.columns = ["group_code","group_title","group_definition"]

##### MAJOR CODE
tierTwo = noc_structure[noc_structure.level == 2][["code","title","definition"]]
diff_row_tier = tierTwo[[len(x) > 2 for x in  tierTwo.code]].copy()

data = []
for i in range(len(diff_row_tier)):
    row = diff_row_tier.iloc[i,:].copy()
    start, end = row.code.split("-")
    for n in np.arange(int(start),int(end)+1):
        d = row.copy()
        d.code = str(n).zfill(2)
        data.append(d)

append_data = pd.DataFrame(data)


tierTwo = tierTwo[~tierTwo.code.isin(diff_row_tier.code)].append(append_data)
tierTwo.columns = ["major_code","major_title","major_definition"]

##### MINOR CODE
tierThree = noc_structure[noc_structure.level == 3][["code","title","definition"]]
tierThree.columns = ["minor_code","minor_title","minor_definition"]

##### UNIT CODE
tierFour = noc_structure[noc_structure.level == 4][["code","title","definition"]]
tierFour.columns = ["unit_code","unit_title","unit_definition"]


noc_elements.columns = ["level","code","title","type","text_description"]

noc_elements["unit_code"] = noc_elements.code.apply(lambda t: str(t).zfill(4))
noc_elements["minor_code"] = noc_elements.unit_code.apply(lambda t4: t4[:3] )
noc_elements["major_code"] = noc_elements.unit_code.apply(lambda t4: t4[:2] )
noc_elements["group_code"] = noc_elements.unit_code.apply(lambda t4: t4[:1] )


information_type = noc_elements["type"].drop_duplicates().to_list()
type_to_table = {t:"" for t in noc_elements.type.drop_duplicates().to_list()}

type_to_table["Illustrative example(s)"] = "noc_unit_example"
type_to_table["All examples"] = "noc_unit_example"
type_to_table["Exclusion(s)"] = "noc_unit_exclusion"
type_to_table["Main duties"] = "noc_unit_main_duties"
type_to_table["Employment requirements"] = "noc_unit_employment_requirements"
type_to_table["Inclusion(s)"] = "noc_unit_inclusion"
type_to_table["Additional information"] = "noc_unit_aditional_information"

### Step 3: Database Stagging/Ingest

USER = "postgres"
PASS = "pass"
HOST = "192.168.1.5"
PORT = "5432"
SCHEMA = "noc_search_engine"

db_connection_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(USER,PASS,HOST,PORT,SCHEMA)
db_connection = create_engine(db_connection_str)

tierOne.to_sql("noc_group", con=db_connection, index=False, if_exists="append", schema="public")
tierTwo.to_sql("noc_major", con=db_connection, index=False, if_exists="append", schema="public")
tierThree.to_sql("noc_minor", con=db_connection, index=False, if_exists="append", schema="public")
tierFour.to_sql("noc_unit", con=db_connection, index=False, if_exists="append", schema="public")

for i in type_to_table:
    table = type_to_table.get(i)
    df = noc_elements[noc_elements.type == i][["unit_code","text_description"]].copy()
    df.to_sql(table, con=db_connection, index=False, if_exists="append", schema="public")
