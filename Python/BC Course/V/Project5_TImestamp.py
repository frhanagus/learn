for hour in range(24):
  # Format hour string with leading zero if needed
  hour_str = f"{hour:02d}"

  for minute in range(60):
    # Format minute string with leading zero if needed
    minute_str = f"{minute:02d}"

    # Combine and print the time string
    print(f"{hour_str}:{minute_str}")
