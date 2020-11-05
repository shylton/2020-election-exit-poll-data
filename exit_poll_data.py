import requests
import bs4
import csv

"""A simple script to save the exit poll data from abcnews.com into a csv file
"""
page = requests.get('https://abcnews.go.com/Elections/exit-polls-2020'
                    '-us-presidential-election-results-analysis')
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
questions = soup.select('.PollContent__Question')

with open('election_data.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    # header row
    writer.writerow(['Question', 'Answer', 'Voted (D)', 'Voted (R)'])
    for question in questions:
        q = question.caption.getText()  # get question header
        # navigate ea table row
        for row in question.tbody.contents:
            csv_data = []
            csv_data.append(q)
            for data in row.contents:
                csv_data.append(data.getText())
            writer.writerow(csv_data)
