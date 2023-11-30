from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
import pandas as pd

client = OpenAI()

def create_post(information):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'You are a real estate agent, you are skilled at advertising, specifically by writing Instagram posts to promote your listings.'
            },
            {
                'role': 'user',
                'content': information
            }
        ]
    )
    return response.choices[0].message.content

def process_entry(entry):
    _, row = entry
    formatted_string = '\n'.join([f'{column}={value}' for column, value in row.items()])
    end_info = '// all parameters used to generate this sample'
    post_content = create_post(formatted_string)
    separator = '-' * 20
    return f"{formatted_string}\n{end_info}\n{post_content}\n{separator}"

def parallel_process(data):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_entry, data))
    return results

if __name__ == '__main__':
    df = pd.read_csv('Housing.csv')
    random_entries = df.sample(n=20)

    output_filename = 'EXAMPLE.txt'

    with open(output_filename, 'w') as output_file:
        results = parallel_process(random_entries.iterrows())
        output_file.write('\n'.join(results))

