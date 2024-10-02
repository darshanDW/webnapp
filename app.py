from dotenv import load_dotenv
import sqlite3
import os
import google.generativeai as genai

# Load environment variables (API Key)
load_dotenv()

# Initialize SQLite connection and cursor
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to use Generative AI to get the SQL query
def get_gemini(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text  # Assuming response contains text with SQL

# Function to execute SQL query and fetch results
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Fetch schema information from the student table
cursor.execute(f"PRAGMA table_info('STUDENT')")
schema_info = cursor.fetchall()
print(schema_info)

# Example table name (dynamically assigned)
table_name = 'STUDENT'

# Extract column names dynamically from schema_info
column_names = [column[1] for column in schema_info]

# Assign a dynamic value for the example (like "Data Science" for CLASS)
example_value = "Data Science"

# Dynamically generate the prompt
prompt = [f"""
You are an expert in converting English questions to SQL query!
The SQL database has the name {table_name} and has the following columns - {', '.join(column_names)}

For example,
Example 1 - How many entries of records are present?, 
the SQL command will be something like this: SELECT COUNT(*) FROM {table_name};

Example 2 - Tell me all the students studying in {example_value} class?, 
the SQL command will be something like this: SELECT * FROM {table_name} where CLASS='{example_value}';

Also, the SQL code should not have ``` in the beginning or end and should not include the word 'SQL' in the output.
"""]

# Get a natural language question as input
x = input("Enter your question: ")

# Get the SQL query from the Generative AI model
response = get_gemini(x, prompt=prompt)

# Check if the response contains a valid query and execute it
if response:
    print(f"Generated SQL query: {response}")
    data = read_sql_query(response, "student.db")
    for row in data:
        print(row)
else:
    print("No response from AI.")
