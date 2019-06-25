from pathlib import Path
from dotenv import find_dotenv, load_dotenv

def main():
    """ Simple main() to initialize environment variables.
    """
    print("Loading environment variables")

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

if __name__ == '__main__':

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    print("Executed when invoked directly")

    main()
else:
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    #print("Executed when imported")
    
    main()
