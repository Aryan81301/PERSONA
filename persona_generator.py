"""
persona_generator.py

Uses Together AI to process Reddit posts/comments
and build a user persona with inline citations.
"""

import os
import together

# ✅ Load Together API key from an environment variable
os.environ["TOGETHER_API_KEY"] = "54215a933151dc535ef0c443a67bf3eff39e21f2c188e278051074fec4593fc1"



def build_persona(username, posts, comments):
    """
    Use Together AI LLM to generate a user persona from posts/comments.

    Args:
        username (str): Reddit username.
        posts (list): List of user's submissions.
        comments (list): List of user's comments.

    Returns:
        str: A formatted persona string with inline citations.
    """
    # Prepare user content for the prompt
    user_content = ""
    for post in posts:
        user_content += (
            f"POST:\n"
            f"Title: {post['title']}\n"
            f"Body: {post['body']}\n"
            f"URL: {post['permalink']}\n\n"
        )

    for comment in comments:
        user_content += (
            f"COMMENT:\n"
            f"{comment['body']}\n"
            f"URL: {comment['link']}\n\n"
        )

    # Strong prompt with clear instructions for inline citations
    prompt = f"""
You are an expert user research analyst.

Analyze the following Reddit posts and comments for user **{username}**.
Create a detailed **User Persona** using only the information found.

Your persona must have these sections:
1. Demographics (if possible)
2. Interests & Topics of Discussion
3. Personality Traits
4. Values & Beliefs
5. Tone & Communication Style

✅ For every insight or bullet point, cite the specific post or comment
by including the exact Reddit URL in parentheses at the end.

✅ Do not invent citations — use only the real URLs given.

✅ Example format:

Personality Traits:
- Curious and analytical. (Source: https://www.reddit.com/...)
- Enjoys detailed discussions. (Source: https://www.reddit.com/...)

---

User's posts and comments:
{user_content}
"""

    response = together.Complete.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        prompt=prompt,
        max_tokens=800,
        temperature=0.7,
    )

    persona = response["choices"][0]["text"]
    return persona
