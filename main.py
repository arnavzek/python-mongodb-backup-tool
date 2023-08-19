import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

today = date.today()

mongodumpLocation = 'mongodump'
outputLocation = f'backups/{today}'

databaseUrl = os.getenv('DATABASE_URL')


print("Today's date:", today)

cmdLine = f'{mongodumpLocation} --uri {databaseUrl} -o {outputLocation}'

print(f'Running the command: {cmdLine}')
os.system(cmdLine)

# path = os.path.realpath(outputLocation)
# os.startfile(path)

