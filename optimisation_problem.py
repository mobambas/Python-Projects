import random
import csv

def save_to_csv(user_score, optimal_score, difference, rank):
    filename = "scores.csv"
    headers = ["User Score", "Optimal Score", "Difference", "Rank"]

    # Write to CSV
    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            # Write headers only if the file is new
            if file.tell() == 0:
                writer.writerow(headers)
            writer.writerow([user_score, optimal_score, difference, rank])
        print(f"Scores saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def play_game():
    print("Welcome to the Biotech Exploration Game!")

    # Prompt user for their number
    try:
        user_submission = float(input("Enter your number (a real number): "))
    except ValueError:
        print("Invalid input. Please enter a real number.")
        return

    # Generate random numbers for the other four players (uniformly between 0 and 25 for simplicity)
    other_submissions = [round(random.uniform(0, 25), 2) for _ in range(4)]
    
    print(f"Other players submitted: {other_submissions}")

    # Calculate the total sum (S)
    total_sum = user_submission + sum(other_submissions)

    if total_sum > 50:
        print("Warning: Total submissions exceed 50. Scores will be negative.")

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

    # Display the results
    print(f"Total sum (S): {sum(other_submissions)} (T) + {user_submission} = {total_sum}")
    print(f"Remaining value (50 - S): {remaining_value}")
    print(f"Your score: {user_score:.2f}")
    print(f"The most optimal number for you to select would have been: {optimal_submission:.2f}, which would have given you a score of {optimal_score:.2f}")
    print(f"The difference between your submission and the optimal submission is: {difference:.2f}")
    print(f"You ranked {user_rank} out of 5.")

    # Save scores to CSV
    save_to_csv(user_submission, optimal_submission, difference, user_rank)

# Run the game
if __name__ == "__main__":
    play_game()