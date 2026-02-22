from datetime import datetime, timezone


def main() -> None:
    print("federated-abuse-reporting-intelligence-layer initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
