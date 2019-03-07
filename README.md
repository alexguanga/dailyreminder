# Daily Email Generator
---
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
```
todoist==0.0.1
itertools==5.0.0
TwitterAPI==2.5.9
myfitnesspal==1.13.3
```

### API's Requirements
- Before the script is put into production, you must make sure that Twitter, MyFitnessPal, and Todoist API are properly set-up.
  1. **Twitter**: Please follow the instructions on https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html
  2. **MyFitnessPal**: Clone the GitHub Package https://github.com/coddingtonbear/python-myfitnesspal or `pip install myfitnesspal`
  3. **Todoist**: Generate a `TODOIST_ACCESS_TOKEN_KEY` from the Todoist App on your mobile device or web browser.


### Installing
```
git clone https://github.com/alexguanga/dailyreminder.git
cd ./dailyreminder
```

### API Configuration
After the API's Requirements are correctly configured, include them into API_CONFIG.py file. Include information accordingly to their specific task.


### Run Script
```
python3 __main__.py
```

---
## Output

Below is an email example (what I receive every morning)
![Alt text](/images/DailyJournal.png)
