import logging
from specs import get_specs
from ui import create_ui

def main():
    try:
        # Retrieve system specifications
        specs_text = get_specs()

        # Create and display the UI with the retrieved specs
        create_ui(specs_text)  # Pass specs_text as an argument
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
