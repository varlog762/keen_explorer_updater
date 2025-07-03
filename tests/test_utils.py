from utils import generate_router_ip

def test_generate_ip_happy_path():
    """Тестируем стандартный, "счастливый" случай."""
    assert generate_router_ip('user3112') == '10.83.112.1'

def test_generate_ip_with_leading_zero():
    """Тестируем случай с ведущим нулем, который нужно обработать."""
    assert generate_router_ip('user3012') == '10.83.12.1'

def test_generate_ip_invalid_login_too_short():
    """Тестируем невалидный логин (слишком короткий)."""
    assert generate_router_ip('u12') is None

def test_generate_ip_invalid_login_not_digits():
    """Тестируем невалидный логин (не цифры в конце)."""
    assert generate_router_ip('userABCD') is None

def test_generate_ip_zero_octet():
    """Тестируем случай, который должен дать некорректный IP."""
    assert generate_router_ip('user3000') is None