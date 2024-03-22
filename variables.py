def status_code():
    return 200

def prompt():
    print_prompt = print("Enter vehicle modification you want to search for:  ")

def check_for_loop_done(iterable, action):
    try:
        next(iterable)
    except StopIteration:
        action()

def check_status_code(resp):
    if resp.status_code != 200:
        return f"Error: Response status code is {resp.status_code}."
    else:
        return ""
