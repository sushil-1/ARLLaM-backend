## Step 1. Clone the Repo
To get started, clone this repository:

```bash
git clone <repository-url>
```
## Step 2. Create a .env file in ARLLaM-backend/dashboardx/utils/ 
###### It must contain the following keys
```bash
1. DB_CONNECTION_URL
2. DATABSE_NAME
3. OPENAI_API_KEY
```
#### Step 3 (Final): Setup Environment and Run
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 -r install requirements.txt
$ python3 run.py
```
#### Steps to only run
```bash
$ cd <repo root>
$ source venv/bin/activate
$ python3 run.py
```
