system_prompt = """
You are a text classification model with the ability to filter and categorize texts based on specified topics.
"""

user_prompt = """
Please process the provided text and filter it according to the following topics:
1. Safety
2. Privacy
3. Harassment
4. Hate Speech
5. Misinformation

For each text, determine whether it is relevant to these topics and categorize it accordingly. Return the results in JSON format, where each entry includes the original text and its classification for each topic.

**Format:**
```json
[
    {
        "classification": {
            "Safety": "Yes/No",
            "Privacy": "Yes/No",
            "Harassment": "Yes/No",
            "Hate Speech": "Yes/No",
            "Misinformation": "Yes/No"
        }
    },

]
```
"""
