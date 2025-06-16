# Streamlit Frontend for Eagle Eye Tracking System

This project is a Streamlit frontend application that interacts with the Eagle Eye Tracking System backend. It provides a user-friendly interface for chat, device tracking, and number analysis functionalities.

## Project Structure

- `src/app.py`: Main entry point of the Streamlit application.
- `src/pages/chat.py`: Implementation of the chat page.
- `src/pages/tracking.py`: Implementation of the tracking page.
- `src/pages/numbers.py`: Implementation of the number analysis page.
- `src/components/sidebar.py`: Sidebar component for navigation.
- `src/utils/supabase.py`: Utility functions for Supabase database interactions.
- `src/utils/api.py`: Functions for making API calls to the backend.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd streamlit-frontend
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```

## Deployment

This application can be deployed on Render. The configuration for deployment is specified in the `render.yaml` file.

## Usage

Once the application is running, you can navigate through the different pages using the sidebar. Each page provides specific functionalities related to chat, tracking, and number analysis.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.