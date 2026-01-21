from rapidfuzz import process, fuzz
from names_data import names

def find_matches(user_input, top_n=5):
    matches = process.extract(
        user_input,
        names,
        scorer=fuzz.ratio,
        limit=top_n
    )

    result = []
    for name, score, _ in matches:
        result.append({
            "name": name,
            "score": round(score / 100, 2)
        })

    return result
