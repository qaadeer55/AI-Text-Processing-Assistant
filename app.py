from utils.logger import logger

from utils.file_handler import load_text

from utils.save_json import save_json
from utils.save_text import save_text

from services.summarizer import generate_summary
from services.key_points import extract_key_points
from services.action_items import extract_action_items
from services.json_generator import generate_json
from utils.validator import (
    validate_input_file,
    validate_output_folder,
    validate_prompt,
    validate_json,
)


def main():

    try:

        logger.info("Application started.")

        logger.info("Loading meeting notes...")
        validate_input_file("data/meeting_notes.txt")
        meeting_notes = load_text("data/meeting_notes.txt")

        logger.info("Generating summary...")
        summary = generate_summary(meeting_notes)

        logger.info("Extracting key points...")
        key_points = extract_key_points(meeting_notes)

        logger.info("Extracting action items...")
        action_items = extract_action_items(meeting_notes)

        logger.info("Generating structured JSON...")

        try:
            analysis = generate_json(meeting_notes)

        except Exception as e:

            logger.warning(
                f"AI failed to generate valid JSON. Using fallback. Error: {e}"
            )

            analysis = {
                "summary": summary,
                "key_points": key_points.split("\n"),
                "action_items": action_items.split("\n"),
            }

        logger.info("Validating JSON...")
        validate_json(analysis)

        validate_output_folder("outputs")
        logger.info("Saving summary...")
        save_text(summary, "summary.txt")

        validate_output_folder("outputs")
        logger.info("Saving key points...")
        save_text(key_points, "key_points.txt")

        validate_output_folder("outputs")
        logger.info("Saving action items...")
        save_text(action_items, "action_items.txt")
        
        validate_output_folder("outputs")
        logger.info("Saving analysis.json...")
        save_json(analysis, "analysis.json")

        logger.info("Displaying results...")

        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(summary)

        print()

        print("=" * 60)
        print("KEY POINTS")
        print("=" * 60)
        print(key_points)

        print()

        print("=" * 60)
        print("ACTION ITEMS")
        print("=" * 60)
        print(action_items)

        print()

        print("=" * 60)
        print("STRUCTURED JSON")
        print("=" * 60)
        print(analysis)

        print()

        logger.info("Application completed successfully.")

    except Exception as e:

        logger.exception(f"Application failed: {e}")

        raise


if __name__ == "__main__":
    main()