import csv

# uses spaced repetition technique to help you review your toughest problems, pulling from the data in ./exercies.md

"""
Algorithm for repeating probs:
- hard - solved in more than 45 minutes and feel like need to review 
- Medium - solved in 35
- Easy - solved in 20
- 
- 
- review probs not solved in time or feel like need to review in 1, 3, 7, 21, 90, 120 days.
 Once solved without feeling like need to review and in time twice in a row, goes to backlog. 
 If problem not solved in time without feeling like need to review, stars at beginning. If more than one problem at once - well, treat it like a queue, not a stack, so the oldest problems I struggled with will be reviewed first 
- Backlog will draw from bag of chips. Problem gets a “chip” each time it’s not solved in time without feeling like need to review 
"""

def parse_exercises(file_path):
    """
    Parses the exercises file and evaluates each problem based on its difficulty and time taken to solve.
    Only processes the 'Difficulty (Easy/Medium/Hard)' and 'Minutes to Solve' columns, ignoring all others.
    Prints specific messages if the problem is solved within the expected time for its difficulty.
    Otherwise, prints a validation error with the problematic line.
    
    Args:
        file_path (str): Path to the exercises markdown file.
    """
    with open(file_path, 'r') as file:
        # Read the file as a CSV with '|' as the delimiter
        reader = csv.DictReader(file, delimiter='|')
        
        # Strip spaces from header field names
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        
        for row in reader:
            # Stop parsing if the "Problem Tags" row is reached
            if row['Problem Name'] and row['Problem Name'].strip() == 'Problem Tags':
                break
            
            # Skip header rows, empty rows, or separator rows
            if not row['Problem Name'] or row['Problem Name'].strip() == '' or \
               row['Problem Name'].strip() == 'Problem Name' or \
               row['Problem Name'].strip().startswith('---'):
                continue
            
            try:
                # Extract only the relevant fields
                difficulty = row.get('Difficulty (Easy/Medium/Hard)', '').strip() if row.get('Difficulty (Easy/Medium/Hard)') else ''
                minutes_to_solve = row.get('Minutes to Solve', '').strip() if row.get('Minutes to Solve') else ''
                
                # Ensure values are not empty or invalid
                if not difficulty or not minutes_to_solve.isdigit():
                    continue  # Skip rows with invalid or missing data
                
                minutes_to_solve = int(minutes_to_solve)
                
                # Check if the problem was solved within the expected time for its difficulty
                if difficulty == 'Hard' and minutes_to_solve <= 45:
                    print('hard and solved in time')
                elif difficulty == 'Medium' and minutes_to_solve <= 35:
                    print('medium and solved in time')
                elif difficulty == 'Easy' and minutes_to_solve <= 20:
                    print('easy and solved in time')
                else:
                    # Print validation error if the problem doesn't meet the criteria
                    print(f'Validation error: {row}')
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f'Error parsing line: {row} - {e}')
    
    # Print completion message
    print("processing complete.")

# Example usage: Parse the exercises file and evaluate problems
parse_exercises('/Users/sarahsepanski/gitroot/technical-interview/example/exercises.md')