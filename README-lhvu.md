# Commands to setup

`conda create -n insight-bench  python=3.12`

`conda activate insight-bench`

`pip install -r requirements.txt`

`pip install -e .`

`cd tests; python test_with_litellm_ibm.py` to test the basic code


# Stats

✅ Total files = 103

```
(insight-bench) [lhvu@mpcrltune notebooks]$ grep -h '"category":' *.json | sed 's/.*"category": *"//; s/".*//' | sort | uniq -c | sort -nr
     26 Finance Management
     16 Incidents Management
     16 Goal Management
     14 Incident Management
      8 User Management
      6 Asset Management
      4 Strategic Goal Management
      4 Incidents Management.
      2 Hardware
      2 Financial Management
      2 Finance Management and User Management
      2 Asset Management & User Management
      1 Network
```
