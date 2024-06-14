from discord import Message

member_counters = {}

def get_response(command: str, sender, mentioned_name, mentioned_display_name: str = None, value: int = 1) -> str:
    
    if mentioned_display_name not in member_counters:
        member_counters[mentioned_display_name] = 0

    if command.lower() == "hello" and mentioned_display_name == "Metlu":
        return "nee pani nuvvu chusko ra chekka"
    
    elif command.lower() == "help" and mentioned_display_name == "Metlu":
        return "Commands: \nhelp @Metlu \nhello @Metlu \nakop \nekkavu <@user> <optional number> \ndigavu <@user> <optional number> \nmetlu \nclear <@user>"
    
    elif command.lower() == "akop":
        return "no suop"
    
    elif command.lower() == "ekkavu":
        if sender.name == 'cookiesdude' and mentioned_name != 'cookiesdude':
            member_counters[mentioned_display_name] += value
            return f"Super kanna {mentioned_display_name}: {member_counters[mentioned_display_name]}"
        elif sender.name != 'cookiesdude' and mentioned_name == 'cookiesdude':
            member_counters[mentioned_display_name] += value
            return f"Super kanna {mentioned_display_name}: {member_counters[mentioned_display_name]}"
    
    elif command.lower() == "digavu":
        if sender.name == 'cookiesdude' and mentioned_name != 'cookiesdude':
            member_counters[mentioned_display_name] -= value
        elif sender.name != 'cookiesdude' and mentioned_name == 'cookiesdude':
            member_counters[mentioned_display_name] -= value
            return f"Chi chi {mentioned_display_name}: {member_counters[mentioned_display_name]}"
    
    elif command.lower() == "metlu":
        filtered_counters = {name: count for name, count in member_counters.items() if name is not None}
        return str(filtered_counters)
    
    elif command.lower() == "clear":
        if sender.name == 'cookiesdude' and mentioned_name != 'cookiesdude':
            member_counters[mentioned_display_name] = 0
            return f"Metlu count {mentioned_display_name}: 0"
        elif sender.name != 'cookiesdude' and mentioned_name == 'cookiesdude':
            member_counters[mentioned_display_name] = 0
            return f"Metlu count {mentioned_display_name}: 0"
