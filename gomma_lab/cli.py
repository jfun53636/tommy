from importlib.resources import files

EXPERIMENTS = [
    ("EXPERIMENT 1 - GRADIENT DESCENT", "gradient.py"),
    ("EXPERIMENT 2 - SEARCHING TECHNIQUES", "searching.py"),
    ("EXPERIMENT 3 - K-MEANS CLUSTERING", "clustering.py"),
    ("EXPERIMENT 4 - SVM CLASSIFICATION", "classification.py"),
    ("EXPERIMENT 5 - CNN IMAGE CLASSIFICATION", "cnn.py"),
    ("EXPERIMENT 6 - LSTM TIME SERIES PREDICTION", "lstm.py"),
]


def main():
    package = files("gomma_lab")

    for title, filename in EXPERIMENTS:
        print("\\n" + "=" * 70)
        print(title)
        print("=" * 70 + "\\n")

        code = package.joinpath(filename).read_text(encoding="utf-8")
        print(code)
        print("\\n" + "=" * 70)


if __name__ == "__main__":
    main()
