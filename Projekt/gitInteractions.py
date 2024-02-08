# pip install requests

import requests
from getpass import getpass

def create_github_discussion(repo_owner, repo_name, title, body, token):
    # Set the API endpoint for creating discussions
    api_url = f"https://api.github.com/jonasDHBW/codespaces-jupyter/{repo_owner}/{repo_name}/discussions"
    
    # https://github.com/jonasDHBW/codespaces-jupyter/discussions/categories/general

    # Provide authentication token
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Discussion data
    data = {
        "title": title,
        "body": body
    }

    # Send the POST request to create a new discussion
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 201:
        print("Discussion created successfully!")
        print(f"Discussion URL: {response.json()['html_url']}")
    else:
        print(f"Failed to create discussion. Status code: {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == "__main__":
    # GitHub repository information
    owner = "jonasDHBW"  # Replace with your GitHub username or organization
    repo = "codespaces-jupyter"  # Replace with the name of your repository

    # Discussion details
    discussion_title = "Week 8"
    discussion_body = "This is the content of the new discussion."

    # GitHub personal access token with 'repo' scope
    github_token = getpass("Enter your GitHub personal access token: ")

    # Create a new discussion
    create_github_discussion(owner, repo, discussion_title, discussion_body, github_token)
    
    
# Replace `"YourGitHubUsername"`, `"YourRepositoryName"`, `"New Discussion Title"`, and `"This is the content of the new discussion."` with your GitHub username, repository name, discussion title, and discussion content respectively.

# This script will prompt you to enter your GitHub personal access token securely. Make sure your token has the necessary permissions to create discussions in the repository.