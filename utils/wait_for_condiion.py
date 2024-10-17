import time
from typing import Callable, Any


def wait_for_condition(
        description: str,
        max_retries: int = 10,
        retry_timeout: int = 0.5,
        action: Callable[..., Any] = lambda: True,
        condition: Callable[[Any], bool] = lambda result: bool(result),
) -> Any:
    retries = 0
    condition_result = False
    action_result = None

    while retries < max_retries:
        try:
            retries += 1

            print(f"Trying to achieve condition: '{description}'. Try {retries}/{max_retries}")
            action_result = action()

            if not condition(action_result):
                time.sleep(retry_timeout)
            else:
                return action_result
        except Exception:
            time.sleep(retry_timeout)

    if not condition_result:
        raise AssertionError(f"Failed to achieve the condition in {retries} tries: {description}")

    return action_result
