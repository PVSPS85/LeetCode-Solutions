import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Compute dense rank in descending order and convert to integer
    scores["rank"] = (
        scores["score"].rank(method="dense", ascending=False).astype(int)
    )

    # Select the required columns and sort the final output by score descending
    return scores[["score", "rank"]].sort_values(by="score", ascending=False)
