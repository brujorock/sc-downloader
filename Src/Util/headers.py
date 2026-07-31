# 3.12.23 -> 10.12.23

# Import
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# Picked once and reused for the whole run: a real browser never changes its
# user-agent mid-session, and doing so on every request is a classic bot signal
# that can get individual requests blocked by anti-bot protections.
_cached_user_agent = None

def get_headers():
    global _cached_user_agent

    if _cached_user_agent is None:
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=10)
        _cached_user_agent = user_agent_rotator.get_random_user_agent()

    return _cached_user_agent