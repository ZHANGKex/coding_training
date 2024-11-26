def parse_robots(lines):
    """
    Parse the lines of a robots.txt file and return a list of disallowed URL patterns
    for DoeBot and wildcard (*) user-agents.

    Args:
        lines (List[str]): Lines of the robots.txt file.

    Returns:
        List[str]: Sorted and deduplicated list of disallowed URL patterns.
    """
    disallowed_patterns = set()
    allowed_agent = {"DoeBot", "*"}
    current_agent = ""
    for line in lines:
        line.strip()
        if line.startswith("User-agent"):
            user_agent = line.split(":")[1].strip()
            if user_agent in allowed_agent:
                current_agent = user_agent
            else:
                current_agent = None

        if current_agent:
            if line.startswith("Disallow"):
                disalloed_content = line.split(":")[1].strip()
                if disalloed_content:
                    disallowed_patterns.add(disalloed_content)
    
    return sorted(disallowed_patterns)



if __name__ == "__main__":
    # Exemple de test
    robots_txt_lines = [
        "User-agent: *",
        "Disallow: /private",
        "Disallow: /tmp",
        "",
        "User-agent: DoeBot",
        "Disallow: /data",
        "Disallow: /private",
        "   ",
        "User-agent: OtherBot",
        "Disallow: /admin",
    ]

    # Appel de la fonction
    result = parse_robots(robots_txt_lines)
    print(result)
    # Résultat attendu : ['/data', '/private', '/tmp']
