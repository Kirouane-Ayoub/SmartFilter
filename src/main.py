import argparse

import pandas as pd
from datasets import load_dataset
from tqdm import tqdm
from utils import extract_json_from_string, run_filter


def llm_filter(ds_name, split, target_column):
    """
    Filters a dataset using a language model to classify texts based on specified topics.

    Args:
        ds_name (str): The name of the dataset.
        split (str): The split of the dataset to use.
        target_column (str): The column containing the texts to filter.

    Returns:
        pandas.DataFrame: A dataframe containing the original texts, their classifications, and any errors.
    """
    ds = load_dataset(ds_name, split=split)
    text_list = ds[target_column]

    df_dict = []
    # Process each text in the list
    for i in tqdm(text_list, desc="Processing texts"):
        result = run_filter(i)
        objs, errors = extract_json_from_string(result)

        # Handle cases where objs or errors might be empty
        classification = objs[0]["classification"] if objs else None
        error_info = errors[0] if errors else None

        # Append results to the list
        df_dict.append(
            {"text": i, "classification": classification, "errors": error_info}
        )

    df = pd.DataFrame(df_dict)
    classification_df = pd.json_normalize(df["classification"])
    final_df = df.drop(columns=["classification"]).join(classification_df)
    # Save DataFrame to CSV file
    final_df.to_csv(
        f"{ds_name.rsplit('/')[-1]}-{target_column}-Filtered.csv", index=False
    )

    return final_df


def main():
    # Set up argparse
    parser = argparse.ArgumentParser(description="Run LLM filter on a dataset.")
    parser.add_argument(
        "--ds_name", type=str, required=True, help="Name of the dataset"
    )
    parser.add_argument(
        "--split",
        type=str,
        default="train",
        required=True,
        help="Dataset split (e.g., train, test)",
    )
    parser.add_argument(
        "--target_column",
        default="text",
        type=str,
        required=True,
        help="Column name containing text data (e.g., text, response)",
    )

    args = parser.parse_args()

    # Run the function
    llm_filter(ds_name=args.ds_name, split=args.split, target_column=args.target_column)


if __name__ == "__main__":
    main()
