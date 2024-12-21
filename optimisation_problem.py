import random
import csv

def save_to_csv(user_submission, optimal_submission, difference, user_rank, trial, other_submissions, total_sum, user_score, optimal_score):
    filename = "scores_2.csv"
    headers = [
        "Trial", 
        "User Submission", 
        "Optimal Submission", 
        "Difference", 
        "User Rank", 
        "Other Submissions", 
        "Total Sum", 
        "User Score", 
        "Optimal Score"
    ]

    # Write to CSV
    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            # Write headers only if the file is new
            if file.tell() == 0:
                writer.writerow(headers)
            writer.writerow([
                trial,
                user_submission,
                optimal_submission,
                difference,
                user_rank,
                other_submissions,
                total_sum,
                user_score,
                optimal_score
            ])
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def play_game():
    print("Running Automated Trials...")

    # Loop through each user submission (from 0 to 25)
    for user_submission in range(26):
        for trial in range(1, 11):  # Run 10 trials for each submission
            # Generate random numbers for the other four players (uniformly between 0 and 25)
            other_submissions = [round(random.uniform(0, 25), 2) for _ in range(4)]

            # Calculate the total sum (S)
            total_sum = user_submission + sum(other_submissions)

            # Calculate the user's score
            remaining_value = 50 - total_sum
            user_score = user_submission * remaining_value

            # Calculate scores for other players
            other_scores = [submission * remaining_value for submission in other_submissions]

            # Determine the most optimal number for the user
            optimal_submission = (50 - sum(other_submissions)) / 2
            optimal_remaining_value = 50 - (optimal_submission + sum(other_submissions))
            optimal_score = optimal_submission * optimal_remaining_value

            # Calculate the difference between the optimal score and the user's score
            difference = optimal_submission - user_submission

            # Determine position (rank) in the non-optimal case
            all_scores = other_scores + [user_score]
            sorted_scores = sorted(all_scores, reverse=True)
            user_rank = sorted_scores.index(user_score) + 1

            # Save scores to CSV
            save_to_csv(
                user_submission=user_submission,
                optimal_submission=round(optimal_submission, 2),
                difference=round(difference, 2),
                user_rank=user_rank,
                trial=trial,
                other_submissions=other_submissions,
                total_sum=round(total_sum, 2),
                user_score=round(user_score, 2),
                optimal_score=round(optimal_score, 2)
            )

    print("All trials completed and results saved to 'scores.csv'.")

# Run the automated game
if __name__ == "__main__":
    play_game()
