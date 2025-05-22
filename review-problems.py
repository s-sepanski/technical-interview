"""
review-problems.py

This script analyzes your LeetCode review log in problems.md and recommends the top three highest-priority problems to review next, based on spaced repetition principles.

Algorithm:
1. Parse problems.md and extract all review events.
2. For each unique problem, find the most recent review event.
3. Filter for problems where the most recent review has 'Feel Could Benefit From Review?' == 'Y'.
4. Sort these by the most overdue (oldest review date first).
5. Print the top three problems to review, with the highest priority as number one. If there are fewer than three, print 'insufficient data'.

Benefit:
This approach ensures you focus on the problems you struggle with most and have neglected the longest, making your review sessions efficient and effective.
"""

import os
import sys
import csv
from datetime import datetime
from collections import defaultdict

PROBLEMS_MD_PATH = os.path.join(
    os.path.dirname(__file__),
    'knowledge-by-topic', 'ds-algo-theory', 'practice', 'problems.md'
)

DATE_FORMAT = "%Y-%m-%d"


def parse_problems_md(filepath):
    """
    Parses the problems.md file and returns a list of review events (dicts).
    Each event contains problem name, link, date solved, difficulty, tags, minutes, review flag, and comment.
    """
    review_events = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Find the header row
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and 'Problem Name' in line:
            header_idx = i
            break
    if header_idx is None:
        return review_events
    header = [h.strip() for h in lines[header_idx].strip().split('|')[1:-1]]
    # Parse data rows
    for line in lines[header_idx+2:]:
        if not line.strip().startswith('|') or '---' in line:
            continue
        fields = [f.strip() for f in line.strip().split('|')[1:-1]]
        if len(fields) != len(header):
            continue
        event = dict(zip(header, fields))
        review_events.append(event)
    return review_events


def get_latest_reviews(review_events):
    """
    For each unique problem, find the most recent review event.
    Returns a dict: problem name -> latest event dict.
    """
    latest_reviews = {}
    for event in review_events:
        name = event['Problem Name']
        date_str = event['Date Solved (YYYY-MM-DD)']
        try:
            date = datetime.strptime(date_str, DATE_FORMAT)
        except Exception:
            continue
        if name not in latest_reviews or date > latest_reviews[name]['_date']:
            event['_date'] = date
            latest_reviews[name] = event
    return latest_reviews


def get_top_problems_to_review(latest_reviews, top_n=3):
    """
    Returns a list of the top N problems to review, sorted by oldest review date first.
    Only includes problems where 'Feel Could Benefit From Review?' == 'Y'.
    """
    candidates = [
        event for event in latest_reviews.values()
        if event.get('Feel Could Benefit From Review? (Y/N)', '').upper() == 'Y'
    ]
    candidates.sort(key=lambda e: e['_date'])
    return candidates[:top_n]


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except Exception:
        return False


def is_example_or_placeholder(event):
    # Check for common placeholders or example data
    placeholders = [
        'plaintext name of problem', 'hyperlink to problem', 'YYYY-MM-DD',
        '[string-in-hyphenated-format]', 'plaintext comment'
    ]
    for value in event.values():
        if value in placeholders:
            return True
    return False


def main():
    if not os.path.exists(PROBLEMS_MD_PATH):
        print(f"File not found: {PROBLEMS_MD_PATH}")
        sys.exit(1)
    review_events = parse_problems_md(PROBLEMS_MD_PATH)
    valid_events = []
    errors = []
    for event in review_events:
        if is_example_or_placeholder(event):
            errors.append(f"Row with problem name '{event.get('Problem Name', '')}' appears to be example or placeholder data. Please replace with real problem information.")
            continue
        if not is_valid_date(event.get('Date Solved (YYYY-MM-DD)', '')):
            errors.append(f"Row with problem name '{event.get('Problem Name', '')}' has an invalid or missing date. Please use format YYYY-MM-DD.")
            continue
        valid_events.append(event)
    if errors:
        print("Input data errors detected:")
        for err in errors:
            print(f"- {err}")
        if not valid_events:
            print("No valid problem review data found. Please update your problems.md file.")
            return
    latest_reviews = get_latest_reviews(valid_events)
    top_problems = get_top_problems_to_review(latest_reviews, top_n=3)
    print("Top 3 problems to review:")
    for idx in range(3):
        if idx < len(top_problems):
            event = top_problems[idx]
            print(f"{idx+1}. {event['Problem Name']} ({event['Problem Link']}) - Last reviewed: {event['Date Solved (YYYY-MM-DD)']}")
        else:
            print("insufficient data")


if __name__ == "__main__":
    main()
