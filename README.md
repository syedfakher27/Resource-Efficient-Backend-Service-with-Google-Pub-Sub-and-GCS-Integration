# Google Pub/Sub Backend Service

This backend service is designed to handle asynchronous message processing using Google Pub/Sub while efficiently managing resources to prevent service overload. The service subscribes to a Pub/Sub topic, processes incoming messages, and interacts with a REST API, ensuring that the API remains in control without becoming overwhelmed.

## Features

- **Asynchronous Message Processing:** Subscribes to a Pub/Sub topic and pulls messages from the associated pull subscription.
- **REST API Interaction:** Sends message data to the provided REST API endpoint for further processing.
- **Flow Control:** Optimized to prevent resource overuse by limiting message batch sizes and configuring lease times.
- **Retry Mechanism:** Includes a callback function that handles message retries if necessary.

## Deployment Options

This service can be deployed using the following options:
- **Google App Engine**
- **Google Cloud Run**
- **Google Kubernetes Engine (GKE)**

**Important:** Ensure that the container does not enter sleep mode, as it would prevent the service from pulling messages from the Pub/Sub subscription.

## Environment Variables

You need to set the following environment variables before deploying the service:

- `SUBSCRIPTION_ID` (Required): The unique name of the pull subscription created in Google Pub/Sub.
- `SERVICE_URL` (Required): The backend service endpoint that will be called when the service receives a message from Pub/Sub.
- `BATCH_SIZE` (Optional): The maximum number of messages that can be processed concurrently. Default: `5`.
- `LEASE_TIME` (Optional): The timeout duration for a Pub/Sub message. Default: `15 minutes`.

## Pub/Sub Setup

1. Create a Pub/Sub topic and a pull subscription linked to the topic.
2. Deploy the service to your chosen platform (App Engine/Cloud Run/GKE).
3. Ensure the subscription and service are correctly configured to avoid service overload and optimize performance.

## Scaling and Performance

This architecture is designed for handling long-running tasks and scaling under heavy workloads by:
- Limiting the number of concurrent messages through the `BATCH_SIZE` setting.
- Managing message timeouts with the `LEASE_TIME` configuration.
- Processing messages efficiently without overwhelming the backend service.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

## Contact

For any inquiries or support, please reach out to [your email/contact info].
