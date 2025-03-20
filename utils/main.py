import re


def capitalise(p):
    h = p.capitalize()
    
    # Remove extra spaces
    h = re.sub(r'\s+', ' ', h).strip()

    # Capitalize first letter after ".", "?", or "!"
    h = re.sub(r'([.!?])\s*(\w)', lambda m: m.group(1) + " " + m.group(2).upper(), h)

    # Capitalize standalone "i"
    h = re.sub(r'\bi\b', 'I', h)

    h = re.sub(r'\s+([.!?,])', r'\1', h)

    return h

