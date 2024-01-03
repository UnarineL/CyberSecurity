import time

class SIEMDashboard:
    def __init__(self):
        self.log_entries = []

    def log_event(self, event):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {event}"
        self.log_entries.append(log_entry)

    def display_dashboard(self):
        print("SIEM Dashboard:")
        for entry in self.log_entries:
            print(f"- {entry}")

if __name__ == "__main__":
    siem = SIEMDashboard()

    # Simulate events
    siem.log_event("User login successful")
    siem.log_event("Firewall alert: Suspicious activity detected")
    siem.log_event("System update completed")

    # Display the SIEM dashboard
    siem.display_dashboard()
