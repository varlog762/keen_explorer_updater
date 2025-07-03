def generate_router_ip(login: str) -> str | None:
    if len(login) < 4 or not login[-4:].isdigit():
        return None

    last_four = login[-4:]
    second_octet_tail = last_four[0]
    third_octet_raw = last_four[1:] 

    if int(third_octet_raw) == 0:
        return None

    return f'10.8{second_octet_tail}.{int(third_octet_raw)}.1'




