from contextlib import contextmanager


@contextmanager
def _agent_manager(agent_type):
    print(f"Agent type is: {agent_type}")
    yield agent_type
    print(f"Close agent: {agent_type}")


def test_agent():
    with _agent_manager("test agent") as agent:
        print("With code")
