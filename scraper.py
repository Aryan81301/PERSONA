"""
scraper.py

Scrapes a Reddit user's posts and comments,
builds a user persona using an LLM,
and outputs it to a text file.

Usage:
    python scraper.py --url <reddit_profile_url>
"""

import argparse
import os

import praw

from persona_generator import build_persona


def scrape_reddit_profile(username):
    """
    Scrape the latest posts and comments for a given Reddit username.
    Returns:
        (posts, comments): Lists of dictionaries.
    """
    reddit = praw.Reddit(
        client_id="EtTrtrXhUBLHW51UJQT6-w",
        client_secret="Jyt7tGY1xw66Naagj-UEi5grFtctpw",
        user_agent="PersonaScraper/0.1 (by u/Aryan81301)",
    )

    user = reddit.redditor(username)

    posts = []
    comments = []

    for submission in user.submissions.new(limit=20):
        posts.append(
            {
                "title": submission.title,
                "body": submission.selftext,
                "url": submission.url,
                "permalink": f"https://www.reddit.com{submission.permalink}",
            }
        )

    for comment in user.comments.new(limit=20):
        comments.append(
            {"body": comment.body, "link": f"https://www.reddit.com{comment.permalink}"}
        )

    return posts, comments


def main():
    """Parse input arguments and generate user persona."""
    parser = argparse.ArgumentParser(
        description="Scrape Reddit profile and generate user persona."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Reddit profile URL (e.g., https://www.reddit.com/user/kojied/)",
    )

    args = parser.parse_args()
    url = args.url.strip("/")
    username = url.split("/")[-1]

    posts, comments = scrape_reddit_profile(username)
    persona = build_persona(username, posts, comments)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"{username}_persona.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona generated: {output_file}")


if __name__ == "__main__":
    main()
