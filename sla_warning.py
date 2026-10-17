"""SLA breach warning (BD-103)."""

WARN_BEFORE_MINUTES = 15


def notify(ticket, slack):
    """Warn the team's Slack channel 15 minutes before the SLA breach. No email."""
    if ticket.minutes_to_breach() <= WARN_BEFORE_MINUTES:
        slack.post(ticket.team_channel, f"{ticket.id} breaches its SLA in {ticket.minutes_to_breach()} min")
