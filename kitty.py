import subprocess
import os
from datetime import datetime, timedelta


def create_commit(date_obj, message):
    """
    Executes a git commit using specific environment variables to backdate it.
    """
    # Format the date for Git's environment variables
    git_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    # Set environment variables for the commit date
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = git_date
    env["GIT_COMMITTER_DATE"] = git_date

    # Modify a file to ensure there is content to commit
    with open('commit_data.txt', 'a') as f:
        f.write(f".")

    # Run the git commands
    subprocess.run(["git", "add", "commit_data.txt"], env=env, check=True)
    subprocess.run(["git", "commit", "-m", message], env=env, check=True)


def generate_github_art():
    """
    Generates commits across the last year to form a 'cat' pattern.
    """

    # A simple 7-day x 52-week grid (approx a year) representing a cat shape.
    # 1 represents a commit day, 0 represents a blank day.
    # The pattern is simplified for illustration but follows a typical design.
    # This matrix needs careful design to look good, but here is an example structure:
    # We are working backwards in time, column by column (week by week).

    # Simplified structure placeholder: Actual art takes careful matrix design.
    # This example fills some sample "pixels".
    cat_pattern = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sun
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Mon
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Tue
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Wed
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Thu
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fri
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sat
    ]

    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=364)  # Ensure a full year coverage

    print("Starting commit generation. This may take a while...")

    # Iterate through every day of the year grid
    for week_index in range(52):
        for day_index in range(7):
            current_date = start_date + timedelta(days=week_index * 7 + day_index)

            # Use the pattern to decide whether to commit
            if cat_pattern[day_index][week_index] == 1:
                create_commit(
                    datetime.combine(current_date, datetime.min.time()),
                    f"Drawing the cat on {current_date}"
                )

    print(f"Commit generation complete. {os.getcwd()} is ready to be pushed.")


if __name__ == "__main__":
    generate_github_art()