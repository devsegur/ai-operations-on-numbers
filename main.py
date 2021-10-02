import dataset_creator
import execute_training_and_test

csv_path = "data/dataset.csv"


def main():
    print("Starting process")

    dataset_creator.main(csv_path, 100)

    print("dataset created")

    print("training and test start")

    execute_training_and_test.main(csv_path)

    print("done")


if __name__ == '__main__':
    main()
