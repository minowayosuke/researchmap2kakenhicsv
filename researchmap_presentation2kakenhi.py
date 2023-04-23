import jsonlines
import csv

def process_jsonl_to_csv(jsonl_file, csv_file):
    with jsonlines.open(jsonl_file) as reader, open(csv_file, mode='w', encoding='shift_jis', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for obj in reader:
            merge = obj['merge']

            # Get presenters
            presenters = ','.join([p['name'] for p in list(merge['presenters'].values())[0]])

            # Get presentation_title
            presentation_title = list(merge['presentation_title'].values())[0]

            # Get event
            event = list(merge['event'].values())[0]

            # Get from_event_date and to_event_date
            from_event_year = merge['from_event_date'][:4]
            to_event_year = merge['to_event_date'][:4]

            # Get invited flag
            invited = int(merge['invited'])

            # Get languages flag
            languages_flag = int('languages' in merge and 'eng' in merge['languages'])

            # Write to CSV
            csv_writer.writerow([presenters, presentation_title, event, from_event_year, to_event_year, invited, languages_flag])

# Use the function to process your JSONL file
process_jsonl_to_csv('test.jsonl', 'output.csv')