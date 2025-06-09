def handle_webhook_event(event_data):
    """
    Handle incoming GitHub webhook events.

    Args:
        event_data (dict): The data received from the GitHub webhook.

    Returns:
        str: A message indicating the result of the processing.
    """

    # Example processing logic for a pull request merged event
    if event_data.get('action') == 'closed' and event_data.get('pull_request', {}).get('merged'):
        # Process the merged pull request
        pr_title = event_data['pull_request']['title']
        pr_number = event_data['pull_request']['number']

        # TODO: Add your logic here (e.g., notify a service, update a database, etc.)
        # TODO: Run the indexing agent/code

        return f"Pull request #{pr_number} titled '{pr_title}' has been merged."

    return None

def validate_event_data(event_data):
    """
    Validate the incoming event data from GitHub.

    Args:
        event_data (dict): The data received from the GitHub webhook.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    required_keys = ['action', 'pull_request']
    return all(key in event_data for key in required_keys)
